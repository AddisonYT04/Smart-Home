# Home Virtual Assistant | House cleaning, doing chores or stuff that is productive.
import speech_recognition as sr
import pyttsx3
from tkinter import W
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def take_Command():
    try:
        with sr.Microphone() as source:
            print("Waiting patiently..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Emma" in command:
                command - command.replace("Emma", '')
                print(command)
    except:
        pass
    return command

def talk(text):
    engine.say(text)
    engine.runAndWait()

    # Music
    def Music(self,command):
        print(command)
        if("music" in command):
            self.talk('playing music on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=m-M1AtrxztU&list=RDm-M1AtrxztU')
            # This is a playlist | "&list=RDm"
        elif("burn" in command):
            self.talk('playing burn on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=CGyEd0aKWZE')
        elif('sugar' in command):
            self.talk('playing sugar on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=bvC_0foemLY')
        elif('bad habits' in command):
            self.talk('playing bad habits on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=orJSJGHjBLI')
        elif('levels' in command):
            self.talk('playing levels on youtube')
            webbrowser.open('https://youtu.be/_ovdm2yX4MA')
        elif('lush life' in command):
            self.talk('playing lush life on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=tD4HCZe-tew')
        elif('stay' in command):
            self.talk('playing stay on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=h--P8HzYZ74')
        elif('sweet escape' in command):
            self.talk('playing sweet escape on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=thpsmZiDv6U')
        elif('lights' in command):
            self.talk('playing lights on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=0NKUpo_xKyQ')
        elif('higher' in command):
            self.talk('playing higher on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=Rqsfa5At214')
        elif('i really like you' in command):
            self.talk('playing i really like you on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=qV5lzRHrGeg')
        elif('this is what you came for' in command):
            self.talk('playing this is what you came for on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=kOkQ4T5WO9E')
        elif('shape of you' in command):
            self.talk('playing shape of you on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=JGwWNGJdvx8')
        elif('shut up and dance' in command):
            self.talk('playing shut up and dance on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=6JCLY0Rlx6Q')
        elif("don't wanna know" in command):
            self.talk("playing I don't wanna know on youtube")
            webbrowser.open('https://www.youtube.com/watch?v=ANS9sSJA9Yc')
        elif('levitating' in command):
            self.talk("playing levitating on youtube")
            webbrowser.open("https://www.youtube.com/watch?v=TUVcZfQe-Kw")
        elif('one kiss' in command):
            self.talk('playing one kiss on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=DkeiKbqa02g')
        elif('rather be' in command):
            self.talk('playing rather be on youtube')
            webbrowser.open('https://www.youtube.com/watch?v=m-M1AtrxztU')
        else :
            self.No_result_found()

    # Start Of The Day
    def Intro(self):
        while True:
            self.permission = self.take_Command()
            print(self.permission)
            if ("good morning" in self.permission) or ("wake up" in self.permission):
                self.run_emma()
            elif ("goodnight" in self.permission) or ("good night" in self.permission):
                self.talk("Alright I'll be up all night protecting the house.")
                exit()
