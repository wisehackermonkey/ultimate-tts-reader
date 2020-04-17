from pynput import keyboard


import pyttsx3
import pyperclip


# engine = pyttsx3.init()



def read_text(text):
    engine.say(text)
    # engine.runAndWait()


# call when any key is pressed
# goal is to read the clipboard when the insert key is pressed
def on_press(key):
    try:
        if key == key.insert:
            print("works")
            engine.say(pyperclip.paste())
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print("stoped the listener")
        return False

def onWord(name, location, length):
    print ('word', name, location, length)
    if keyboard.is_pressed("esc"):
       engine.stop()
       return False


# def wait_for_insert_keypress():




if __name__ == "__main__":
    print("Ultimate tts reader:")
    print("press escape to quit program <ESC>")

    # start of main program
    
    engine = pyttsx3.init()
    engine.connect('started-word', onWord)

    engine.startLoop(False)
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    read_text("Starting. To quit press the fn plus the insert key.")


    while True:
        # try:

        engine.iterate() 

        # except: 
        #     break
      
        
    engine.endLoop()