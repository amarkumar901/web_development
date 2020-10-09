import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',145)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis sir. My processor speed 2.6 giga hertz . How may i help you?")

def takecommand():
    #it takes microphone input from user and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('popularkid901@gmail.com','your-password')
    server.send('1905367@kiit.ac.in',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
    #if 1:
        query=takecommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
             speak('Searching wikipedia...')
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)

        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('www.google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('www.stackoverflow.com')

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        elif 'open visual code' in query:
            codepath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to amar' in query:
            try:
                speak('what should i say?')
                content=takecommand()
                to="popularkid901@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Amar bhai. I am not able to send this email.")

        elif 'exit' in query:
            quit()
