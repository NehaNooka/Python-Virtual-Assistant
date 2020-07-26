#libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

#ignore any warning msgs
warnings.filterwarnings('ignore')

#record audio and return as str
def recordAudio():
    #record audio
    r=sr.Recognizer()
    #open microphone
    with sr.Microphone() as source:
        print('Say Something')
        audio=r.listen(source)

    #use google speech recognition
    data=''
    try:
        data=r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError:
        print("Google speech recognition couldnt understand the audio,unknown error")
    except sr.RequestError as e:
        print("request  results from google speech recognition service error "+e)
    return data
    #data is the text form of our audio

#assistant response from text to speech
def assistantResponse(text):
    print(text)
    myobj=gTTS(text=text,lang='en',slow=False)

    #save audio to a file
    myobj.save('assistant_response.mp3')

    #play converted file
    os.system('start assistant_response.mp3')

#a function for wake words to start
def WakeWord(text):
    WAKE_WORDS=['hey monica','okay monica'] #list

    text=text.lower()

    #check text and wake words
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False

#A function to return current date
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day

    #list of months
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    #list of ordinal num
    ordinalnum=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']


    return ('Today is  '+weekday+' '+ month_names[monthNum-1] +' '+ordinalnum[dayNum-1]+'.')

#Function to return random greeting
def greeting(text):
    GREETING_INPUTS=['hi','hey','hello','hola','wassup']
    GREETING_RESPONSES=['howdy','hello there','hey there','whats up']

    #return random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return(random.choice(GREETING_RESPONSES)+'.')
    #no greeting then empty str
    return("")

#Function to get person first and last name
def getPerson(text):
    wordList = text.split()

    for i in range(0,len(wordList)):
        if i+3<=len(wordList)-1 and wordlist[i].lower()=='who' and wordList[i+1].lower()=='is':
            return (wordList[i+2]+''+wordList[i+3])

while True:

    #record audio
    text=recordAudio()
    response=""

    #check for wake word
    if (WakeWord(text)==True):
        
        #check for greeings
        response=response+greeting(text)

        #check for date
        if('date' in text):
            get_date=getDate()
            response=response+''+get_date
        #check for time
        if('time' in text):
            now=datetime.datetime.now()
            moridiem=''
            if now.hour>=12:
                meridiem="p.m."
                hour=now.hour-12
            else:
                meridiem="a.m."
                hour=now.hour
            #convert min into str
            if now.minute<10:
                minute='0'+str(now.minute)
            else:
                minute=str(now.minute)
            response=response+' '+"It is"+str(hour)+":"+str.minute+" "+meridiem+'.'
        #check for WHO IS..
        if( 'who is' in text):
            person = getPerson(text)
            wiki=wikipedia.summary(person,sentences=2)
            response=response+''+wiki
        assistantResponse(response)