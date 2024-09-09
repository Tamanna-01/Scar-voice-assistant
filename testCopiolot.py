# Import the modules
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyttsx3
import pyautogui

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen to the user's voice
def listen():
    # Use the microphone as the source
    with sr.Microphone() as source:
        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        # Listen for the user's input
        audio = r.listen(source)
        # Recognize the speech using Google API
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
            return text
        except:
            print("Sorry, I could not understand that.")
            return ""

# Define a function to handle the user's query
def handle_query(query):
    # Convert the query to lowercase
    query = query.lower()
    # Check if the query contains certain keywords
    if "hello" in query or "hi" in query:
        # Greet the user
        speak("Hello, I am your desktop assistant. How can I help you?")
    elif "time" in query:
        # Tell the current time
        now = datetime.datetime.now()
        speak("The current time is " + now.strftime("%H:%M"))
    elif "wikipedia" in query:
        # Search Wikipedia for the query
        query = query.replace("wikipedia", "")
        speak("Searching Wikipedia for " + query)
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + result)
    elif "google" in query:
        # Open Google in the browser
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    else:
        # Say that the query is not recognized
        speak("Sorry, I do not recognize that command. Please try again.")

# Create a main loop
while True:
    # Listen to the user's voice
    query = listen()
    # Handle the user's query
    handle_query(query)
