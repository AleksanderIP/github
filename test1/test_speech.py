import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 1) as source:
    print("Говорите ...")
    audio = r.listen(source)
try:
    query = r.recognize_google(audio, language="ru-RU")
    print("Вы сказали: " + query.lower())
