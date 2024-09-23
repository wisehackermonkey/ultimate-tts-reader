# # import os
# # import tempfile
# # import subprocess
# # import shutil
# # import winsound

# # # Get the current script directory
# # script_dir = os.path.dirname(os.path.abspath(__file__))

# # # Input text to be converted to speech
# # text_input = input("Enter the text you want Piper to say: ")

# # # Construct the Piper executable path relative to the script's directory
# # piper_executable = os.path.join(script_dir, 'piper', 'piper.exe')

# # # Output file name
# # output_file = "goodbye.wav"

# # # Piper command without echo (we'll provide the text directly via stdin)
# # piper_command = [piper_executable, '--model', 'voices\\en_US-hfc_female-medium.onnx', '--output_file', output_file]

# # # Using TemporaryDirectory to hold temporary files if needed
# # with tempfile.TemporaryDirectory() as temp_folder:
# #     # Run the Piper command and pipe the input text
# #     process = subprocess.Popen(piper_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# #     # Send the text input to Piper and close stdin
# #     stdout, stderr = process.communicate(input=text_input)

# #     if process.returncode == 0:
# #         # Move and rename the file to tts.wave
# #         new_file_path = os.path.join(temp_folder, "tts.wave")
# #         shutil.move(output_file, new_file_path)
        
# #         # Play the renamed file
# #         print(f"Playing the file: {new_file_path}")
# #         winsound.PlaySound(new_file_path, winsound.SND_FILENAME)
# #     else:
# #         print(f"An error occurred: {stderr}")

# #     print(f"Temporary folder: {temp_folder}")


# import os
# import subprocess
# import tempfile
# import shutil
# import winsound
# import signal

# class PiperTTS:
#     def __init__(self):
#         self.process = None
#         self.output_file = "goodbye.wav"

#     def play(self, text_input):
#         # Get the current script directory
#         script_dir = os.path.dirname(os.path.abspath(__file__))

#         # Construct the Piper executable path
#         piper_executable = os.path.join(script_dir, 'piper', 'piper.exe')

#         # Piper command without echo
#         piper_command = [piper_executable, '--model', 'voices\\en_US-hfc_female-medium.onnx', '--output_file', self.output_file]

#         # Using TemporaryDirectory to hold temporary files if needed
#         with tempfile.TemporaryDirectory() as temp_folder:
#             # Run the Piper command and pipe the input text
#             self.process = subprocess.Popen(piper_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#             # Send the text input to Piper and close stdin
#             stdout, stderr = self.process.communicate(input=text_input)

#             if self.process.returncode == 0:
#                 # Move and rename the file to tts.wave
#                 new_file_path = os.path.join(temp_folder, "tts.wave")
#                 shutil.move(self.output_file, new_file_path)

#                 # Play the renamed file
#                 print(f"Playing the file: {new_file_path}")
#                 winsound.PlaySound(new_file_path, winsound.SND_FILENAME)
#             else:
#                 print(f"An error occurred: {stderr}")

#     def stop(self):
#         if self.process:
#             os.kill(self.process.pid, signal.SIGTERM)
#             self.process = None
#             print("Playback stopped.")

# # Create an instance for easy usage
# piper_tts = PiperTTS()

# def play(text):
#     piper_tts.play(text)

# def stop():
#     piper_tts.stop()
import os
import tempfile
import subprocess
import shutil
import winsound
import threading

# Global variable to keep track of the subprocess
current_process = None

def play(text_input):
    global current_process

    # Get the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the Piper executable path
    piper_executable = os.path.join(script_dir, 'piper', 'piper.exe')

    # Output file name
    output_file = "goodbye.wav"

    # Piper command without echo (we'll provide the text directly via stdin)
    piper_command = [piper_executable, '--model', 'voices\\en_US-hfc_female-medium.onnx', '--output_file', output_file]

    # Using TemporaryDirectory to hold temporary files if needed
    with tempfile.TemporaryDirectory() as temp_folder:
        # Run the Piper command and pipe the input text
        current_process = subprocess.Popen(piper_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Send the text input to Piper and close stdin
        stdout, stderr = current_process.communicate(input=text_input)

        if current_process.returncode == 0:
            # Move and rename the file to tts.wave
            new_file_path = os.path.join(temp_folder, "tts.wave")
            shutil.move(output_file, new_file_path)

            # Play the renamed file
            print(f"Playing the file: {new_file_path}")
            winsound.PlaySound(new_file_path, winsound.SND_FILENAME)
        else:
            print(f"An error occurred: {stderr}")

def stop():
    global current_process
    if current_process:
        current_process.terminate()  # Terminate the Piper process
        current_process = None
        print("Playback stopped.")

def play_threaded(text_input):
    # Start the playback in a separate thread
    tts_thread = threading.Thread(target=play, args=(text_input,), daemon=True)
    tts_thread.start()
