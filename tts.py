import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

    delay = len(text.split()) * 0.25
    time.sleep(delay)