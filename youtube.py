from time import sleep
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import webbrowser
from datetime import date
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def youtube(query,q):
    if 'open youtube' in query:
                print(f"opening youtube...")
                speak(f"opening youtube")
                webbrowser.open(f"https://www.youtube.com/")
    else:
        if 'play' in query or 'song' in query:
            query=query.replace("play","")
            query=query.replace("open","")
            query=query.replace("find","")
            query=query.replace("search","")
            query=query.replace("youtube","")
            str1=''
            str1=query
            print(f"Searching youtube...")
            speak(f"Searching {str1} on youtube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={str1}")
            sleep(5)
            pyautogui.click(x=755, y=500)
        else:
            str1=''
            query=query.replace("search","")
            query=query.replace("youtube","")
            query=query.replace("in","")
            query=query.replace("on","")
            str1=query
            print(f"Searching youtube...")
            speak(f"Searching {str1} on youtube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={str1}")
            sleep(5)
            pyautogui.click(x=755, y=500)

def volume_play(query,q):
    if ('decrease' in query or 'lower' in query) and ('volume' in query):
        for i in range(7):
            pyautogui.hotkey("down")
    elif 'increase' in query  and ('volume' in query):
        for i in range(7):
            pyautogui.hotkey("up")
    elif 'play' in query:
        pyautogui.hotkey('k')
    elif 'pause' in query:
        pyautogui.hotkey('k')
    elif 'fullscreen' in query  or 'full screen' in query:
        pyautogui.hotkey('f')
    elif 'next' in query  or 'previous' in query:
        if 'next' in query:
            pyautogui.hotkey('shift','n')
        else:
            pyautogui.hotkey('shift','p')
    elif 'skip':
        if 'forward' in query:
            pyautogui.hotkey('l')
        else:
            pyautogui.hotkey('j')