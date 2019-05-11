'''
Created on May 10, 2019

@author: sthapa
'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    
    speak("My Name is kaancha!! How may i help you")
        



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold= 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:(query)\n")
        
    except Exception as e:
        print("Say that again please.....")
        return "None"
        
    return query       

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.tpls()
    server.login('tsgeek92@gmail.com', 'thapakazi92')
    server.sendmail('tsgeek92@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "open Jira" in query:
            webbrowser.open("https://jira.comscore.com/issues")
            
        
        elif "play music" in query:
            music_dir = "C:\\Users\\sthapa\\Music"
            songs = os.listdir(music_dir)
            print()
            os.startfile(os.path.join(music_dir, songs[0])) #can use random module to play random songs
            
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, the time is {strTime}")
        
        elif "open code" in query:
            codePath = "C:\\Users\\sthapa\\eclipse-workspace\\PythonTest\\src\\AI\\Demo\\KanchaDai.py"
            os.startfile(codePath)
            
        elif "email to Gaurav" in query: 
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "007gauravchhetri@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                speak("Sorry, Daju i  am not able to sent the email at the moment")
                
        elif "quit" in query:
            speak("good byee sir")
            exit()
                
                
                
                
                
            
        
        
            
            
            
                    
            
        
    
    
    #logic for exec tasks based on queries
    
    
   


