# запись с микрофона

import speech_recognition as sr


def comm():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language="ru-Ru").lower()
            print("вы сказали " + command)
        except sr.UnknownValueError:
            print("я вас не поняла")
            command = comm()
        return command


comm()
