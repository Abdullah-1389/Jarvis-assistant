# # jarvis_core.py

# import datetime
# import os

# def process_command(command):
#     command = command.lower()

#     if "time" in command:
#         now = datetime.datetime.now().strftime("%I:%M %p")
#         return f"The current time is {now}"
#     elif "open notepad" in command:
#         os.system("notepad")
#         return "Opening Notepad"
#     elif "hello" in command:
#         return "Hello! How can I assist you today?"
#     elif "exit" in command or "quit" in command:
#         return "Goodbye!"
#     else:
#         return "I didn't understand that command."


import datetime
import os

def process_command(command):
    command = command.lower()

    # Greetings
    if "hello" in command or "hi" in command:
        return "Hello! How can I assist you today?"
    elif "thanks" in command or "thank you" in command:
        return "Your Welcome!.I'm here to help you"
    elif "your name" in command:
        return "I am Jarvis, your virtual assistant."
    # introduction
    elif "introduce myself" in command:
        return "I'm Abdullah Attique I'm currently studying BS Software Engineering at the University of Lahore I love developing web applications with Flask, exploring e-commerce, and building real-world projects I also play badminton competitively and enjoy mentoring others."
    # apps
    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    elif "open google chrome" in command or "chrome" in command:
        os.system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"')
        return "Opening Chrome"
    elif "open whatsapp" in command:
        os.system(r'start whatsapp:')
        return "Opening WhatsApp"
    elif "open vs code" in command or "open visual studio code" in command:
        os.system("code")
        return "Opening Visual Studio Code"

    elif "bye" in command:
        return "Goodbye! Have a great day!"

    # Date & Time
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    elif "date" in command:
        today = datetime.datetime.today().strftime("%A, %B %d, %Y")
        return f"Today's date is {today}."


    else:
        return "I'm not sure how to respond to that yet."
