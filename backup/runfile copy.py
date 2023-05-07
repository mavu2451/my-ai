import openai
import config
import pyttsx3

from voice import en_us as e


engine = pyttsx3.init()

openai.api_key = config.API_KEY

model="text-davinci-003"
# print("Select your language: ")
# print("1. English: ")
# print("2. Japanese: ")
# print("3. Vietnamese: ")
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
            model=model,
            prompt=prompt,
            max_tokens=4000,
            )      
            response= completion.choices[0].text
            print(response)
            engine.say(response)
            engine.runAndWait()


def japanese():

    engine.setProperty("voice", voices[3].id)
    engine.setProperty("rate", 140)
    while True:
        prompt = input("質問を入力してください: ")     
        if prompt == "":
            print("Stop")
            break
        else:
            completion = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=4000,
            )   
            response= completion.choices[0].text
                
            print(response)
            engine.say(response)
            engine.runAndWait()

def vietnamese():

    engine.setProperty("voice", voices[4].id)
    engine.setProperty("rate", 140)
    while True:
        prompt = input("Mời nhập câu hỏi: ")     
        if prompt == "":
            print("Stop")
            break
        else:
            completion = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=4000,
            )   
            response= completion.choices[0].text
            print(response)
            engine.say(response)
            engine.runAndWait()




if __name__ == '__main__':
    e.test()
    print("Select your language: ")
    print("0. English: ")
    print("1. Japanese: ")
    print("2. Vietnamese: ")
    print("Your selection: ")
    lang= input()
    match lang:
        case '0':
            english()
        case '1':
            japanese()
        case '2':
            vietnamese()

