from io import StringIO
from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui
import pywhatkit
import smtplib
import playsound
from bs4 import BeautifulSoup
import requests
import psutil

from wikipedia.wikipedia import languages

print('Initializing Jarvis...')

MASTER = "pratham" 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak funtion
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wish me function
def wishMe():
    
    hour = int(datetime.datetime.now().hour) 
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER )

    elif hour>12 and hour<18:
        speak("Good Afternoon" + MASTER )

    else:
        speak("Good Evening" + MASTER )
    speak(" how may I help you") 
#take command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listerning...")
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:   
        print("Say that again please")
        TaskEecution()
        query = None
    return query
def Temp():
        search = "temperature in kichha"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} ")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            speak("no problem sir")

def screenshort():
    speak("Ok Boss , What Should I Name That File ?")
    path = takeCommand()
    path1name = path + ".png"
    path1 = "F:\\Pictures\\screen short\\"+ path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("F:\\Pictures\\screen short")
    speak("Here Is Your ScreenShot")
def TaskEecution():
    while True:
        query = takeCommand()
        
        #logic for executing tasks as per query..
        if 'wikipedia' in query.lower():
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)
        battery = psutil.sensors_battery()
        percentage = battery.percent  
        elif percentage>95 and percentage<97:
                playsound.playsound('f:\\code\\sound\\Battery Charged.mp3')

        elif percentage<25 and percentage>5:
            playsound.playsound('f:\\code\\sound\\Jarvis Low Power Message Tone.mp3') 
        
        elif "battery" in query.lower():
            if percentage>95 and percentage<97:
                playsound.playsound('f:\\code\\sound\\Battery Charged.mp3')

            if percentage<25 and percentage>5:
                playsound.playsound('f:\\code\\sound\\Jarvis Low Power Message Tone.mp3')
        elif 'open youtube' in query.lower():
            speak('Opening youtube..')
            webbrowser.open("www.youtube.com")

        elif "thank you" in query.lower():
            speak('its my job sir!')

        elif "jokes" in query.lower():
            speak('telling some jokes')
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            speak('should i tell other joke')
            response = takeCommand()
            if response == 'yes':
                 joke_2 = pyjokes.get_joke()
                 print(joke_2)
                 speak(joke_2)
                 
            else:
                pass
        
        elif 'play' in query.lower():
                song = query.replace('play', '')
                print(query)
                print("playing" + song)
                speak("playing" + song)
                pywhatkit.playonyt(song)

        elif 'play video ' in query.lower():
                video = query.replace('play', '')
                print(query)
                speak("playing" + video)
                pywhatkit.playonyt(video)

        elif 'open google' in query.lower():
            speak('Opening google..')
            webbrowser.open("www.google.com") 

        elif 'music' in query.lower():
            songs_dir = "f:\\Music"  
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[1]))

        elif "the time" in query.lower():
            time = datetime.datetime.now().strftime("%I:%M:%S")
            print(time)
            speak(time)
        

        elif "open code" in query.lower():
            speak('opening visual studio code') 
            codepath = "F:\\code\\vs code\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "close code" in query.lower():
            speak('closeing visual studio code') 
            os.close(codepath)

        elif "open zoom" in query.lower(): 
            speak('opening zoom')
            zoompath = "C:\\Users\\prath\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoompath)


        elif 'search' in query.lower():
            search = query.replace('search', '')
            print(search)
            speak("searching" + search)
            pywhatkit.search(search)

        elif 'opening whatsapp' in query.lower():
            speak('Opening whatsapp...')
            webbrowser.open('https://web.whatsapp.com/')

        elif 'online classes' in query.lower():
            speak('Opening E connect...')
            webbrowser.open('https://eck12student.jupsoft.com/sisStudentLoginNew.aspx?id=59HAojtXA6w%3d')

        elif 'play song' in query.lower():
                song = query.replace('play', '')
                print(query)
                speak("playing" + song)
                pywhatkit.playonyt(song)

        elif 'open amazon' in query.lower():
            amazon = query.replace('open amazon', 'opening amazon')
            speak(amazon)
            webbrowser.open("www.amazon.in")

        elif 'open chrome' in query.lower():
            speak("Opening google chrome...")
            webbrowser.open("www.chrome.com")

        elif 'open youtube' in query.lower():
            speak("Opening youtube...")
            webbrowser.open("www.youtube.com")

        elif 'battery percentage' in query.lower():
            battery = psutil.sensors_battery()
            percentage = battery.percent  
            speak(percentage)

        elif 'open gmail' in query.lower():
            speak("opening Gmail...")
            webbrowser.open('https://mail.google.com/')

        elif 'play video ' in query.lower():
                video = query.replace('play', '')
                print(query)
                speak("playing" + video)
                pywhatkit.playonyt(video)

        elif 'shutdown' in query.lower():
            playsound.playsound("f:\\code\\sound\\JARVIS Goodbye Sir.mp3")
            playsound.playsound('f:\\code\\sound\\power down.mp3')
            exit()

        elif "alarm" in query.lower():
            speak("enter the time!")
            time = input()

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    playsound.playsound("f:\\code\\sound\\ironman.mpeg")
                    playsound.playsound('F:\\code\\sound\\Jarvis Alarm.mp3')                   
                    speak("alarm closed!")

                elif now>time:
                    break    


        elif 'calculate' in query.lower():
            speak('ok sir! speak your values...')
            speak('speak your value 1... ')
            val1 = takeCommand()
            speak('speak your value 2...')
            val2 = takeCommand()
            speak('speak your opreation sir')
            oprerator= takeCommand()
            
            if oprerator=="addition":
                speak('addition of value1 and value2 is')
                add = float(val1) + float(val2)
                print(add)
                speak(add)

            elif oprerator=="substraction":
                speak('substraction of value1 and value2 is')
                sub = float(val1) - float(val2)
                print(sub)
                speak(sub)

            elif oprerator=="multiplication":
                speak('multiplication of value1 and value2 is')
                mul = float(val1) * float(val2)
                print(mul)
                speak(mul)

            elif oprerator=="division":
                speak('division of value1 and value2 is')
                div = float(val1) / float(val2)
                print(div)
                speak(div)

            else:
                speak('I does not able to find solution! let me try ')
                pywhatkit.search('val1,oprerator,val2')

        elif 'who are you' in query.lower():
            print('J A R V I S (Just A Rather Very Intelligent System) is a fictional character voiced by Paul Bettany in the Marvel Cinematic Universe (MCU) film franchise, based on the Marvel Comics characters Edwin Jarvis and H.O.M.E.R., respectively the household butler of the Stark family and another AI designed by Stark. J.A.R.V.I.S. is an artificial intelligence created by Tony Stark, who later controls his Iron Man and Hulkbuster armor for him. ')   
            speak('J A R V I S (Just A Rather Very Intelligent System) is a fictional character voiced by Paul Bettany in the Marvel Cinematic Universe (MCU) film franchise, based on the Marvel Comics characters Edwin Jarvis and H.O.M.E.R., respectively the household butler of the Stark family and another AI designed by Stark. J.A.R.V.I.S. is an artificial intelligence created by Tony Stark, who later controls his Iron Man and Hulkbuster armor for him. ')   

        elif 'games' in query.lower():
            speak("here are the games i found in this system")
            speak("gta vice city")

            speak('now tell me which game i should open for you')
            Gchoice = takeCommand()
            if 'gta' in Gchoice.lower():
                speak('Opening gta vice city')
                gtapath = "E:\\gta vc\\gta-vc.exe"
                os.startfile(gtapath)

            else:
                speak('sorry we could not find the game you searched')
                speak('let me search in browser')
                pywhatkit.search('Gchoice')
                
        if 'send whatsapp message' in query.lower():
            speak("sir to whom you like to send message")  
            speak('speak name')    
            P_name = takeCommand()
            speak('what message should i send')
            W_message = takeCommand() 
            

        if 'automate' in query.lower():
            speak('sir plz speak the text')
            A_message = takeCommand()
            print(A_message)

        elif 'movies' in query.lower():
            speak('showing all movies in this system..')
            os.startfile("E:\\encypeted\\movies")

        if 'are you there' in query.lower():
            speak('always for you sir! tell me your command')
            speak('listerning....')
            TaskEecution()

        elif 'screenshot' in query.lower():
            screenshort()

        elif 'temperature' in query.lower():
            Temp()


        if query==None:
            TaskEecution()

        else:
            TaskEecution()
def startup():
    playsound.playsound('f:\\code\\sound\\power up.mp3')
    playsound.playsound('f:\\code\\sound\\jarvis Start up.wav')
    playsound.playsound('f:\\code\\sound\\jarvis.mp3') 
    battery = psutil.sensors_battery()
    percentage = battery.percent  
    if percentage>95 and percentage<97:
        speak('battery is been fullycharged ')

    if percentage<95 and percentage>30:
        speak('battery is in stable condition')

    if percentage<30 and percentage>5:
        playsound.playsound('f:\\code\\sound\\Jarvis Low Power Message Tone.mp3')
    wishMe()
    TaskEecution() 
        
#main program starts here...
startup()
