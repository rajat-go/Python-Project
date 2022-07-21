import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import ctypes
import requests
import pytz
import pyjokes


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak(" Good Morning Boss ")
        print(" Good Morning Boss ")
    elif hour>=12 and hour<18:
        speak(" Good Afternoon Boss ")
        print(" Good Afternoon Boss ")
    else:
        speak(" Good Evening Boss ")
        print(" Good Evening Boss ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
    
wishMe()

if __name__=='__main__':


    while True:
        speak("Boss how can I help you")
        statement = takeCommand().lower()

        if statement==0:
            continue

        elif "bye" in statement or "good bye" in statement or "ok bye" in statement or "stop" in statement or "goodbye" in statement or "okbye" in statement or "exit" in statement:
            speak('Good Bye boss')
            print('Good Bye boss')
            break

        
        elif 'open wikipedia' in statement or 'start wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.org/")
            speak("Wikipedia is opened")
            time.sleep(5)

        elif 'open music ' in statement or 'start music' in statement:
            webbrowser.open_new_tab("https://wynk.in/music")
            speak("Music website is opened")
            time.sleep(5)
            
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
            
        elif 'open wikipedia' in statement or 'start wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.org/")
            speak("Wikipedia is open now")
            time.sleep(5)
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'jokes' in statement:
            joke = pyjokes.get_joke(language="en", category="all")
            speak(joke)
            print(joke)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Which city")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'current time' in statement or 'current day' in statement or 'current date' in statement:
            speak("Which city")
            city_name=takeCommand()
            complete_url="https://24timezones.com/"+city_name+"/time"
            url=complete_url
            webbrowser.open_new_tab(url)
            time.sleep(5)
            
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,show time & day of any city,take a photo,search any word wikipedia, search anything on google,'
                  'predict weather of different cities ,get top headline news from Indian Express, open music website,listen some jokes and solve arithmetic question,'
                  'lock window and shutdown system!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement or "who built you" in statement:
            speak("I was built by RAJAT GOYAL")
            print("I was built by RAJAT GOYAL")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'latest news' in statement:
            news = webbrowser.open_new_tab("https://indianexpress.com/")
            speak('Here are some headlines from Indian Express ')
            time.sleep(6)

        elif "take photo" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'solve questions' in statement:
            speak('I can answer to alrithmetic questions')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "lock my window" in statement:
            speak("Ok, your window is getting locked")
            ctypes.windll.user32.LockWorkStation()
            
        elif "shutdown" in statement or "shut down" in statement:
            speak("Ok , your laptop will shutdown in some time")
            os.system("shutdown /s /t 1")

time.sleep(3)
