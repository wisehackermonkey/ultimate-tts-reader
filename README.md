# ultimate-tts-reader
####  awesome app to read text from the clipboard when you press the insert key
```
by oran collins
github.com/wisehackermonkey
oranbusiness@gmail.com
20200415
```

# how to install 

```
git clone https://github.com/wisehackermonkey/ultimate-tts-reader.git
cd ultimate-tts-reader
pip install -r requirements.txt
```

# how to run 

#### windows only
```
python ./main.py
```
## Useage
```
copy something to the clipboard
press 'insert' on the keyboard
the computer should read the text to you!
```


## How to build windows exe
### install pyinstaller 
```
>pip install pyinstaller 
```
```
cd /path/to/project
```
### Simple build
```
pyinstaller --hidden-import=pyttsx3.drivers  --hidden-import=pyttsx3.drivers.sapi5 --noconsole --onefile app.py
```
### clean build 
```
pyinstaller --noconsole --hidden-import=pyttsx3.drivers  --hidden-import=pyttsx3.drivers.sapi5 --specpath ${PWD}/builds --distpath ${PWD}/builds/dist --workpath ${PWD}/builds/build --onefile app.py 
```
### Advanced (windows powershell) Build, move exe  to to windows folder, includes moving of build files to ./builds 
```
add move to windows folder 
NOTE mv -force overwrites the exe (and is a powershell command)

> pyinstaller --noconsole --hidden-import=pyttsx3.drivers  --hidden-import=pyttsx3.drivers.sapi5 --specpath ${PWD}/builds --distpath ${PWD}/builds/dist --workpath ${PWD}/builds/build --onefile app.py ; mv -force ${PWD}/builds/dist/app.exe ${PWD}/windows/app.exe
```


## Improvements
- pause key/button
- fix quit on escape
- ~~change stop use TK to quit~~
- ~~change stop key to fn + insert~~
- slow down the voice
- catch KeyboardInterrupt graceful shutdown
- Copy selected text to clipboard or copy selected text and read it
- dependence injection
- change voice
- ~~gui mvp~~



## Links
```
tts
https://pyttsx3.readthedocs.io/en/latest/engine.html#examples

keyboard
https://pynput.readthedocs.io/en/latest/keyboard.html

posible solution to pause key
https://github.com/nateshmbhat/pyttsx3/issues/35
```