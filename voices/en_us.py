import pyttsx3
import runfile as r
import openai
import pyttsx3
import config

MODEL = config.model

openai.api_key = config.API_KEY

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

def english():
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 140)
    while True:
        prompt = input("Enter question: ")     
        if prompt == "":
            print("Stop")
            break
        else:
            completion = openai.Completion.create(
            model=MODEL,
            prompt=prompt,
            max_tokens=4000,
            )      
            response= completion.choices[0].text
            print(response)
            engine.say(response)
            engine.runAndWait()
