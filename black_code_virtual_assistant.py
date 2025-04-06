import threading
import time
import speech_recognition as sr
import webbrowser
import subprocess
import pygame
from notifypy import Notify
import sys

# Personalize these paths according to your files and configurations
audio_path = r'PATH\TO\YOUR\AUDIO\FOLDER'  # <-- Change this to your audio path
imou_path = r'PATH\TO\YOUR\IMOU\PROGRAM'  # <-- Change this to your Imou executable path
scripts_path = r'PATH\TO\YOUR\SCRIPTS\FOLDER'  # <-- Change this to your scripts path

pygame.init()

def play_audio(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def execute_script(script):
    subprocess.run(script)

def show_notification():
    notification = Notify()
    notification.title = "BLACK CODE"
    notification.message = "I’m listening..."
    notification.icon = r"C:\Users\jorge\Desktop\Accesos\Photoshop edit\jpg\black code\black_final (2).jpg"
    notification.send()

def process_commands(text):
    command = text.lower()

    if 'hello' in command or 'hello black code' in command:
        play_audio(audio_path + r'\beast.mp3')
    elif 'open youtube' in command:
        play_audio(audio_path + r'\youtube.mp3')
        time.sleep(1)
        webbrowser.open('https://www.youtube.com/')
    elif 'open google' in command:
        play_audio(audio_path + r'\performing_commands.mp3')
        webbrowser.open('http://www.google.com/')
    elif 'camera' in command or 'camera two' in command:
        play_audio(audio_path + r'\camera.mp3')
        threading.Thread(target=execute_script, args=(imou_path,)).start()
    elif 'email' in command:
        execute_script(scripts_path + r'\send_email.exe')
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
    show_notification()
    while True:
        listen_for_commands()
