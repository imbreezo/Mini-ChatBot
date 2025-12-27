def mini_chatbot():
    print("Hi! I'm Mini. Let's chat. Type 'bye' to exit.")

    while True:
        msg = input("You: ").lower()

        if msg == "bye":
            print("Mini: See you later!")
            break
        elif "how are you" in msg:
            print("Mini: I'm just code, but I feel awesome!")
        elif "name" in msg:
            print("Mini: I'm Mini, Your friendly buddy who was coded by Paritosh on a saturday Evening !!!")
        elif "joke" in msg:
            print("Mini: Why do programmers prefer dark mode? Because light attracts bugs! LoL")
        elif "weather" in msg:
            print("Mini: I can't check the real weather yet, but I hope it's not super hot!")
        else:
            print("Mini: Interesting!")

mini_chatbot()
