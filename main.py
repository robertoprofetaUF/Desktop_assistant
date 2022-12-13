import pyttsx3 #module that we use to intepretate the text and make our program talk
import speech_recognition as sr #recognizes the voice of the user and translate commands to text inputs
import datetime #for date and time information
import wikipedia #to gather information from wikipedia
import webbrowser #interact with web browsers
import subprocess #open applications 
import os
import pywhatkit
import openai

#Secret key:
#openai_key = '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'
openai.api_key = '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'


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak function will produce audio with the string that it takes as input
def speak(text):
    engine.say(text)
    engine.runAndWait()

#greetMe function welcomes the user when it is called
def greetMe():
    hour = int(datetime.datetime.now().hour) #Depending on the time, the greet function will greet with a different word
    print(hour) 

    if hour >=0 and hour <12:
        speak("Good morning my friend!")

    elif hour >=12 and hour <18:
        speak("Good afternoon my friend!")
    
    else:
        speak("Good evening my friend!") 

    speak("Hasbulla is here to help you...")  

#takeOrder is the function that captures the order given by the user to run the code
def takeOrder():

    speak('Ready to listen...')

    r = sr.Recognizer()

    with sr.Microphone() as source: 
        print("Listening...")
        r.dynamic_energy_threshold = False
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    
    
    except Exception as e:
        speak("I didn't understand you...")
        query = None
        
    return query

#Main Program starts here
greetMe()

active = True

while active:

    query = takeOrder()

#Logic to execute tasks based on the instructions by the user
#The data structure followes a while loop that stays active until the user decides he does not want it running anymore

    if query == None:
        print("Didn't receive command")
        speak("Didn't receive command")
        continue
    

#The assistant answers to the question by the user  
    elif 'how are you' in query.lower():
        print('I am doing fine, happy to serve...')
        speak('I am doing fine, happy to serve...')
        
#The assistant plays a video on youtube (ideally music)  
    elif 'play' in query.lower() and 'on youtube' in query.lower():
        query = query.replace('play','').replace('on youtube','')
        pywhatkit.playonyt(query)

#This statement was generated using the OpenAI API from DALL-E-2 to generate AI images based on the input from the user
    elif 'create image' in query.lower():
        query = query.replace('generate image of','')
        size = '1024x1024'
        gen_image = openai.Image.create(
            prompt = query, 
            n = 1, 
            size = "1024x1024" 
        )

        image_url = gen_image['data'][0]['url']
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(image_url)

#This statement retrieves the current time
    elif 'time is' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The time is {strTime}")
        speak(f"The time is {strTime}")

#This statement retrieves the current date
    elif 'date' and 'today' in query.lower():
        strDate = datetime.datetime.now().date()
        print(f"The date is {strDate}")
        speak(f"The date is {strDate}")        

#This statement looks for the input of the user in wikipedia, if it does not finda match, it will just produce a google search
    elif 'search'in query.lower() or 'what is' in query.lower() or 'who is' in query.lower():
        
        try:
            speak('Searching...')
            query = query.replace("search ","").replace("what is the","").replace("who is ","").replace("what is a","").replace("what is","")
            result = wikipedia.summary(query, sentences = 2, auto_suggest = False)
            print(result)
            speak(result)
        
        except Exception:
            query = query.replace("search ","").replace("what is the","").replace("who is ","").replace("what is a","").replace("what is","")
            pywhatkit.search(query)

#This statement opens the calculator:
    elif 'open calculator' in query.lower():
        subprocess.call('calc.exe')

#This statement uses the word run as input to open different applciations in the computer of the user:
    elif 'run' in query.lower():
        if 'microsoft word' in query.lower():
            subprocess.Popen("C:\Program Files (x86)\Microsoft Office\\root\Office16\WINWORD.EXE")
        elif 'microsoft excel' in query.lower():
            subprocess.Popen("C:\Program Files (x86)\Microsoft Office\\root\Office16\EXCEL.EXE")
        elif 'microsoft powerpoint' in query.lower():
            subprocess.Popen("C:\Program Files (x86)\Microsoft Office\\root\Office16\POWERPNT.EXE")
        elif 'spotify' in query.lower():
            subprocess.Popen("spotify.exe")
        elif 'minecraft' in query.lower():
            subprocess.Popen("C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe")

#This statement uses the word open as an input to open any .com webpage using chrome
    elif 'open' in query.lower():
        query = query.replace("open ","")
        page = f"{query}.com"
    
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(page)
        continue

#This stament use the word exit as the input to close apps
    elif 'exit' in query.lower():
        if 'microsoft word' in query.lower():
            os.system("taskkill /f /im winword.exe")
        
        elif 'microsoft excel' in query.lower():
            os.system("taskkill /f /im excel.exe")
        
        elif 'chrome' in query.lower():
            os.system("taskkill /f /im chrome.exe")

        elif 'power point' in query.lower():
            os.system("taskkill /f /im powerpnt.exe")

        elif 'minecraft' in query.lower():
            os.system("taskkill /f /im MinecraftLauncher.exe")

        else:
            query = query.replace("close", "")
            os.system("taskkill /f /im {query}.exe")

#This statement finishes the program if the user says goodbye or stop
    elif 'goodbye' in query.lower() or 'stop' in query.lower():
        print("Have a good one, I will be here for you")
        speak("Have a good one, I will be here for you")
        active = False

    else:
        print("Didn't receive command")
        speak("Didn't receive command")
        



