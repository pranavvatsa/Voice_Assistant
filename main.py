import os
import requests
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

def telltime():
	strtime=datetime.datetime.now().strftime("% H:% M:% S")
	speak(f"The current time is {strtime}")

def tellday():
	strday=datetime.datetime.now()
	speak(strday.strftime("%A"))




def takeCommand():
	r = sr.Recognizer()

	# from the speech_Recognition module we will use the microphone module for listening the command
	with sr.Microphone() as source:
		print('Listening...')

		# seconds of non-speaking audio before a phrase is considered complete
		r.pause_threshold = 0.5
		audio = r.listen(source)

		# Now we will be using the try and catch method so that if sound is recognized it is good else we will have exception handling
		try:
			print("Recognizing...")

			# for Listening the command in indian english we can also use 'hi-In' for hindi
			Query = r.recognize_google(audio, language='en-in')
			print("the command is=", Query)

		except Exception as e:
			print(e)
			print("Say that again...")
			return "None"

		return Query


def speak(audio):
	engine = pyttsx3.init()
	# getter method(gets the current value of engine property
	voices = engine.getProperty('voices')

	# setter method .[0]=male voice and [1]=femal voice in set property
	engine.setProperty('voice', voices[0].id)

	# Method for the speaking of the assistant
	engine.say(audio)

	# Blocks while processing all the currently queued commands
	engine.runAndWait()


def Take_query():
	# This loop is infinite as it will take our queries continuously until and unless we do not say bye to terminate
	while (True):

		query = takeCommand().lower()

		if "day" or "the day" in query:
			speak("ITS SUNDAY")
			continue

		elif "the time" or "time" in query:
			telltime()
			continue

		elif "bye" in query:
			speak("Bye")
			exit()

		elif "tell me your name" in query:
			speak("I am Jarvis. Your desktop Assistant")

		elif "open spotify" in query:
			speak("Opening spotify...")
			os.system("Spotify")





if __name__ == '__main__':
	Take_query()