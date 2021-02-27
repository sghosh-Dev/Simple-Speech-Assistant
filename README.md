# Simple-Speech-Assistant

Python speech assistant using the speech_recognition and Pyaudio (recognize_google) libraries. In order to accomplish a few selected tasks including name for assistant (Dodo), time, date, the ability to search for a specific query (e.g. cats), and the ability to pull up information regarding a specific or general location (google maps).

**Required dependencies** _pip install ..._
1.speechrecognition
2.pyaudio *see note 1 below*
3.playsound
4.gTTS (Google Text to audio)

NOTES/Issues:
1. Had issues installing pyaudio (pip install pyaudio, was not working. Instead used pipwin (refer to https://pypi.org/project/pipwin/) to install 
pip install pipwin
pipwin install pyaudio

2. Initially, program was not detecting words, due to ambient noise, adjusted for using sr.Recognizer class ( r.adjust_for_ambient_noise(source, duration=5) )
