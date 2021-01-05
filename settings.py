from mod import *
with open('settings.json') as f:
    data = json.load(f)
def take_voice() :
    r = sr.Recognizer()
    with sr.Microphone()as source :
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)
        text = r.recognize_google(audio, language=data['language'])
def say(text):
	global date_string
	date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
	filename = "voice"+date_string+".mp3"
	tts = gTTS(text)
	tts.save(filename)
	playsound(filename)
	os.unlink(filename)
def sp(text):
    print(text)
    say(text)
def screenshot():
	date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
	screenshot = pyautogui.screenshot()
	screenshot.save(f'Screenshots/screenshot{date_string}.png')
