# visual part of the app shows window with play and quit buttons
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200419

import tkinter as tk
import threading
import sys
import os

# location of server address, app version number
from client_config import ClientConfig

# download and update app to new version
import update 

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

    def restart(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        print("Stopping")
        python = sys.executable
        os.execl(python, python, * sys.argv)

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

        # TODO add pause button

        # Stop button
        button = tk.Button(self.root, justify="center", text="Stop", command=self.restart)
        button.pack()


        # Update app button
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.root,tearoff=0)


        self.filemenu.add_command(label="Update", command=update.check_for_update)
        self.filemenu.add_command(label="Exit", command=self.close_window)

        self.menubar.add_cascade(label="Options", menu=self.filemenu)


        # display the menu
        self.root.config(menu=self.menubar)

        # Quit button
        self.quit = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit.pack(side="bottom")

        # Start of threaded main tkinter loop
        self.root.mainloop()