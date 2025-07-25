from speech_recognition import get_voice_command as gvc
from tts import speak
from command_parser import handleCommand as hc
from tasks import execute_command as ec
import time

if __name__ == "__main__":
    speak("Hello, I am JARVIS. How can I help you today?")

    while True:
        time.sleep(2)
        command = gvc()

        print(f"User said: {command}")

        if not command:
            continue

        response = hc(command)

        if response.lower() in ["", "i didn't understand that command", "sorry! i didn't catch that"] or "i don't recognize the app" in response.lower():
            response = ec(command)
        
        print(f"JARVIS: {response}")
        speak(response)

        if "exit" in command or "quit" in command:
            break