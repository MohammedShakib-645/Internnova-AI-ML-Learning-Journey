print("AI Chatbot: Hello! I am your AI assistant.")
print("Type 'bye' to exit.")
while True:
    user = input("You: ").lower()
    if user == "hello" or user == "hi":
        print("Bot: Hello! Welcome.")
    elif user == "how are you":
        print("Bot: I'm fine. How are you?")
    elif user.startswith("my name is"):
        name = user.replace("my name is", "").strip()
        print("Bot: Nice to meet you, " + name.title() + "!")
    elif user == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")
    elif user == "what can you do":
        print("Bot: I can respond to simple messages using predefined rules.")
    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
