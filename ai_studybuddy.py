# -----------------------------------------------
# AI StudyBuddy - Rule-Based Chat Assistant
# Created by: Subarna Ghosh
# -----------------------------------------------

import datetime
import time

hour = datetime.datetime.now().hour
if 5 <= hour < 12:
    print("Good morning, Subarna!")
elif 12 <= hour < 17:
    print("Good afternoon, Subarna!")
elif 17 <= hour < 21:
    print("Good evening, Subarna!")
else:
    print("Good night, Subarna!")

print("\nHello! I am Subarna's AI StudyBuddy!")
print("You can talk to me. Type 'bye' anytime to exit.\n")

responses = {
    "hello": "Hi there! How can I help you with your studies today?",
    "who are you": "I am your friendly AI StudyBuddy created by Subarna Ghosh.",
    "how are you": "I am just Python code, but I feel great when you run me!",
    "motivate me": "Keep going! Every bug you fix makes you a better programmer.",
    "python": "Python is powerful — it is widely used in AI, data analytics, and automation!",
    "ai": "Artificial Intelligence is transforming the world, and prompt engineering is a key skill!",
    "sad": "Don't worry! Even code breaks sometimes, but it always runs again.",
    "happy": "That is great to hear! Keep that positive energy going.",
    "bye": "Goodbye! Keep learning and keep smiling."
}

def get_response(user_input):
    user_input = user_input.lower()
    if "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    for key in responses:
        if key in user_input:
            return responses[key]
    return "Hmm... I am not sure about that yet, but I will learn soon!"

while True:
    user = input("You: ")
    reply = get_response(user)
    time.sleep(0.5)
    print("StudyBuddy:", reply)

    if "bye" in user.lower():
        break
