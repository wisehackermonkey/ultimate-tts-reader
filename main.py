from pynput import keyboard


import pyttsx3
import pyperclip


engine = pyttsx3.init()



def read_text(text):
    engine.say(text)
    engine.runAndWait()


# call when any key is pressed
# goal is to read the clipboard when the insert key is pressed
def on_press(key):
    try:
        # print(f'alphanumeric key { key.char} pressed')
        if key == key.insert:
            print("works")
            engine.say(pyperclip.paste())
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        print("stoped the listener")
        return False

def onWord(name, location, length):
    print ('word', name, location, length)
    if keyboard.is_pressed("esc"):
       engine.stop()


# def wait_for_insert_keypress():




if __name__ == "__main__":
    print("Ultimate tts reader:")
    print("press escape to quit program <ESC>")
    # read_text("Welcome to Ultimate tts reader. To quit press the escape key.")

    # start of main program
    # wait_for_insert_keypress()
    # read_text(pyperclip.paste())
    
    engine = pyttsx3.init()
    engine.connect('started-word', onWord)

    # engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
    engine.startLoop(False)
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    while True:
        # try:

        engine.iterate() 

        # except: 
        #     break
      
        
        # must be called inside externalLoop()
    engine.endLoop()
      

    # Notes
    # - we should sanitize parts
    # - what should we print next
    # - update him on what she said
    # - express: i want to laser cut masks fabric, they might not need face shield. will see