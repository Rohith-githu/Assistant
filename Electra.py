from practically import *
from settings import *
while True:
    text = take_voice().lower()
    speak = ''
    if call(text):
        speak = ''
        if "date" in text or "day" in text or "month" in text:
            get_today = say_hello(text)
            speak = speak + " " + get_today
        elif 'time' in text:
            speak = speak + 'the time is :' + datetime.datetime.now().strftime('%H:%M')
        elif 'note' in text:
            text = text.replace("create a note", '')
            note(text)
        elif 'calculate' in text:
            app_id = data['wapp_id']
            client = wolframalpha.Client(app_id)
            ind = text.lower().split().index("calculate")
            text = text.split()[ind + 1:]
            res = client.query(" ".join(text))
            answer = next(res.results).text
            speak = speak + "The answer is " + answer
        elif 'who is' in text or 'what is' in text:
            app_id = data['wapp_id']
            client = wolframalpha.Client(app_id)
            ind = text.lower().split().index("is")
            text = text.split()[ind + 1:]
            res = client.query(" ".join(text))
            answer = next(res.results).text
            speak = speak + answer
        elif 'dont listen' in text or 'stop listening' in text:
            say("how much time should i sleep")
            text = take_voice().lower()
            time.sleep(int(text))
            say('i am back you can ask questions')
        elif 'say a joke' in text or 'a joke' in text:
            speak = speak + pyjokes.get_joke()
        elif 'where is' in text or 'locate' in text:
            ind = text.split().index("is")
            maps(ind)
            speak = speak + 'this is the location of {ind}'
        elif 'weather' in text:
            key = "c1a1d7cd5a5a31f4b2bb46132c56b06b"
            weather_url = "http://api.openweathermap.org/data/2.5/weather?"
            ind = text.split().index("in")
            location = text.split()[ind + 1:]
            location = "".join(location)
            url = weather_url + "appid=" + key + "&q=" + 'hyderabad'
            js = requests.get(url).json()
            if js["cod"] != "404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature - 273.15
                humidity = weather["humidity"]
                desc = js["weather"][0]["description"]
                weather_response = " The temperature in Celcius is " + str(temperature) + " The humidityis " + str(
                    humidity) + " and The weather description is " + str(desc)
                speak = speak + weather_response
            else:
                speak = speak + "City Not Found"
        elif 'google' in text :
            ind = text.lower().split().index("google")
            search = text.split()[ind + 1:]
            webbrowser.open("https://www.google.com/search?q=" + "+".join(search))
            speak = speak + "Searching " + str(search) + " on google"
        elif 'search' in text:
            ind = text.lower().split().index("search")
            search = text.split()[ind + 1:]
            webbrowser.open("https://www.google.com/search?q=" + search)
            speak = speak + "Searching " + str(search) + " on google"  
        elif 'youtube' in text :
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open("http://www.youtube.com/results?search_query=" +"+".join(search))
            speak = speak + "Opening " + str(search) + " on youtube"
        elif 'practically' in text:
            practically()
        elif 'open chrome' in text:
            webbrowser.open('chrome.exe')
        elif 'open edge' in text:
            webbrowser.open('msedge.exe')
        
        try :
            say(speak)
        except AssertionError as e :
            say("I dont know that")