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

dictapp = {"commandprompt":"cmd","paint":"mspaint","chrome":"chrome","word":"winword","excel":"excel","chrome":"chrome","code":"code","powerpoint":"powerpnt","notepad":"notepad","calculator":"calc","whatsapp":"whatsapp://","settings":"ms-settings:","task manager":"taskmgr"}
dictapp1 = {"commandprompt":"cmd","paint":"mspaint","chrome":"chrome","word":"winword","excel":"excel","chrome":"chrome","code":"code","powerpoint":"powerpnt","notepad":"notepad","skyrim":"SkyrimSE","calculator":"CalculatorApp","whatsapp":"WhatsApp","settings":"SystemSettings","task manager":"Taskmgr","pc":"rundll32.exe powrprof.dll, SetSuspendState Sleep","windows":"rundll32.exe powrprof.dll, SetSuspendState Sleep"}

def openappweb(query,q):
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        speak(f"opening https://www.{query}")
        webbrowser.open(f"https://www.{query}")
    elif('skyrim' in query):
        print("Opening SKYRIM...")
        speak("Opening SKY RIM")
        os.startfile("D:\\Games\\The Elder Scrolls V Skyrim Anniversary Edition\\SkyrimSE.exe")
    elif("search" in q or "what" in q  or "is" in q or "are" in q or "how" in q or "why" in q ):
        m=[]
        l=["search",'chrome',"google","yahoo","edge","the","bing","what","find","on","internet","net"]
        for i in q:
            if i not in l:
                m.append(i)
        str1 = ""
        for ele in m:
            str1 += ele+" "
        speak(f"Searching {str1}")
        webbrowser.open(f"https://www.google.com/search?q={str1}")

    else:        
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak(f"launching {app}")
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    if(('pc' in query or 'windows' in query) and 'sleep' in query):
        keys = list(dictapp1.keys())
        for app in keys:
            if app in query:
                speak(f"putting {app} to sleep mode")
                os.system(f"start {dictapp1[app]}")
    else:
        speak("Closing,sir")
        if "one tab" in query or "1 tab" in query:
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "2 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "3 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
            
        elif "4 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")
        elif "5 tab" in query:
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            sleep(0.5)
            pyautogui.hotkey("ctrl","w")
            speak("All tabs closed")

        
        else:
            keys = list(dictapp1.keys())
            for app in keys:
                if app in query:
                    os.system(f"taskkill /f /im {dictapp1[app]}.exe")