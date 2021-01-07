from settings import *
while True:
    text = take_voice()
    speak = ''
    if call(text):
        hi = say_hello(text)
        speak = hi
        if "date" in text or "day" in text or "month" in text:
            get_today = say_hello(text)
            speak = speak + " " + get_today
        say(speak)