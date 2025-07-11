import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level
    engine.say(text)
    engine.runAndWait()

def main():
    print("Text-to-Speech (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter text to speak:\n> ")
        
        if user_input.strip().lower() == 'exit':
            print("Exiting program.")
            break

        text_to_speech(user_input)

if __name__ == "__main__":
    main()
