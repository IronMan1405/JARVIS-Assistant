import os, random, webbrowser
from datetime import datetime

def greet():
    return "Hello! How may I assist you?"

def get_time():
    return f"The Time is {datetime.now().strftime('%I:%M %p')}"

def get_date():
    return f"Today's date is {datetime.now().strftime('%d %B, %Y')}"

def exit_jarvis():
    return "Goodbye!"

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening Youtube"

def open_google():
    webbrowser.open("https://www.google.com")
    return "Opening Google"

def open_code():
    os.system("open -a 'Visual Studio Code'")
    return "Opening VS Code"

def unknown():
    return "Sorry! I didn't catch that."

commands = {
    "hello" : greet,
    "hi" : greet, 
    "time" : get_time,
    "date" : get_date,
    "exit" : exit_jarvis,
    "quit" : exit_jarvis, 
    "youtube": open_youtube,
    "google": open_google,
    "code": open_code,
}

def handleCommand(cmd: str) -> str:
    cmd = cmd.lower()

    for keyword, action in commands.items():
        if keyword in cmd:
            return action()
        
    return unknown()