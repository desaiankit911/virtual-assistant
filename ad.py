from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open fb' in command:
        reg_ex = re.search('open facebook (.*)', command)
        url = 'https://www.facebook.com/'
        if reg_ex:
            subfb = reg_ex.group(1)
            url = url + 'r/' + subfb
        webbrowser.open(url)
        print('Done!')

    if 'open youtube' in command:
        reg_ex = re.search('open youtube (.*)', command)
        url = 'https://www.youtube.com/'
        if reg_ex:
            subyoutube = reg_ex.group(1)
            url = url + 'r/' + subyoutube
        webbrowser.open(url)
        print('Done!')

     
        
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'mail' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'ankit' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('desaiankit911@gmail.com', 'ad8898301742')

            #send message
            mail.sendmail('ankit desai', 'ankit.desai@monginis.net', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        if 'subhash' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('desaiankit911@gmail.com', 'ad8898301742')

            #send message
            mail.sendmail('Subhash desai', 'dsubhash9820@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')
            
        if 'nikhil' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('desaiankit911@gmail.com', 'ad8898301742')

            #send message
            mail.sendmail('Nikhil Wani', 'nikhilwani05@gmail.com ', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        if 'sumit' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('desaiankit911@gmail.com', 'ad8898301742')

            #send message
            mail.sendmail('Sumeet Desai', 'soumitred@gmail.com ', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')
            
    elif 'calculator' in command:
        talkToMe('what do you what to calculate')
        recipient = myCommand()
        
        if 's' in recipient:
            talkToMe("give me two numbers")
            
talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
