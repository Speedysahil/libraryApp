from newsapi import newsapi_client
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=ee0000163e5b407d8db850075d456714')
text = r.text
jaso = json.loads(text)

try :
    speak("your today's news")
    for i in range(0, 6):
        speak(jaso['articles'][i]['title'])


except Exception as e:
    speak("sorry no data found")