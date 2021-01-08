from practically import *
from settings import *
while True:
    text = take_voice().lower()
    speak = ''
    if 'electra' in text or 'alexa' in text or 'electronic' in text or 'ultron' in text or 'computer' in text or 'okay' in text or 'hey' in text or 'hi' in text or 'elektra'in text or 'siri' in text or 'shri' in text:

        greet = ['how can i help you','what can i do for you','go ahead','i am here','online ask anything']
        say(random.choice(greet))
        text = take_voice().lower()
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
            try:
                time.sleep(int(text))
            except :
                speak = speak + 'Error! occoured while executing program '
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
            url = weather_url + "appid=" + key + "&q=" + location
            js = requests.get(url).json()
            if js["cod"] != "404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature - 273.15
                humidity = weather["humidity"]
                desc = js["weather"][0]["description"]
                weather_response = " The temperature in Celcius is " + str(temperature[0:4]) + " The humidityis " + str(
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
        elif 'wikipedia' in text:
            text = text.replace('wikipedia', '')
            results = wikipedia.summary(text, sentences=5)
            speak = speak + 'According to wikipedia article :' + results
        elif "note" in text or "remember this" in text:
            say("What would you like me to write down?")
            note_text = take_voice()
            note(note_text)
            speak = speak + "I have made a note of that."
        elif 'screenshot' in text:
            screenshot()
            speak = speak + 'Screenshot captured and copied to clipboard.'
        elif 'mute' in text:
            pyautogui.hotkey('alt','a') #unmutes mic for zoom
            pyautogui.hotkey('ctrl','d')    #unmutes mic for google meet
        elif 'video' in text :
            pyautogui.hotkey('ctrl','e')
            pyautogui.hotkey('alt','v')
        elif 'switch window' in text or 'which window' in text:
            pyautogui.hotkey('alt','tab')
        elif 'which tab' in text :
            pyautogui.hotkey('ctrl','tab')
        elif 'close window' in text :
            pyautogui.hotkey('alt','f4')
        elif 'who are you' in text :
            speak = speak + """Hello, I am your personal Assistant Electra. Your Assistant. I am here to make your life easier.  
                You can command me to perform various tasks such as solving mathematical questions or opening 
                applications etcetera."""
        elif 'how are you' in text :
            speak = speak + 'I am fine'
        elif 'where are you' in text or 'where do you' in text:
            speak = speak + 'I am you computer, i stay in your hardisk and in github repository'
        elif 'the time' in text :
            speak = speak + f'The time is {time_string}'
        elif 'desktop' in text :
            pyautogui.hotkey('win','d')
        elif 'whatsapp' in text :
            pyautogui.hotkey('win','5')
        elif 'timeline' in text:
            pyautogui.hotkey('win','tab')
        elif 'explorer' in text :
            pyautogui.hotkey('win','e')
        elif 'open' in text :
            speak = speak + 'opened'
            if 'chrome' in text :
                webbrowser.open('chrome.exe')
            elif 'edge' in text:
                webbrowser.open('msedge.exe')
            elif 'code' in text:
                os.system('code')
            elif 'cortana' in text :
                pyautogui.hotkey('win','c')
            elif 'zoom' in text:
                os.startfile(r"C:\Users\rohit\AppData\Roaming\Zoom\bin\Zoom.exe")
            elif 'notepad' in text :
                os.startfile(r"C:\WINDOWS\system32\notepad.exe")
            elif 'youtube' in text :
                webbrowser.open('http://www.youtube.com')
            elif 'whatsapp' in text :
                webbrowser.open('http://web.whatsapp.com')
            else :
                speak = speak + 'Can\'t find the app or couldn\'t open'
        elif 'youtube' in text :
            topic = text.split().index('youtube')
            search = text.split()[topic + 1:]
            url = 'https://www.youtube.com/results?q=' + search
            cont = requests.get(url)
            count = 0
            data = cont.content
            data = str(data)
            lst = data.split('"')
            for i in lst:
                count+=1
                if i == 'WEB_PAGE_TYPE_WATCH':
                    break
            if lst[count-5] == "/results":
                raise Exception("No video found.")
        
            webbrowser.open("https://www.youtube.com"+lst[count-5])
        elif 'password' in text:
            password_manager()
            speak = speak + ' generated a password and stored to database'
        elif 'my passwords' in text:
            passwords()
            speak = speak + 'These are your passwords'
        try :
            say(speak)
        except AssertionError as e :
            dont = ['I Don\'t Know that',
                    'I can\'t do that',
                    'That ,aybe beyond my abilities',
                    'Ask Anything else' ]
            say(random.choice(dont))

say('process terminated')