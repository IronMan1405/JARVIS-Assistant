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

def open_app(appname: str):
    try:
        os.system(f"open -a '{appname}'")
        return f"Opening {appname}"
    except Exception:
        return f"Could not open {appname}"

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

app_aliases = {
    "chrome" : "Google Chrome",
    "safari": "Safari",
    "code": "Visual Studio Code",
    "spotify": "Spotify",
    "notes": "Notes",
    "calendar": "Calendar",
    "terminal": "Terminal",
    "photos": "Photos",
    "messages": "Messages",
}

def handleCommand(cmd: str) -> str:
    cmd = cmd.lower()

    for keyword, action in commands.items():
        if keyword in cmd:
            return action()

    if cmd.startswith("open "):
        app_key = cmd.replace("open ", "").strip()
        app_name = app_aliases.get(app_key)

        if app_name:
            return open_app(app_name)
        else:
            return f"I don't recognize the app {app_key}"
        
    return unknown()