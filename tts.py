# class handles keyboard input and reading of the text
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200419

from pynput import keyboard

import pyttsx3
import pyperclip




# example useage
# tts = TTS()

# while True:
#     tts.iterate()
# tts.endloop()


class TTS():
    def __init__(self,speed=None):
        self.engine = pyttsx3.init()

        if speed:
            self.engine.setProperty('rate', speed)

        self.engine.startLoop(False)
        self.listener = keyboard.Listener(
                                    on_press=self.on_press,
                                    on_error=self.onError
                                    )
        self.listener.start()

    def read_text(self, text):
        self.engine.say(text)
    def iterate(self):
        self.engine.iterate()
    def endloop(self):
        self.engine.endLoop()
    # call when any key is pressed
    # goal is to read the clipboard when the insert key is pressed
    def on_press(self,key):
        try:
            # print( str(repr(key)) == '\x03')

            if key == key.insert:
                print("reading clipboard")
                self.engine.say(pyperclip.paste())
        except AttributeError:
            print(f'special key {key} pressed')
            
    def onError(self):
        print("error occurred")