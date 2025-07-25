from my_speech_recognition import recognize_speech
from tts import speak
from command_parser import handleCommand
from tasks import execute_command

def main():
    while True:
        text = recognize_speech()

        if not text:
            continue

        handled = handleCommand(text)

        if handled:
            speak(handled)
        else:
            result = execute_command(text)
            speak(result)

if __name__ == "__main__":
    speak("Hello, I am JARVIS. How can I help you today?")

    main()