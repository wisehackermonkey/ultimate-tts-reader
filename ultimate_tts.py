from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
import threading
import subprocess
import ctypes 
from ctypes import wintypes
import time
import sys

import pipertts


state = False
run_tts = False
speed = 1.0
global tts_thread
global is_stop
is_stop = False

VK_F2 = 0x71  # Virtual key code for F2
VK_LMENU = 0xA4  # Virtual key code for Left Alt
VK_RMENU = 0xA5  # Virtual key code for Right Alt

user32 = ctypes.windll.user32

def is_key_pressed(vk):
    return user32.GetAsyncKeyState(vk) & 0x8000 != 0



def create_image():
    # Create an image for the tray icon
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle([width // 4, height // 4, width * 3 // 4, height * 3 // 4], fill=(0, 128, 255))
    return image



def on_clicked(icon, item):
    global state
    state = not item.checked


def monitor_keys():
    while True:
        alt_left_pressed = is_key_pressed(VK_LMENU)
        alt_right_pressed = is_key_pressed(VK_RMENU)
        f2_pressed = is_key_pressed(VK_F2)
        print(".", end="")
        if alt_left_pressed:
            print("l")
        if alt_right_pressed:
            print("r")
            
        if f2_pressed:
            print("f")
        if (alt_left_pressed) and f2_pressed:

        # if (alt_left_pressed or alt_right_pressed) and f2_pressed:
            print("ALT + f2 is pressed!")
            pipertts.play_threaded("Wrapper Functions: play and stop provide a simple interface to interact with the PiperTTS class. You can further enhance this library with error handling, logging, or more features as needed!")
        if (alt_right_pressed) and f2_pressed:
            print("stopping")

            pipertts.stop()
        
        time.sleep(0.1)
def on_quit(icon, item):
    global tts_thread
    tts_thread.set()
    tts_thread.join()#  a hack to kill the thread
    icon.stop()
def stop_tts(icon, item):
    # print("stopping")
    # pipertts.stop()
    pass
def monitor_toggle(icon, item):
    global run_tts
    run_tts = not item.checked
    pass
def faster_speed(icon, item):
    pass
def slower_speed(icon, item):
    pass
def default_speed(icon, item):
    pass
def about_program(icon, item):
    icon.notify("Created by oran collins (wisehackermonkey) 2024-09-22") 
if __name__ == "__main__":
    tts_thread = threading.Thread(target=monitor_keys, daemon=False)
    tts_thread.start()

    icon = icon("clipyserver", create_image(), "Clipy Server", menu=menu(
        item("Stop TTS", stop_tts),
        item("Toggle monitor Ctrl + C", monitor_toggle, checked=lambda item: run_tts),
        item("change speed",
             menu(
                 item("faster", faster_speed),
                 
                 item("slower", slower_speed),
                 
                 item("Default", default_speed),
             )),
        item("about", about_program),
        item("Quit", on_quit)
    ))
    icon.run()


  