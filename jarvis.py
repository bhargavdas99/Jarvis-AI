from time import sleep
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from bs4 import BeautifulSoup
import requests
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
from datetime import date
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet(r):
    if  r==0:
        print("Jarvis here.How may I help you sir?")       
        speak("Jarvis here. How may I help you sir?") 
    elif r==1:
        print("Your Super Advanced A.I Jarvis at your Service..Waiting for your command Sir...")       
        speak("your super advanced a i Jarvis at your Service. Waiting for your command Sir..") 
    elif r==2:
        print("Jarvis at your Service Sir.Hope you are doing well Today...")       
        speak("Jarvis at your Service Sir. Hope you are doing well TODAY") 
    else:
        print("Jarvis here. Its an honor to be at your service...")       
        speak("Jarvis here. Lets do this sir") 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    r = random.randrange(4)
    if hour>=0 and hour<12:
        print("Good morning Sir!")
        speak("Good morning Sir Bhaargab!")
        speak("A new day to rule the world")
        greet(r)
    elif hour>=12 and hour<18:
        print("Good afternoon Sir!")
        speak("Good afternoon Sir Bhaargab!")
        greet(r)
    else:
        print("Good evening Sir!")
        speak("Good evening Sir Bhaargab!") 
        greet(r)

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    wishMe()
    
    while True:
    # if 1:
        query = takeCommand().lower()
        q= query.split(" ")

        # Logic for executing tasks based on query
        if ('my' in query or 'you' in query and 'play' not in query and 'youtube' not in query):
            from personal import personal_queries
            personal_queries(query)


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif (('youtube' in query) or ('play' in query and len(q)<4) or ('song' in query)):
            print('caught')
            from youtube import youtube
            youtube(query,q)

        elif 'volume' in query or 'play'  in query or 'pause'  in query or 'skip'  in query or 'full screen' in query  or 'fullscreen' in query  or 'full screen' in query  or 'next video' in query  or 'previous' in query:
            from youtube import volume_play
            volume_play(query,q)


        elif ('map' in query):
            if 'open map of' in query:
                query=query.replace("open map of","")
                print(f"Opening map of {query}")
                speak(f"opening map of {query}")
                webbrowser.open(f"https://www.google.com/maps/place/{query}")
            else:
                print("please say: \'open Map of \"place\"\' ")
                speak("please say open Map of followed by the name of the place ")
                takeCommand()
                if 'open map of' in query:
                    query=query.replace("open map of","")
                    print(f"Opening map of {query}")
                    speak(f"opening map of {query}")
                    webbrowser.open(f"https://www.google.com/maps/place/{query}")
                else:
                    continue
        
        elif 'google' in query and len(q)<3:
            speak("opening google")
            webbrowser.open("https://www.google.com")

        elif 'flipkart' in query and len(q)<3:
            speak("opening flipkart")
            webbrowser.open("https://www.flipkart.com")
        
        elif 'amazon' in query and len(q)<3:
            speak("opening amazon")
            webbrowser.open("https://www.amazon.in")

        elif 'stackoverflow' in query and len(q)<3:
            speak("opening stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")   

# ----------------------------------TIME,TEMPERATURE,ALARM----------------------------------------------

        elif 'play music' in query :
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'date' in query or "day" in query:
            today = date.today()
            today = str(today)

            today = today.split("-")
            month=''
            if today[1]=='01':
                month='January'
            elif today[1]=='02':
                month="February"
            elif today[1]=='03':
                month="March"
            elif today[1]=='04':
                month="April"
            elif today[1]=='05':
                month="May"
            elif today[1]=='06':
                month="June"
            elif today[1]=='07':
                month="July"
            elif today[1]=='08':
                month="August"
            elif today[1]=='09':
                month="September"
            elif today[1]=='10':
                month="October"
            elif today[1]=='11':
                month="November"
            else:
                month="December"

            if today==['2023', '03', '10']:
                print(f"Today is the birth day of the great Bhargab. Happy birthday sir Bhargab! ")
                speak(f"Today March 10th is the birth day of the great Bhargab das. Happy birthday sir Bhargab! ")
                continue
            print(f"Today's date is {today[2]} {month} {today[0]}")
            speak(f"Today's date is {today[2]}th {month} {today[0]}")

        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            time = strTime.split(":")
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<10:
                print(f"{time[0]}:{time[1]} AM ")
                speak(f"Sir, the time is {time[0][1]} {time[1]} a m")
            elif hour>=10 and hour<12:
                print(f"{time[0]}:{time[1]} AM ")
                speak(f"Sir, the time is {time[0]} {time[1]} a m")  
            elif hour==12:
                print(f"{time[0]}:{time[1]} PM ")
                speak(f"Sir, the time is {time[0]} {time[1]} a m")    
            else:
                print(f"{hour-12}:{time[1]} PM ")
                speak(f"Sir, the time is {hour-12} {time[1]} p m")

        elif 'temperature' in query or 'weather' in query and ('chrome' not in query or 'google' not in query):
            search = "temperature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div", class_= "BNeawe").text
            print(f"The temperature is {temperature} at your location.")
            speak(f"The temperature is {temperature} at your location.")

        elif "set" in query and "alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")
        
        elif "remember that" in query or 'remind me' in query:
            rememberMessage = query.replace("remember that","")
            rememberMessage = query.replace("jarvis","")
            speak("You told me to "+rememberMessage)
            remember = open("Remember.txt","a")
            remember.write(rememberMessage)
            remember.close()

        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())

# ------------------------------------------------------------------------------------------------------     

        elif ("close" in query and len(q)>=2 and 'please' not in query) or (('pc' in query or 'windows' in query) and 'sleep' in query):
            from Dictapp import closeappweb
            closeappweb(query)

        elif "go to" in query and "tab" in query:
            
            if "one" in query or '1' in query:
                pyautogui.hotkey("ctrl",'1')
            elif 'two' in query  or 'tab to'in query  or '2' in query:
                pyautogui.hotkey('ctrl','2')
            elif 'three' in query or '3' in query:
                pyautogui.hotkey('ctrl','3')
            elif 'four' in query or '4' in query:
                pyautogui.hotkey('ctrl','4')
            elif 'five' in query or '5' in query:
                pyautogui.hotkey('ctrl','5')
            elif 'six' in query or '6' in query:
                pyautogui.hotkey('ctrl','6')
            elif 'seven' in query or '7' in query:
                pyautogui.hotkey('ctrl','7')
            elif 'eight' in query or '8' in query:
                pyautogui.hotkey('ctrl','8')
            elif 'nine' in query or '9' in query:
                pyautogui.hotkey('ctrl','9')
            elif 'ten' in query or '10' in query:
                pyautogui.hotkey('ctrl','10')
            else:
                query = query.replace('go to tab','')
                query = query.replace(' ','')
                pyautogui.hotkey('ctrl',query)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "dasbhargab19@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")      

        elif (('close' in query and len(q)==1) or ('quit' in query) or ('exit' in query) or ('bye' in query) or ('bi' in query) or ('goodbye' in query) or ('go to sleep' in query) or ('good night' in query)):
            hour = int(datetime.datetime.now().hour)
            if (hour>7 and hour<16): 
                print("See ya. Have a great day Sir!")
                speak("See yaa!. Have a great day Sir!")
            elif(hour>=16 and hour<23):
                print("See ya. Have a pleasant evening Sir!")
                speak("See yaa!. Have a pleasant evening Sir!")   
            elif(hour>1):
                print("Exiting now. Good Night Sir!Sweet Dreams. See you in the morning.")
                speak("Exiting now. Good Night Sir!Sweet Dreams. See you in the morning.")
            else:
                print("Exiting now. Good Night Sir!Sweet Dreams")
                speak("Exiting now. Good Night Sir!Sweet Dreams")
            exit()
 # ===============================================================================================

        elif(query==None or "none" in query):
            continue
        else:
            from Dictapp import openappweb
            openappweb(query,q)