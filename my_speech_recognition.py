import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User said: {text}")
        return text.lower()
    
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None