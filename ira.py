# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 13:45:58 2022

@author: Huru
"""

import pyttsx3 as py3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import pyjokes as pyj
import datetime
import pyaudio
import time
import re
import time
import wordtodigits
from word2number import w2n
import requests, json

r = sr.Recognizer()

engine = py3.init()


def nowTime():
    ctime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour > 1 and hour < 12:
        speak("It's {} A M".format(ctime))
    elif hour >= 12 and hour <= 24:
        speak("It's {} P M".format(ctime))


def todayDate():
    ctime = datetime.datetime.today().strftime("%d %B %Y")
    speak(ctime)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good Morning Sir !")
        print("Good Morning Sir !")
        engine.runAndWait()
    elif hour >= 12 and hour < 18:
        engine.say("Good Afternoon Sir !")
        print("Good Afternoon Sir !")
        engine.runAndWait()
    else:
        engine.say("Good Evening Sir !")
        print("Good Evening Sir !")
        engine.runAndWait()

    assname = ("IRA 1 point o")
    engine.say("I am your Assistant")
    print("I am your Assistant")
    engine.runAndWait()
    engine.say(assname)
    print(assname.replace("point", "."))
    engine.runAndWait()
def speech():



    # wishMe()

    while True:

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)

                speak("Say something!")

                audio = r.listen(source)

            engine.say("Listening...")
            print("Listening...")
            engine.say("Done!")
            print("Done!")
            engine.runAndWait()
            print("You said: " + r.recognize_google(audio))

            a = r.recognize_google(audio)
            b = str(a).lower()

            if "hello" in a:
                engine.say("Hello, How Can I Help You?")

                print("Hello, How Can I Help You?")

                engine.runAndWait()


            elif "how are you" in a:
                engine.say("Hmm, I am Fine")

                print("Hmm, I am Fine")

                engine.runAndWait()


            elif "google" in a:
                engine.say("Searching Google...")
                engine.runAndWait()

                a = str(a).replace("google", "")
                results = wikipedia.summary(a, sentences=3)

                engine.say("According to Google")
                print(results)

                engine.say(results)
                engine.runAndWait()


            elif "Google" in a:
                engine.say("Searching Google...")
                engine.runAndWait()

                a = str(a).replace("Google", "")
                results = wikipedia.summary(a, sentences=3)

                engine.say("According to Google")
                print(results)

                engine.say(results)
                engine.runAndWait()

            elif ("youtube" in str(a).lower()) and ('search' in str(a).lower()):
                engine.say("Searching in Youtube ...")
                engine.runAndWait()

                a = str(a).replace("YouTube", "")
                a = str(a).replace("search", "")
                a = str(a).replace("in", "")
                a = str(a).replace("on", "")
                a = str(a).replace("at", "")
                a = str.strip(a)

                engine.runAndWait()
                wb.open(f"https://www.youtube.com/results?search_query={a}")

            elif "open" in str(a).lower():
                engine.say("Opening ...")

                a = str(a).replace("open", "")
                a = str.strip(a)
                print("Opening...")

                engine.runAndWait()
                wb.open(f"https://{a}.com")
            elif "suggest" in str(a).lower():
                engine.say("Suggesting ...")

                a = str(a).replace("suggest", "")
                a = str.strip(a)
                print("Suggesting...")
                print(a)

                engine.runAndWait()
            elif 'weather today' in str(a).lower() or "today's weather" in str(a).lower():
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                CITY = "Baku"
                API_KEY = "32dd8c804845157a5dbc92e9ab9fea72"
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    temperature = main['temp']
                    C = temperature - 273
                    humidity = main['humidity']
                    pressure = main['pressure']
                    report = data['weather']
                    print(f"{CITY:-^30}")
                    temp = f"Temperature is {C:.2f}".format(C)
                    print(f"Temperature: {C:.2f}")
                    print(f"Humidity: {humidity:.2f}".format(humidity))
                    print(f"Pressure: {pressure}")
                    print(f"Weather Report: {report[0]['description']}")
                    engine.say(temp)
                else:
                    # showing the error message
                    print("Error in the HTTP request")
            elif "what time" in a:
                nowTime()
            elif ('today' in a) and ('date' in a):
                todayDate()

            elif 'countdown' in a:
                def countdown(t):
                    while t:
                        mins, secs = divmod(t, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        engine.say(t)

                        t -= 1

                    engine.say('Fire in the hole!!')


                number_extract_pattern = "\\d+"
                try:
                    b = re.findall(number_extract_pattern, a)
                    b = list(map(int, b))[0]
                    countdown(b)
                except:

                    c = str(a).replace("countdown", "")
                    c = w2n.word_to_num(f'{c}')
                    countdown(c)





            elif "sleep ira" in str(a).lower():
                engine.say("As you wish!")
                print("As you wish!")

                engine.runAndWait()
                exit()


            elif "wish me" in str(a).lower():
                wishMe()

            elif "joke" in str(a).lower():
                engine.say(pyj.get_joke())
                engine.runAndWait()
                print(pyj.get_joke())


            elif "what can you do" in b:
                speak(
                    "I can Tell you a joke, Open YouTube, Google Something, Wish You,Give a today's weather prognosis, set a coundown")
                speak("I can Tell you the time, chat with you, and much more.")

            elif "send email" in b:
                speak("Sorry!, I can't do that!")

            elif "can you chat with me" in b:
                speak("Yeah!, Sure, But Speak in english only")

            elif "bored" in b and "I" in b:
                speak("U Can listen music or Chat with me")

            else:
                engine.say("It's hard to understand")

                print("It's hard to understand")

                engine.runAndWait()



        except Exception as e:
            b = "Could not understand audio,try type"

            engine.say(b)

            print(b)
            engine.runAndWait()
            a = input()
            a = a.lower()
            b = a.lower()

            print("You said: " + a)

            if "hello" in a:
                engine.say("Hello, How Can I Help You?")

                print("Hello, How Can I Help You?")

                engine.runAndWait()


            elif "how are you" in a:
                engine.say("Hmm, I am Fine")

                print("Hmm, I am Fine")

                engine.runAndWait()


            elif "google" in a:
                engine.say("Searching Google...")
                engine.runAndWait()

                a = str(a).replace("google", "")
                results = wikipedia.summary(a, sentences=3)

                engine.say("According to Google")
                print(results)

                engine.say(results)
                engine.runAndWait()




            elif ("youtube" in str(a).lower()) and ('search' in str(a).lower()):
                engine.say("Searching in Youtube ...")
                engine.runAndWait()

                a = str(a).replace("YouTube", "")
                a = str(a).replace("search", "")
                a = str(a).replace("in", "")
                a = str(a).replace("on", "")
                a = str(a).replace("at", "")
                a = str.strip(a)

                engine.runAndWait()
                wb.open(f"https://www.youtube.com/results?search_query={a}")

            elif "open" in str(a).lower():
                engine.say("Opening ...")

                a = str(a).replace("open", "")
                a = str.strip(a)
                print("Opening...")

                engine.runAndWait()
                wb.open(f"https://{a}.com")
            elif "suggest" in str(a).lower():
                engine.say("Suggesting ...")

                a = str(a).replace("suggest", "")
                a = str.strip(a)
                print("Suggesting...")
                print(a)

                engine.runAndWait()
            elif 'weather today' in str(a).lower() or "today's weather" in str(a).lower():
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                CITY = "Baku"
                API_KEY = "32dd8c804845157a5dbc92e9ab9fea72"
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    temperature = main['temp']
                    C = temperature - 273
                    humidity = main['humidity']
                    pressure = main['pressure']
                    report = data['weather']
                    print(f"{CITY:-^30}")
                    temp = f"Temperature is {C:.2f}".format(C)
                    print(f"Temperature: {C:.2f}")
                    print(f"Humidity: {humidity:.2f}".format(humidity))
                    print(f"Pressure: {pressure}")
                    print(f"Weather Report: {report[0]['description']}")
                    engine.say(temp)
                else:
                    # showing the error message
                    print("Error in the HTTP request")
            elif "what time" in a:
                nowTime()
            elif ('today' in a) and ('date' in a):
                todayDate()

            elif 'countdown' in a:
                def countdown(t):
                    while t:
                        mins, secs = divmod(t, 60)
                        timer = '{:02d}:{:02d}'.format(mins, secs)
                        engine.say(t)

                        t -= 1

                    engine.say('Fire in the hole!!')


                number_extract_pattern = "\\d+"
                try:
                    b = re.findall(number_extract_pattern, a)
                    b = list(map(int, b))[0]
                    countdown(b)
                except:

                    c = str(a).replace("countdown", "")
                    c = w2n.word_to_num(f'{c}')
                    countdown(c)





            elif "sleep ira" in str(a).lower():
                engine.say("As you wish!")
                print("As you wish!")

                engine.runAndWait()
                exit()


            elif "wish me" in str(a).lower():
                wishMe()

            elif "joke" in str(a).lower():
                engine.say(pyj.get_joke())
                engine.runAndWait()
                print(pyj.get_joke())


            elif "what can you do" in b:
                speak(
                    "I can Tell you a joke, Open YouTube, Google Something, Wish You,Give a today's weather prognosis, set a coundown")
                speak("I can Tell you the time, chat with you, and much more.")

            elif "send email" in b:
                speak("Sorry!, I can't do that!")

            elif "can you chat with me" in b:
                speak("Yeah!, Sure, But Speak in english only")

            elif "bored" in b and "I" in b:
                speak("U Can listen music or Chat with me")

            else:
                engine.say("It's hard to understand")

                print("It's hard to understand")

                engine.runAndWait()
def text():


    while True:
        a=input()
        a = a.lower()
        b = a.lower()

        print("You said: " + a)
        if "hello" in a:
            engine.say("Hello, How Can I Help You?")

            print("Hello, How Can I Help You?")

            engine.runAndWait()


        elif "how are you" in a:
            engine.say("Hmm, I am Fine")

            print("Hmm, I am Fine")

            engine.runAndWait()


        elif "google" in a:
            engine.say("Searching Google...")
            engine.runAndWait()

            a = str(a).replace("google", "")
            results = wikipedia.summary(a, sentences=3)

            engine.say("According to Google")
            print(results)

            engine.say(results)
            engine.runAndWait()




        elif ("youtube" in str(a).lower()) and ('search' in str(a).lower()):
            engine.say("Searching in Youtube ...")
            engine.runAndWait()

            a = str(a).replace("YouTube", "")
            a = str(a).replace("search", "")
            a = str(a).replace("in", "")
            a = str(a).replace("on", "")
            a = str(a).replace("at", "")
            a = str.strip(a)

            engine.runAndWait()
            wb.open(f"https://www.youtube.com/results?search_query={a}")

        elif "open" in str(a).lower():
            engine.say("Opening ...")

            a = str(a).replace("open", "")
            a = str.strip(a)
            print("Opening...")

            engine.runAndWait()
            wb.open(f"https://{a}.com")
        elif "suggest" in str(a).lower():
            engine.say("Suggesting ...")

            a = str(a).replace("suggest", "")
            a = str.strip(a)
            print("Suggesting...")
            print(a)

            engine.runAndWait()
        elif 'weather today' in str(a).lower() or "today's weather" in str(a).lower():
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
            CITY = "Baku"
            API_KEY = "32dd8c804845157a5dbc92e9ab9fea72"
            URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()
                main = data['main']
                temperature = main['temp']
                C = temperature - 273
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                print(f"{CITY:-^30}")
                temp = f"Temperature is {C:.2f}".format(C)
                print(f"Temperature: {C:.2f}")
                print(f"Humidity: {humidity:.2f}".format(humidity))
                print(f"Pressure: {pressure}")
                print(f"Weather Report: {report[0]['description']}")
                engine.say(temp)
            else:
                # showing the error message
                print("Error in the HTTP request")
        elif "what time" in a:
            nowTime()
        elif ('today' in a) and ('date' in a):
            todayDate()

        elif 'countdown' in a:
            def countdown(t):
                while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    engine.say(t)

                    t -= 1

                engine.say('Fire in the hole!!')

            number_extract_pattern = "\\d+"
            try:
                b = re.findall(number_extract_pattern, a)
                b = list(map(int, b))[0]
                countdown(b)
            except:

                c = str(a).replace("countdown", "")
                c = w2n.word_to_num(f'{c}')
                countdown(c)





        elif "sleep ira" in str(a).lower():
            engine.say("As you wish!")
            print("As you wish!")

            engine.runAndWait()
            exit()


        elif "wish me" in str(a).lower():
            wishMe()

        elif "joke" in str(a).lower():
            engine.say(pyj.get_joke())
            engine.runAndWait()
            print(pyj.get_joke())


        elif "what can you do" in b:
            speak(
                "I can Tell you a joke, Open YouTube, Google Something, Wish You,Give a today's weather prognosis, set a coundown")
            speak("I can Tell you the time, chat with you, and much more.")

        elif "send email" in b:
            speak("Sorry!, I can't do that!")

        elif "can you chat with me" in b:
            speak("Yeah!, Sure, But Speak in english only")

        elif "bored" in b and "I" in b:
            speak("U Can listen music or Chat with me")

        else:
            engine.say("It's hard to understand")

            print("It's hard to understand")

            engine.runAndWait()

text()