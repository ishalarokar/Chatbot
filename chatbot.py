# basic_chatbot.py

import re

# Define simple patterns and responses
rules = {
    r'hi|hello|hey': "Hello! How can I help you today?",
    r'how are you': "I'm just a bunch of code, but I'm doing fine!",
    r'what is your name': "I'm a simple chatbot built with Python.",
    r'time|current time': None,  # handle dynamically
    r'bye|exit|quit': "Goodbye! Have a great day!"
}

def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            if response:
                return response
            if 'time' in pattern:
                from datetime import datetime
                return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    return "I'm sorry, I don't understand. Can you rephrase?"

def chat():
    print("Welcome! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        reply = get_response(user)
        print("Bot:", reply)
        if re.search(r'bye|exit|quit', user, re.IGNORECASE):
            break

if __name__ == "__main__":
    chat()
