from datetime import datetime

def greet():
    return "Hello! How may I assist you?"

def get_time():
    return f"The Time is {datetime.now().strftime('%I:%M %p')}"

def get_date():
    return f"Today's date is {datetime.now().strftime('%d %B, %Y')}"

def exit_jarvis():
    return "Goodbye!"

def unknown():
    return "Sorry! I didn't catch that."

commands = {
    "hello" : greet,
    "hi" : greet, 
    "time" : get_time,
    "date" : get_date,
    "exit" : exit_jarvis,
    "quit" : exit_jarvis
}

def handleCommand(cmd: str) -> str:
    cmd = cmd.lower()

    for keyword, action in commands.items():
        if keyword in cmd:
            return action()
        
    return unknown()