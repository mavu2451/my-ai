import openai
import config
import pyttsx3
import googletrans
import speech_recognition as sr

from voices import en_us as en
from voices import ja_jp as jp
from voices import vi_VN as vn

#Speech Recognition library
recognizer = sr.Recognizer()
WAKE_UP = "Hey AI"

#OpenAI library
openai.api_key = config.API_KEY

#Pyttsx3 library
engine = pyttsx3.init()


#Main
if __name__ == '__main__':
    print("Select your language: ")
    print("Default. English: ")
    print("      0. Japanese: ")
    print("      1. Vietnamese: ")
    # print("Your selection: ")
    lang= input("Your selection: ")
    match lang:
        case '0':
            jp.japanese()
        case '1':
            vn.vietnamese()
        case default:
            en.english()

