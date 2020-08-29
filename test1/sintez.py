# Настройки призношения текстов

import pyttsx3

text = 'Привет Александр Иванович! Рада Вас слышать!'
tts = pyttsx3.init()
rate = tts.getProperty('rate') #Скорость произношения
tts.setProperty('rate', rate-1)

volume = tts.getProperty('volume') #Громкость голоса
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

tts.say(text)
tts.runAndWait()
