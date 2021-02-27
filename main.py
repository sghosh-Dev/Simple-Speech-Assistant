import speech_recognition as sr 
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang ='en')
    rand = random.randint(1,10000000)
    filename = 'voice-' + str(rand) + '.mp3'
    tts.save(filename)
    print(text)
    playsound.playsound(filename)
    os.remove(filename)

def audio(ask = False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        speak('Go Ahead!')
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Dodo, very nice to meet you')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'what is the date' in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search = audio("What would you like to search?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('This is what I found for ' + search)
    if 'find location' in voice_data:
        location = audio("What place are you trying to find?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)    
    if 'exit' in voice_data:
        exit()


time.sleep(1)
speak('How can I help you')

while 1:
    voice_data = audio()
    #speak(voice_data) #test if capturing audio at all
    respond(voice_data)