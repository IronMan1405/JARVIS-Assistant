import webbrowser, os, datetime, random

def execute_command(command):
    command = command.lower()

    if 'search for' in command:
        query = command.split("search for")[-1].strip()
        url = f"https://www.google.com/search?={query}"
        webbrowser.open(url)
        return f"Searching google for {query}"

    else:
        return f"I don't understand that yet."