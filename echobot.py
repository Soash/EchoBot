import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print('\n___EchoBot v1___\n')

    while True:
        text = input('input> ')
        if text.lower() == 'q':
            break 
        text_to_speech(text)




