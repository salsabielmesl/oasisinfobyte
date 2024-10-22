import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import serpapi
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('SERPAPI_KEY')
client = serpapi.client(api_key=api_key)


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer=sr.Recognizer()
with sr.Microphone() as source :
 while True:
      print("Listening ...")
      audio=recognizer.listen(source)

      try:
            text = recognizer.recognize_google(audio)
            print(f'You said: {text}')
            
            if 'hello' in text.lower():
                speak("Hello!! How can I assist you today?")
            elif 'time' in text:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}.")
            elif 'date' in text:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}.")
            elif 'search' in text:
                result = client.search(
                    q = text,
                    engine = "google"
                )
                for item in result["organic_results"]:
                 print(item['title'])
                 print(item['link'])
                 print(item['snippet'])
                 print('-------------------')
            elif 'stop' in text:
                break
            else:
                speak("I'm sorry, I can only respond to simple commands!.")
        
      except sr.UnknownValueError:
            print("Sorry, I couldn't recognize your voice.")
