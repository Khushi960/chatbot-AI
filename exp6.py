import random

responses = {
    "hello": ["Hi!", "hi", "Hello!", "Hey there!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "your name": ["I am your chatbot.", "Call me ChatBot!"]
}

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break

        found = False
        for key in responses:
            if key in user:
                print("Chatbot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("Chatbot: Sorry, I don't understand.")

chatbot()