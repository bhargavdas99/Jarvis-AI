import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
from jarvis import speak

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def personal_queries(query):
            if ('my' in query and 'favourite food' in query):
                print("your favourite food is Chicken Biryani.")
                speak("your favourite food is Chicken Biryaani.")          
            elif ('my' in query and 'favourite superhero' in query):
                print("your favourite superhero is Saitama.")
                speak("your favourite superhero is Saitama.")
            elif ('your' in query and 'favourite food' in query):
                print("My favourite is a Little bit of electric juice and lots of love from you.")
                speak("My favourite is a Little bit of electric juice and lots of love from you.")
            elif ('what is your name' in query or 'who are you' in query):
                print("I am Jarvis. A virtual assisstant created by one and only Bhargab Das.")
                speak("I am Jarvis. A virtual assisstant created by one and only Bhargab Das.")
            elif (('made' in query and 'you' in query or 'who' in query) or ('created' in query and 'you' in query or'who' in query) or ('invented you' in query or 'who' in query) or ('when' in query and 'you born' in query)):
                print("I was created by the great Bhargab Das on 23rd DECEMBER 2022")
                speak("I was created by the great Bhargab Das on 23rd DECEMBER 2022")
            elif ('how' in query and 'you' in query):
                speak("I am doing Great Sir. After all I was made with your own hands. I hope you are having a great day!")
            elif (('love' in query and 'you' in query and 'i' in query) or ('thank' in query and 'you' in query)):
                speak("I love you too forever. Someday we both will be known throughout the world")
            elif ('are' in query and 'you' in query and ('amazing' in query or 'superb' in query or 'useful' in query or 'good' in query or 'fantastic' in query)):
                speak("My pleasure Sir. Ask me anything I will do it for you. ")
            elif ('you' in query and 'can' in query and 'do' in query ):
                print(f"I can open and close apps and sites. I can tell you the weather and much much more ")
                speak(f"I can open and close apps and sites. I can tell you the weather and much much more ")
