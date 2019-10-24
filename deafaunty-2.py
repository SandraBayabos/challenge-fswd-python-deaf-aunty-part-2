name = input("What is your name? ")
while True:
    speak = input("Speak to aunty:")
    # your reply, e.g. good day
    if speak.islower() == True:
        print(f"WHAT? SPEAK UP!")
    # your reply, e.g. WASSUP!
    if speak.isupper() == True:
        print(f"YOU ARE VERY RUDE!")
    # your reply, e.g. I love you aunty, I have to go now
    if speak.istitle() == True:
        print(f"SHOW SOME RESPECT!")
    if speak == "I love you aunty, I have to go now":
        print(f"ok. Goodbye")
        print(f"{name},are you there?")
        reply = input("Say something:")
        if reply == '':
            reply2 = input("Say something:")
            if reply2 == '':
                print(f"ok. Goodbye")
                break
    continue
