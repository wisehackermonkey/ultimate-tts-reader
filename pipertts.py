import os
import tempfile
import subprocess
import shutil
import winsound
import threading
from pathlib import Path
import sys
import pyperclip
# from plyer import notification

# Show a notification


def show_error(txt, title="Error"):
    ctypes.windll.user32.MessageBoxW(0, txt, title, 1)


    # notification.notify(
    # title="Ultimate TTS",
    # message=txt,
    # app_name="UltimateTTS",
    # timeout=10  # Duration in seconds
    # )
import os
import urllib.request

import zipfile
def setup_piper():
    # Define URLs and output paths
    zip_url = "https://github.com/wisehackermonkey/ultimate-tts-reader/releases/download/resource_file/ultimate_tts_piper_and_voices.zip"
    output_zip_file = str(Path.cwd().joinpath("ultimate_tts_piper_and_voices.zip"))
    

    show_error("downloading piper-tts",title="info")
    # Download the ZIP file
    urllib.request.urlretrieve(zip_url, output_zip_file)

    # Extract the ZIP file
    with zipfile.ZipFile(output_zip_file, 'r') as zip_ref:
        zip_ref.extractall(".")

    # Clean up the temporary ZIP file
    os.remove(output_zip_file)

    show_error("download completed piper-tts voice",title="info")
    

def check_files():
    # Define the paths for the executable and the voice files
    piper_executable = os.path.join("piper","piper.exe")
    onnx_file = os.path.join("voice","en_US-hfc_female-medium.onnx")
    json_file = os.path.join("voice","en_US-hfc_female-medium.onnx.json")
    script_dir =str(Path.cwd())

    # Create a list of files to check
    files_to_check = [piper_executable, onnx_file, json_file]

    # Check if each file exists
    for file in files_to_check:
        file = os.path.join(script_dir,file)
        if not os.path.isfile(file):
            show_error(f"Required file not found: {file}")
            return True 

    print("All required files are present.")
    return False


# Global variable to keep track of the subprocess
current_process = None

def play(text_input):
    global current_process

    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))


 

    # Piper command without echo (we'll provide the text directly via stdin)

    # Using TemporaryDirectory to hold temporary files if needed
    with tempfile.TemporaryDirectory() as temp_folder:
        # Construct the Piper executable path
        current_folder = str(Path.cwd())
        piper_executable = os.path.join(current_folder, 'piper', 'piper.exe')
        output_path = os.path.join(temp_folder, f"tts_{time.time()}.wave")
        piper_command = [piper_executable, '--model', 'voice\\en_US-hfc_female-medium.onnx', '--output_file', output_path]
        # Run the Piper command and pipe the input text
        print(piper_command)
        current_process = subprocess.Popen(piper_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Send the text input to Piper and close stdin
        stdout, stderr = current_process.communicate(input=text_input)
    
        if current_process.returncode == 0:
            # todo fix change gthe outpu directory to here
            # Move and rename the file to tts.wave
            # new_file_path = os.path.join(temp_folder, "tts.wave")
            # shutil.move(output_file, new_file_path)

            # Play the renamed file
            print(f"Playing the file: {output_path}")
            winsound.PlaySound(output_path, winsound.SND_FILENAME)
            os.remove(output_path)
        else:
            print(f"An error occurred: {stderr}")

def stop():
    # current_folder = str(Path.cwd())
    # print("Playback stopped.")
    # python = sys.executable
    # os.execl(python, python, * sys.argv)
        # Get the current script path
    script_path = os.path.abspath(sys.argv[0])
    # Start a new process with the script path
    subprocess.Popen([sys.executable, script_path] + sys.argv[1:])
    # Exit the current process
    sys.exit()

def play_threaded(text_input):
    # Start the playback in a separate thread
    tts_thread = threading.Thread(target=play, args=(text_input,), daemon=True)
    tts_thread.start()




if __name__ == "__main__":
    import ctypes 
    from ctypes import wintypes
    import time 

    

    if check_files():
        show_error("Attempting to download required files please wait...")
        setup_piper()
         # Exit the program with an error status
        show_error("Succesfully downloaded the required files",title="info")
    
    # Call the function
    VK_F2 = 0x71  # Virtual key code for F2
    VK_F3 = 0x72  # Virtual key code for F2
    VK_LMENU = 0xA4  # Virtual key code for Left Alt
    VK_RMENU = 0xA5  # Virtual key code for Right Alt
    VK_LCONTROL = 0xA2  # Virtual key code for Left Control
    VK_RCONTROL = 0xA3  # Virtual key code for Right Control

    user32 = ctypes.windll.user32

    def is_key_pressed(vk):
        return user32.GetAsyncKeyState(vk) & 0x8000 != 0
    
    while True:
        alt_left_pressed = is_key_pressed(VK_LMENU)
        alt_right_pressed = is_key_pressed(VK_RMENU)
        ctrl_left_pressed = is_key_pressed(VK_LCONTROL)
        ctrl_right_pressed = is_key_pressed(VK_RCONTROL)
        f2_pressed = is_key_pressed(VK_F2)
        print(".", end="")
        if alt_left_pressed:
            print("l")
        if alt_right_pressed:
            print("r")
            
        if f2_pressed:
            print("f")

        if (ctrl_left_pressed or ctrl_right_pressed):
            print("c")
        if (alt_left_pressed or alt_right_pressed) and f2_pressed:

        # if (alt_left_pressed or alt_right_pressed) and f2_pressed:
            print("ALT + f2 is pressed!")
            play_threaded(pyperclip.paste())
            time.sleep(2)
        if (ctrl_left_pressed or ctrl_right_pressed) and f2_pressed:
            print("stopping")

            stop()
        
        time.sleep(0.1)