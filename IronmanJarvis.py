import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am jarvis sir, please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('gauravmalaviya183@gmail.com','84878gm@')
    server.sendmail('gauravmalaviya183@gmail.com',"",content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #logic for executing task  based on query

        #wikipedia
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)

        #youtube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        #google
        elif 'open google' in query:
            webbrowser.open("google.com")

        #playmusic
        elif 'play music' in query:
            music_dir = 'D:\\Gaurav\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        #time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")

        #email
        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "gauravmalaviya183@gmail.com"
                sendEmail(to, content)
                speak("eamil has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend. I am not able to send this email")

        elif "quit" in query:
            exit()
    #speak("Gaurav is a good boy")