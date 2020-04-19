from pynput import keyboard


import pyttsx3
import pyperclip


class TTS():
    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.connect('started-word',self. onWord)

        self.engine.startLoop(False)
        self.listener = keyboard.Listener(
                                    on_press=self.on_press,
                                    on_release=self.on_release,
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
            if key == key.insert:
                print("reading clipboard")
                # if not pyperclip.is_available():  
                    # print("Copy functionality unavailable!") 
                    # return
                self.engine.say(pyperclip.paste())
            if key == keyboard.Key.esc:
                print("Pressed escape")
                self.engine.stop()
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
    # when kill key is pressed the event handler is killed.
    # this is done by returning "False"
    def on_release(self,key):
        # if key == keyboard.Key.esc:
    #         # Stop listener
        print("stopped the listener")
            # self.engine.stop()
            # return False

    def onWord(self,name, location, length):
        print('word', name, location, length)
        #     print ('word', name, location, length)
        # if keyboard.is_pressed("esc"):
            # print("Stop")
            # engine.stop()
            # keyboard.Listener.stop
        return False
    def onError(self):
        print("error occured")

if __name__ == "__main__":
    print("Ultimate tts reader:")
    print("press escape to quit program <ESC>")

    # start of main program
    
    # engine = pyttsx3.init()
    # engine.connect('started-word', onWord)

    # engine.startLoop(False)
    # listener = keyboard.Listener(
    #                              on_press=on_press,
    #                              on_release=on_release,
    #                              on_error=onError
    #                              )
    # listener.start()

    # read_text("Starting.")# To quit press the fn plus the insert key.")

    tts = TTS()

    while True:
        tts.iterate()
    tts.endloop()
    #     engine.iterate()         
    # engine.endLoop()