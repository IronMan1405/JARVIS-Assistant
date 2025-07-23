from speech_recognition import get_voice_command as gvc
from tts import speak
from command_parser import handleCommand as hc

if __name__ == "__main__":
    speak("Hello, I am JARVIS. How can I help you today?")

    while True:
        command = gvc()

        print(f"User said: {command}")

        response = hc(command)
        print(f"JARVIS: {response}")
        speak(response)

        if "exit" in command or "quit" in command:
            break