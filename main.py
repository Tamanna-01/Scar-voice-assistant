from selenium_web import *
from YT_auto import *
from news import *
from jokes import *
from weather import *
import pyttsx3 as p
import speech_recognition as sr
import randfacts
import datetime
import webbrowser

engine = p.init()   #used to initiate text to speech pyttsx3
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def wishes():
    h = int(datetime.datetime.now().hour)
    if h>0 and h<12:
        return "morning"
    elif h>=12 and h<16:
        return "afternoon"
    else:
        return "evening"

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(f"Hello, good {wishes()} I am your Voice Assistant, Scar. How can I help you?")

while True:

    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.energy_threshold = 10000
            r.adjust_for_ambient_noise(source, 1.2)
            print("Listening...")
            audio = r.listen(source)
        text = r.recognize_google(audio)
        print("You said:", text)

        if "quit" in text:
            print("Goodbye!")
            speak("Goodbye!")
            break

        elif "information" in text:
            speak("You need information related to which topic?")
            
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listening...")
                audio = r.listen(source)
                infor = r.recognize_google(audio)
                print("Topic:", infor)
                print(f"Opening {infor} in Wikipedia...")
                speak(f"Opening {infor} in Wikipedia...")

                assist = Infow()
                assist.get_info(infor)

        elif "search" in text:
            speak("What do you want to search?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listening...")
                audio = r.listen(source)
                query = r.recognize_google(audio)
                search_url = f"https://www.google.com/search?q={query}"
                webbrowser.open_new_tab(search_url)
                print(f"Searching {query}...")
                print(f"Here are the search results for {query}")
                speak(f"Here are the search results for {query}")

        elif "play" and "video" in text:
            speak("Which video do you want me to play?")

            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listening...")
                audio = r.listen(source)
                vid = r.recognize_google(audio)
                print("Topic:", vid)
                print(f"Playing {vid} on YouTube...")
                speak(f"Playing {vid} on YouTube...")

                assist = music()
                assist.play(vid)

        elif "news" in text:
            speak("Sure, here are some of the latest news...")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])

        elif "fact" in text or "facts" in text:
            x = randfacts.get_fact()
            print(x)
            speak(f"Did you know that? {x}")

        elif "joke" in text or "jokes" in text:
            speak("Sure, here comes a joke for you...")
            arr = joke()
            print(arr[0])
            speak(arr[0])
            print(arr[1])
            speak(arr[1])

        elif "weather" in text or "temperature" in text:
            speak("Sure, you want to know the weather of which place?")
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                r.adjust_for_ambient_noise(source, 1.2)
                print("Listening...")
                audio = r.listen(source)
                place = r.recognize_google(audio)
                print("Place:", place)
                t, d = get_weather(place)
                print(f"The weather of {place} is {d} with a temperature of {t}°.")
                speak(f"The weather of {place} is {d} with a temperature of {t} degrees.")

        elif "date" in text or "time" in text or "day" in text:
            d = datetime.datetime.now()
            print(f"Today is {d.strftime('%d')} of {d.strftime('%B')}, {d.strftime('%Y')}, and its currently {d.strftime('%I')}:{d.strftime('%M')} {d.strftime('%p')}")
            speak(f"Today is {d.strftime('%d')} of {d.strftime('%B')}, {d.strftime('%Y')}, and its currently {d.strftime('%I')} {d.strftime('%M')} {d.strftime('%p')}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))