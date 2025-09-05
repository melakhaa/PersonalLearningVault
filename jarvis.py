import speech_recognition as sr
from gtts import gTTS
import pygame, pywhatkit, datetime, webbrowser, os, time

listener = sr.Recognizer()

# Fungsi buat ngomong
def talk(text):
    file = "temp.mp3"   
    gTTS(text=text, lang='en', tld='co.uk').save(file)

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop() 
    pygame.mixer.quit()
    os.remove(file)

# Fungsi buat denger suara
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            return listener.recognize_google(voice).lower()
    except:
        return ""

# Fungsi buat ngejalanin perintah
def run_jarvis():
    command = take_command()
    if "time" in command:
        talk("The time is " + datetime.datetime.now().strftime("%H:%M"))
    elif "youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "search" in command:
        query = command.replace("search", "")   
        talk("Searching for " + query)
        print(f"Searching for: {query}")
        pywhatkit.search(query)
    elif "stop" in command or "exit" in command:
        talk("Goodbye!")
        exit()
    elif command != "":
        talk("Sorry, I can't hear you.")

# Sapaan awal
talk("Hello, I am Jarvis. How can I help you?")

# Loop utama
while True:
    run_jarvis()