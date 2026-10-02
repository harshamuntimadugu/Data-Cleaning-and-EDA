import pyttsx3
assistant = pyttsx3.init()

assistant.say("Hello, I am your voice assistant")
assistant.runAndWait()

name = input("Enter your name: ")

assistant.say("Hello " + name)
assistant.runAndWait()

print("Assistant: Hello", name)
print("Assistant: I can say hello and goodbye.")

choice = input("Type hello or bye: ").lower()

if choice == "hello":
    assistant.say("Hello! How are you?")
    assistant.runAndWait()

elif choice == "bye":
    assistant.say("Goodbye! Have a nice day.")
    assistant.runAndWait()

else:
    assistant.say("Sorry, I don't understand.")
    assistant.runAndWait()