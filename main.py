import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
from config import apikey

import datetime
import cv2
import random

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr=""
def chat(query):
    global chatStr
    print(chatStr)
   # print(chatStr)
    openai.api_key = apikey
    chatStr+=f"Vicky: {query}\n Cad: "


    response = openai.Completion.create(
        engine="text-davinci-003",  # Use text-davinci-003 engine
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    talk(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(txt)


    # write a program to use open ai key
    # openai.api_key = apikey


def ai(prompt):
    openai.api_key = apikey
    txt=f"OpenAI response for Prompt: {prompt} \n  *********************\n\n"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Use text-davinci-003 engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    txt+=response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.makedirs("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]) }.txt","w") as f:
        f.write(txt)


def talk(text):
    # os.system(f"talk{text}")
    speaker.Speak(text)

'''def extract_prompt(query):
    # Assuming the user query starts with "using" and ends with "for"
    start_index = query.find("using") + len("using")
    end_index = query.rfind("for")
    if start_index != -1 and end_index != -1:
        return query[start_index:end_index].strip()
    else:
        return ""'''

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            #query = r.recognize_google(audio, language="hi-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from AI"


    # print("Enter the word you want to speak it out by computer")
   # s = input("Hello: ")
while True:
    print("ML")
    s="Hello, I am your Virtual Assistant"
    #speaker.Speak(s)
    talk(s)
    while True:
        print("Listening...")
        query = takeCommand().lower()  # # Convert the command to lowercase
        # todo: Add a feature to add more sites
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                talk(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # todo: Add a feature to play a specific song
        if "open music" in query:
            musicPath=r"C:\Users\VM706\Music\SKM.mp3"
            os.startfile(musicPath)
            #os.system(f'wmplayer.exe "{musicPath}"')
            #os.system(f'start "{musicPath}"')
            #subprocess.Popen([musicPath], shell=True)

        elif "time" in query:
            strfTime=datetime.datetime.now().strftime("%I:%M %p")
            print(strfTime)
            talk(f"Current time is {strfTime}")

        elif "open camera" in query:
            talk("Opening the camera...")
            cap = cv2.VideoCapture(0)

            while True:
                ret, frame = cap.read()
                cv2.imshow('Camera Feed', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif "open notepad" in query:
            talk("Opening notepad...")
            os.startfile(r"C:\Windows\System32\notepad.exe")

        elif "open calculator" in query:
            os.startfile(r"C:\Windows\System32\calc.exe")

        # Add more application opening commands as needed

        elif "using artificial intelligence" in query:


            ai(prompt=query)

        elif "Goodbye" in query:
            talk("Goodbye, have a nice day!")
            exit()  # Exit the inner loop, but not the entire program

        elif "exit" in query:
            exit()

        elif "reset chat" in query:
            chatStr= ""

        else:
            print("Chatting...")
            chat(query)



        #talk(query)

        #todo: WeatherAPI, News API, Add more features
