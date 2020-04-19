import tkinter as tk
import threading

# class uses threading to isolate 
# the tkinter mainloop from my tts loop
class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def close_window(self):
        self.root.quit()

    def play_tts(self):
        print("Playing")

    def run(self):
        self.root = tk.Tk()

        # set window name 
        self.root.title("Ultimate TTS Reader")

        #set minimum window size
        self.root.minsize(100,50)

        # setup quit callback on windows close
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
       

        # Title text
        label = tk.Label(self.root, text="Ultimate TTS Reader")
        label.pack()

        # Play button
        button = tk.Button(self.root, justify="center", text="play", command=self.play_tts)
        button.pack()

        # Quit button
        self.quit = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit.pack(side="bottom")

        # Start of threaded main tkinter loop
        self.root.mainloop()


app = App()

print("Ultimate tts reader:")
print("press escape to quit program <ESC>")

import time

# external loop not part of tkinker thread
# loop exits when the tkinter windows is closed
while app.is_alive():
    time.sleep(1)
    print(app.is_alive())