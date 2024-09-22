from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
import threading
state = False
run_tts = False
speed = 1.0
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
        pass

def on_quit(icon, item):
    icon.stop()
def stop_tts(icon, item):
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
    tts_thread = threading.Thread(target=monitor_keys, daemon=True)
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