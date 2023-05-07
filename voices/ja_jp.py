import pyttsx3
import runfile as r
import openai
import pyttsx3
import config
from googletrans import Translator

MODEL = config.model

#Translate to Vietnamese
translator = Translator()
openai.api_key = config.API_KEY

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

def japanese():
    engine.setProperty("voice", voices[2].id)
    engine.setProperty("rate", 140)
    while True:
        prompt = input("質問を入力してください: ")     
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
            print("Dịch sang tiếng Việt: ")
            tr = translator.translate(response, dest='vi')
            print(tr.text)
           

      