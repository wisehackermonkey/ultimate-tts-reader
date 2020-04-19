import tkinter as tk
import threading
global test
test = 0
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
    def printhello(self):
        print("hello")
    def run(self):
        self.root = tk.Tk()

        # set window name 
        self.root.title("Ultimate TTS Reader")

        #set minimum window size
        self.root.minsize(100,50)

        # setup quit callback on windows close
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
       
        label = tk.Label(self.root, text="Ultimate TTS Reader")
        label.pack()

        button = tk.Button(self.root, justify="center", text="play", command=self.printhello)
        button.pack()

        self.quit = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit.pack(side="bottom")


        self.root.mainloop()

app = App()



print("Ultimate tts reader:")
print("press escape to quit program <ESC>")

import time
while app.is_alive():
    time.sleep(1)
    print(app.is_alive())