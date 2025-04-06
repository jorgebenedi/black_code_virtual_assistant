import time
import speech_recognition as sr
import webbrowser
import subprocess
import pygame
from notifypy import Notify
import sys

# Personalize these paths according to your files and configurations
audio_path = r'RUTA\A\TU\FOLDER\DE\AUDIOS'  # <-- Change this to your audio path
imou_path = r'RUTA\A\TU\PROGRAMA\IMOU'  # <-- Change this to your Imou executable path
ruta_scripts = r'RUTA\A\TU\FOLDER\DE\SCRIPTS'  # <-- Change this to your scripts path

pygame.init()

def play_audio(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def execute_script(scripts):
    subprocess.run(scripts)

def show_notify():
    notification = Notify()
    notification.title = "BLACK CODE"
    notification.message = "I’m listening..."
    notification.icon = r"C:\Users\jorge\Desktop\Accesos\Photoshop edit\jpg\black code\black_final (2).jpg"
    notification.send()

def process_commands(text):
    command = text.lower()

    if 'hello' in command or 'hello black code' in command:
        play_audio(audio_path + r'\beast.mp3')
    elif 'open youtube' in command or 'open youtube' in command:
        play_audio(audio_path + r'\youtube.mp3')
        time.sleep(1)
        webbrowser.open('https://www.youtube.com/')
    elif 'open google' in command or 'open google' in command:
        play_audio(audio_path + r'\performing_commands.mp3')
        webbrowser.open('http://www.google.com/')
    elif 'samsung' in command:
        play_audio(audio_path + r'\performing_commands.mp3')
        time.sleep(1)
        webbrowser.open('https://docs.google.com/spreadsheets/d/1DYxqTLZFOQGxjP59abxSpZ2TXBAeByqO04w0U3RsJxc/edit#gid=1331639910')
    elif 'email' in command:
        execute_script(ruta_scripts + r'\send_email.exe')
    elif "close" in command:
        sys.exit()
    else:
        play_audio(audio_path + r'\repeat_command.mp3')

recognizer = sr.Recognizer()

def listen_for_commands():
    try:
        with sr.Microphone() as source:
            print("Speak to Black Code... The darkness listens...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=30)
            text = recognizer.recognize_google(audio, language="en-US")
            print("Recognized text:", text)
            process_commands(text)
    except sr.UnknownValueError:
        print("I couldn’t hear you... Speak louder, or is it the silence playing tricks?")

if __name__ == "__main__":
    show_notify()
    while True:
        listen_for_commands()
