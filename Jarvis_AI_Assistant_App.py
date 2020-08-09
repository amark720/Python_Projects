
'''
GoTo Command Prompt and install pyttsx3 package using command 'pip install pyttsx3'
and install SpeechRecognition package using command 'pip install SpeechRecognition'.
and install wikipedia package using command 'pip install wikipedia.
After that run the below code and Speak something then the Assistant will repeat whatever you said!
'''

import speech_recognition as sr
import datetime
import time as tt
import pyttsx3, wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("Welcome Back!")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"The time is  {Time}")



def wiki():
    try:
        query = "sadsdasd"
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except:
        print("No results Found or Network Connection Error!")



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language= 'en-in')
        tt.sleep(2)
        print((f"You Said:{query}\n"))
        speak((f"You Said:{query}\n"))

    except Exception as e:
        print(e)
        print("Say That Again....")
        speak("Say That Again....")
        return "None"
    return query

takecommand()  # use this function and speak something which Asistant will repeat
#wiki()  # Use this function if you want to search something on wikipedia using Assistant
#time()  #use this function if you want assistant to speak the current time


### End of Code ###

