# class handles keyboard input and reading of the text
from tts import TTS

# custom gui script for generating tkinter
# windows containing play and quit buttons

from gui import App



import sys
# added to fix a anonying error with pyinstaller 
#EX: "[123972] Failed to execute script pyi_rth_win32comgenpy"



app = App()
tts = TTS()

print("Ultimate tts reader:")
print("press escape to quit program <ESC>")

# external loop not part of tkinker thread
# loop exits when the tkinter windows is closed
while app.is_alive():
    # time.sleep(1)
    # print(app.is_alive())
    tts.iterate()
sys.exit()
tts.endloop()