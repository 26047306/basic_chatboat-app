import random

def chatbot():
    # Predefined responses
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm just a bot, but I'm doing fine! How about you?", "I'm great! What about you?"],
        "what is your name": ["I'm Chatbot, your virtual assistant.", "You can call me Chatbot!"],
        "bye": ["Goodbye! Have a great day!", "Bye! Take care!"],
        "default": ["I'm not sure I understand. Could you rephrase?", "Sorry, I don't know how to respond to that."]
    }

    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Find a matching response or use the default response
        response = responses.get(user_input, responses["default"])
        print(f"Chatbot: {random.choice(response)}")

if __name__ == "__main__":
    chatbot()
