import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googlesearch import search



listener = sr.Recognizer()
engine = pyttsx3.init() #creating a engine to talk to me
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #changing voice from male to female

def talk(text):
   engine.say(text)
   engine.runAndWait()


def take_command():
   try:
    # Here i am using my mic to make it listen my audio 
    # giving it a name as source
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa','')
            print(command)
        
   except:
       pass
   return command


def run_alexa():
   command = take_command()
   print(command)
   if 'play' in command:
      song = command.replace('play','')
      talk('playing '+song)
      pywhatkit.playonyt(song) #using pywhatkit to play the song in youtube
   elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      print(time)
      talk('Current time is '+time)
   elif 'who is' in command:
      person = command.replace('who is','')
      info = wikipedia.summary(person,1)
      print(info)
      talk(info)
   elif 'what is' in command:
      Thing = command.replace('what is','')
      info = wikipedia.summary(Thing,1)
      print(info)
      talk(info)
   elif 'joke' in command:
      talk(pyjokes.get_joke())
   else:
      talk('Sorry , can you please say it again')   
      
      
while True:
    run_alexa()