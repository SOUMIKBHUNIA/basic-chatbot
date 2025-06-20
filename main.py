# Function to return responses based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Normalize input

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

# Main loop to interact with user
print("🤖 Chatbot: Hello! Type something (type 'exit' to quit)")

while True:
    user_input = input("🧑 You: ")

    if user_input.lower() == "exit":
        print("🤖 Chatbot: Chat ended. Goodbye!")
        break

    reply = chatbot_response(user_input)
    print("🤖 Chatbot:", reply)
