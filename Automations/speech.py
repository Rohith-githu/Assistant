import speech_recognition as sr
from settings import *
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