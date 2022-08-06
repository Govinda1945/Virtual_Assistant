import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print("listning")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        print("error")

    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time =datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+ time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk("sorry, I have a headache")
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
    elif 'i love you' in command:
        talk("Thank you, i am also love to spend time with you")
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk("hey i didn't heard properly come again?")


while True:
    run_alexa()
