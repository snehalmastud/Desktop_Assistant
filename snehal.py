def main():
    from gtts import gTTS
    import speech_recognition as sr
    import os
    import re
    import pygame
    from pygame import mixer
    import webbrowser
    import pyaudio
    import pyttsx3
    from google import google
    import requests
    import tkinter as tkr
    import random
    import time
    from google.cloud import translate
    import datetime

    player= tkr.Tk()

    translate_client = translate.Client()

    greeting_dict={'hi':'hi','hello':'hello','hey':'hey'}
    google_dict={'what':'what','why':'why','who':'who','which':'which','how':'how','when':'when'}
    translate_error_message = 'Sorry, Not able to translate. Try Again.'

    player.title("Audio Player")
    player.geometry("205x340")

    engine=pyttsx3.init()

    voices=engine.getProperty('voices')


    engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate)

    playlist=tkr.Listbox(player,highlightcolor="blue",selectmode= tkr.SINGLE)
    #print(songlist)



    def play(audio):
        files=audio
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(files)
        pygame.mixer.music.play()


    def ExitPlayer():
        pygame.mixer.music.stop()


    button1 = tkr.Button(player,width=5,height=3,text="PLAY",command=play)
    button1.pack(fill="x")
    button2 = tkr.Button(player,width=5,height=3,text="STOP",command=ExitPlayer)
    button2.pack(fill="x")



    label1= tkr.LabelFrame(player,text="Song Name")
    label1.pack(fill="both",expand="yes")
    contents1=tkr.Label(label1,text= file)
    contents1.pack()


    def translate(phrase):

        try:
            split_phrase = phrase.split(' ')
            list_remove = []
            list_remove.append(split_phrase[0])
            list_remove.append(split_phrase[-1])
            list_remove.append(split_phrase[-2])

            for word in list_remove:
                phrase = phrase.replace(word,'')

            phrase = phrase.strip()

            target = ''
            languages = translate_client.get_languages()
            for language in languages:
                if list_remove[1].lower() == language.get('name').lower():
                    target = language.get('language')

            if target=='':
                talkToMe(translate_error_message)
            else:
                translate = translate_client.translate(values=phrase,target_language=target)

            return translate

        except AttributeError:
            talkToMe(translate_error_message)

        except  IndexError:
            talkToMe(translate_error_message)



    def valid_google_search(phrase):
        if(google_dict.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
            return True

    def valid_greeting_search(phrase):
        if(greeting_dict.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
            return True


    def talkToMe(audio):
        "speaks audio passed as argument"

        print(audio)
        engine.say(audio)
        engine.runAndWait()

    def talk(audio):
        "speaks audio passed as argument"
        engine.say(audio)
        engine.runAndWait()


    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            talkToMe('Good Morning Snehal!')

        if currentH >= 12 and currentH < 18:
            talkToMe('Good Afternoon Snehal!')

        if currentH >= 18 and currentH !=0:
            talkToMe('Good Evening Snehal!')

    greetMe()



    def google_search_result(query):
        search_result=google.search(query)
        for result in search_result:
            talkToMe('Result Found')
            print(result.description)
            talk(result.description)
            break

    #google_search_result('how many states in india')


    def myCommand():
        "listens for commands"

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()

        except sr.UnknownValueError:
            talkToMe('Your last command couldn\'t be heard')
            command = myCommand();
        return command


    def sound():
        #pygame.init()
        mixer.init()
        mixer.music.load("good.mp3")


    def alarm():

        talkToMe('can you tell me Hour')
        hor=int(myCommand())
        talkToMe('can you tell me Minutes')
        minn=int(myCommand())
        talkToMe('can you tell me Seconds')
        sec=int(myCommand())

        n=5
        #talkToMe('can you tell me AM or PM')
        #af=myCommand()
        talkToMe('Alarm Set For '+ str(hor) + ' Hour ' +  str(minn)+ ' Minutes '+ str(sec)+ ' seconds')
        while True:
            if time.localtime().tm_hour==hor and time.localtime().tm_min==minn and time.localtime().tm_sec==sec:
                print ('wake up')
                break
        sound()
        while n>0:
            mixer.music.play()
            time.sleep(2)
            n=n-1
        sn=myCommand()
        if sn=='snooze':
            n=3
            time.sleep(60)
            while n>0:
                mixer.music.play()
                time.sleep(2)

        else:
            exit()


    def assistant(command):
        "if statements for executing commands"


        "This Commands For Open Web Pages Like Youtube, Google, Gmail, Instagram"


        if 'open youtube' in command:
            url = 'https://www.youtube.com/'
            talkToMe('Sure Snehal')
            webbrowser.open(url)
            print('Done!')

        elif 'open google' in command:
            url = 'https://www.google.com/'
            talkToMe('Sure Snehal')
            webbrowser.open(url)
            print('Done!')

        elif 'open facebook' in command:
            url = 'https://www.facebook.com/'
            talkToMe('Sure Snehal')
            webbrowser.open(url)
            print('Done!')

        elif 'open gmail' in command:
            url = 'https://mail.google.com/'
            talkToMe('Sure Snehal')
            webbrowser.open(url)
            print('Done!')

        elif 'open instagram' in command:
            url = 'https://www.instagram.com/'
            talkToMe('Sure Snehal')
            webbrowser.open(url)
            print('Done!')


        elif 'play music' in command:
            talkToMe('Sure Snehal')
            talkToMe('There Are Five Songs In Your Playlist')
            talkToMe('Child')
            talkToMe('Finally Found You')
            talkToMe('we found love')
            talkToMe('Live Young')
            talkToMe('Spaceman')
            talkToMe('which one you want to play?')
            song = myCommand()
            if song == 'child':
                play("Child.mp3")
                player.mainloop()

            elif song == 'finally found you':
                play("Finally Found You.mp3")
                player.mainloop()


            elif song == 'we found love':
                play("we found love.mp3")
                player.mainloop()


            elif song == 'live young':
                play("Live Young.mp3")
                player.mainloop()


            elif song == 'spaceman':
                play("Spaceman.mp3")
                player.mainloop()

            else:
                talkToMe('Song is not in playlist')


        # elif 'open downloads' in command:
        #     os.system('explorer C:\Users\SNEHAL\Downloads')


        elif 'open notepad' in command:
            os.system('notepad.exe')

        elif 'open powerpoint' in command:
            os.system('explorer C:\Program Files (x86)\Microsoft Office\Office14\POWERPNT.EXE')

        elif 'open wordpad' in command:
            os.system('explorer C:\Program Files (x86)\Microsoft Office\Office14\WINWORD.EXE')

        elif 'open paint' in command:
            os.system('mspaint.EXE')




        elif 'whats up' in command:
            talkToMe('Just doing my thing')

        #elif 'what is date' in command:
            now = datetime.now()
            print(now)

        elif 'how are you' in command:
            talkToMe('i am fine..how are you Snehal?')

        elif 'i am also fine' in command:
            talkToMe('thats good ')

        elif 'tell me about you' in command:
            talkToMe('Hiiii My Name is Chitti I am an Artificial Intilligence Designed by Snehal Mastud')

        elif  'tell me your name' in command:
            talkToMe('My Name is Chitti')

        elif 'tell me my name' in command:
            talkToMe('Your Name Is Snehal Mastud')

        elif 'good morning' in command:
            talkToMe('Good Morning Snehal')

        elif 'good afternooon' in command:
            talkToMe('Good Afternoon Snehal')

        elif 'good morning' in command:
            talkToMe('Good Night Snehal')

        elif 'tell me joke' in command:
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"}
                    )
            if res.status_code == requests.codes.ok:
                talkToMe(str(res.json()['joke']))
            else:
                talkToMe('oops!I ran out of jokes')

        elif 'set alarm' in command :
            alarm()


        elif 'calculate' in command:
            talkToMe('ok Snehal')
            talkToMe('what is the function Snehal?')
            function= myCommand()


            if function == 'addition':
                talkToMe('Can you tell me first number')
                a=int(myCommand())
                print(a)
                talkToMe('Can you tell me second number')
                b=int(myCommand())
                print(b)
                talkToMe('Ok Calculating')
                c=a+b
                talkToMe('Answer is')
                talkToMe(c)

            elif function == 'subtraction' :
                talkToMe('Can you tell me first number')
                a=int(myCommand())
                print(a)
                talkToMe('Can you tell me second number')
                b=int(myCommand())
                print(b)
                talkToMe('Ok Calculating')
                c=(a-b)
                talkToMe('Answer is')
                talkToMe(c)

            elif function == 'multiply' :
                talkToMe('Can you tell me first number')
                a=int(myCommand())
                print(a)
                talkToMe('Can you tell me second number')
                b=int(myCommand())
                print(b)
                talkToMe('Ok Calculating')
                c=a*b
                talkToMe('Answer is')
                talkToMe(c)

            elif function == 'divide' :
                talkToMe('Can you tell me first number')
                a=int(myCommand())
                print(a)
                talkToMe('Can you tell me second number')
                b=int(myCommand())
                print(b)
                talkToMe('Ok Calculating')
                c=a/b
                talkToMe('Answer is')
                talkToMe(c)

            else:
                talkToMe('sorry you enter wrong function')





        else:
            talkToMe('I don\'t know what you mean!')

    talkToMe('Hello Snehal what i can do for you?')

    #loop to continue executing multiple commands
    while True:

        command = myCommand()

        if valid_greeting_search(command):
            talkToMe('hii Snehal')

        #elif 'open' in command:
            #talkToMe('Ok Snehal')
            #os.system('explorer C:\\"{}"'.format(command.replace('open ','')))

        elif 'translate' in command:
                text = translate(command)
                print(text.get('translatedText'))

        elif valid_google_search(command):
            google_search_result(command)
            #print('In Google Search....')
            webbrowser.open('https://www.google.com/search?q={}'.format(command))
        elif 'bye' in command:
            talkToMe('Bye Have A Nice Day')
            exit()

        else:
            assistant(command)















