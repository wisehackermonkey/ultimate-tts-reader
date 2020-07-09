from pynput import keyboard


import pyttsx3
import pyperclip


engine = pyttsx3.init()


def read_text(text):
    engine.say(text)


# call when any key is pressed
# goal is to read the clipboard when the insert key is pressed
def on_press(key):
    try:
        if key == key.insert:
            print("reading clipboard")
            engine.say(pyperclip.paste())
        if key == keyboard.Key.esc:
            print("Pressed escape")
            engine.stop()
    except AttributeError:
        print(".")
        # print('special key {0} pressed'.format(key))

# when kill key is pressed the event handler is killed.
# this is done by returning "False"
def on_release(key):
    # if key == keyboard.Key.esc:
#         # Stop listener
    print("stoped the listener")
        # engine.stop()
        # return False

def onWord(name, location, length):
    print('word', name, location, length)
    #     print ('word', name, location, length)
    # if keyboard.is_pressed("esc"):
        # print("Stop")
        # engine.stop()
        # keyboard.Listener.stop
    return False
def onError():
    print("error occured")

if __name__ == "__main__":
    print("Ultimate tts reader:")
    print("press escape to quit program <ESC>")

    # start of main program
    
    # engine = pyttsx3.init()
    engine.connect('started-word', onWord)

    engine.startLoop(False)
    listener = keyboard.Listener(
                                 on_press=on_press,
                                 on_release=on_release,
                                 on_error=onError
                                 )
    listener.start()

    read_text("Starting.")# To quit press the fn plus the insert key.")


    while True:
        engine.iterate()         
    engine.endLoop()