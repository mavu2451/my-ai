import pyttsx3
import speech_recognition as sr
import whisper
import openai
import config

# model = whisper.load_model("base")
# result = model.transcribe("audio.wav")


# WAKE_UP = "Hey"
recognizer = sr.Recognizer()
# translator = Translator()

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")

# engine.setProperty("voice", voices[1].id)
# text= "Hello friends hey"
# engine.say(text)
# engine.runAndWait()

# tr = translator.translate(text, dest='vi')
# print(tr.text)

# def wake_up(phrase):
#     if WAKE_UP in phrase.lower():
#         return WAKE_UP
#     else:
#         return None

# async def main():
#     while True:
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             print(f"ok chat")

#             while True:
#                 audio = recognizer.listen(source)
#                 try:
#                     with open("audio.wav","wb") as f:
#                         f.write(audio.get_wav_data())
#                     model = whisper.load_model("tiny")
#                     result = model.transcribe("audio.wav")
#                     phrase = result["text"]
#                     print(f"You said: {phrase}")

#                     wakeup = wake_up(phrase)
#                     if wakeup is not None:
#                         break
#                     else:
#                         print("Try again")

#                 except Exception as e:
#                     print("error")
#                     continue

print("Speak: ")
try:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"You said: {text}")  
        with open('./audio/audio.wav','wb') as f:
            f.write(audio.get_wav_data())
except Exception as e:
    print("Can't hear")
# if __name__ == '__main__':
#     print(result["text"])