import sys
import webbrowser
import pyttsx3
import speech_recognition as sr


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("привет, я твой личный помощник")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        talk('что открыть?')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        mission = r.recognize_google(audio, language="ru-RU").lower()
        print('вы сказали ' + mission)
    except sr.UnknownValueError:
        talk('не распознано')
        mission = command()
    return mission


def makemission(mission):
    if 'привет' in mission:
        talk('выполняю')
        url = 'http://pypi.org/'
        webbrowser.open(url)
    elif 'стоп' in mission:
        talk('всего доброго')
        sys.exit()


while True:
    makemission(command())
