def chatbot():
    responses = {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "hi": "Hello!",
        "hey": "Hey there!",
        "bye": "Goodbye!"
    }

    print("Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input in responses:
            print("Chatbot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()