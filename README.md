# Electra2.0


Hi I am Electra an open source Virtual assistant Can be used by anyone who wants to.
Created By Rohtih Anumalasetty
Age : 15

<h1>About</h1>
Hello, I am your personal Assistant Electra. Your Assistant. I am here to make your life easier.You can command me to perform various tasks such as solving mathematical questions or opening applications etcetera. And Generates passwords to clipboard

<h1>Setup :</h1>
<b>First :</b>
    Install the requirements
    <code>pip install -r requirements.txt</code>
    After installing all the packages, you are ready to go!

open the Electra file and ask the what ever you need in below commands

<b>Wake Words :</b>
    <ul>
        <li>alexa</li>
        <li>electronic</li>
        <li>electra</li>
        <li>elektra</li>
        <li>hi</li>
        <li>hey</li>
        <li>ultron</li>
        <li>computer</li>
    </ul>

Say anything of the wake words to activate the assistant.


date string
<code>date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")</code>

time string
<code>time_string = datetime.datetime.now().strftime("%H:%M")</code>

take_voice() command to take the microphone input

<code>def take_voice() :
	r = sr.Recognizer()
	with sr.Microphone() as source :
		r.energy_threshold = data['energy_threshold']
		print('Listening...')
		audio = r.listen(source)
		r.pause_threshold = data['pause_threshold']
		try :
			print('recognizing...')
			query = r.recognize_google(audio, language=data['language'])
			print(f'You : {query}')
		except Exception as e:
			print('pls say that again')
			return 'None'
		return query</code>


say(query) functio to convert text-to=speech

<code>
    print(f'{query}')
    tts = gTTS(query)
    tts.save(f'voice{date_string}.mp3')
    playsound(f'voice{date_string}.mp3')
    os.unlink(f'voice{date_string}.mp3')</code>

all the settings page commands


    from mod import *
    with open('settings.json') as f:
        data = json.load(f)
    date_string = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    time_string = datetime.datetime.now().strftime("%H:%M")
    def take_voice() :
    	r = sr.Recognizer()
    	with sr.Microphone() as source :
    		r.energy_threshold = data['energy_threshold']
    		print('Listening...')
    		audio = r.listen(source)
    		r.pause_threshold = data['pause_threshold']
    		try :
    			print('recognizing...')
    			query = r.recognize_google(audio, language=data['language'])
    			print(f'You : {query}')
    		except Exception as e:
    			print('pls say that again')
    			return 'None'
    		return query

    def say(query):
        print(f'{query}')
        tts = gTTS(query)
        tts.save(f'voice{date_string}.mp3')
        playsound(f'voice{date_string}.mp3')
        os.unlink(f'voice{date_string}.mp3')

    def screenshot():
    	screenshot = pyautogui.screenshot()
    	screenshot.save(f'Screenshots/screenshot{date_string}.png')

    def google(query):
        webbrowser.open(f'https://www.google.com/search?q={query}')



    def password():
        set1 = string.ascii_uppercase
        set2 = string.ascii_lowercase
        set3 = string.digits
        set4 = string.punctuation
        passlen = 8
        passset = []
        passset.extend(set1)
        passset.extend(set2)
        passset.extend(set3)
        passset.extend(set4)
        random.shuffle(passset)
        pyperclip.copy(''.join(passset[0:passlen]))

    def wiki(query) :
    	query = query.replace('wikipedia')
    	say(wikipedia.summary(query))

    def maps(place) :
    	say(f'searching directions for {place}')
    	webbrowser.open(f'https://www.google.co.in/maps/place/{place}')
    	say(f'heres the {place}')

    def today_date():
    	now = datetime.datetime.now()
    	date_now = datetime.datetime.today()
    	week_now = calendar.day_name[date_now.weekday()]
    	month_now = now.month
    	day_now = now.day

    	months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
    	]

    	ordinals = [
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
            "9th",
            "10th",
            "11th",
            "12th",
            "13th",
            "14th",
            "15th",
            "16th",
            "17th",
            "18th",
            "19th",
            "20th",
            "21st",
            "22nd",
            "23rd",
            "24th",
            "25th",
            "26th",
            "27th",
            "28th",
            "29th",
            "30th",
            "31st",
    	]

    	say("Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + ".")

    def say_hello(text):
        greet = ['Hi sir!', 'What are you doing?','are you bored','What can i do for you?','yaa i am here']
        return say(random.choice(greet))

    def note(text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])
</code>

check the electra page and know about each command.
