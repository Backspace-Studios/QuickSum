import os
import keyboard as kb
import pyautogui as pag
from google import genai
import PIL.Image
import pyttsx3

engine = pyttsx3.init()

def tts(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()


def screenshot():
    pag.screenshot('ss.png')
    return ""

def query_ai():


    image = PIL.Image.open('ss.png')

    client = genai.Client(api_key="Almost left this in :o")
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["quickly summarise important information on what you see, without every mentioning that you are reading an image you were given. Summarise what you think I want to know. For example, if it's a Wikipedia page, summarise the article", image])
    summary = response.text.replace("*", "").replace("\n", " ")
    return summary

def main():
    while True:
        print("ready")
        kb.wait('alt')
        screenshot()
        summary = query_ai()
        os.remove('ss.png')
        print (summary)
        tts(summary)

main()
