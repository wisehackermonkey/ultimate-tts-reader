# ultimate-tts-reader
# awesome app to read text from the clipboard when you press the insert key

# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200419

import sys

# class handles keyboard input and reading of the text
from tts import TTS

# custom gui script for generating tkinter
# windows containing play and quit buttons
from gui import App

# set the speed at which the computer says words
voice_speed = 200

# gui for program
app = App()
# text to speech for program
tts = TTS(speed = voice_speed)

print("Ultimate tts reader:")
print("press escape to quit program <ESC>")

# external loop not part of tkinker thread
# loop exits when the tkinter windows is closed

while app.is_alive():
    tts.iterate()
print("Quitting..")
sys.exit()
tts.endloop()
