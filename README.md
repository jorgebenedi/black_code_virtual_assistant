# Black Code Virtual Assistant
![black_final](https://github.com/user-attachments/assets/9862f374-995e-481b-9e24-db68a2df0ef9)
### Description
```
=========================================================================================================
            A powerful voice-controlled assistant that responds to your commands
=========================================================================================================
BLACK CODE listens to your voice and performs various automated tasks with audio feedback
=========================================================================================================

Features:
- Voice command recognition in English
- Custom audio responses for different actions
- Web browser automation (YouTube, Google, etc.)
- Script execution capability
- Email sending functionality
- System notifications

Recommendations:
----Customize all paths in the script before use (audio, programs, scripts)
----Use a quality microphone for better recognition
----For email functionality, configure your SMTP credentials properly
----Run the script in a quiet environment for best results
----It is recommended to use it as an .exe to perform tasks via voice commands while doing any daily tasks, using the application: auto-py-to-exe
```
### Technologies
```
python3
SpeechRecognition
PyGame
NotifyPy
SMTP (for email functionality)
```
### Installation Guide
```
apt update && apt install python3 python3-pip git
pip install speechrecognition pygame notifypy
Configure paths in the script:
   - audio_path (for your audio files)
   - imou_path (for external programs)
   - ruta_scripts (for your script files)
   - Email credentials in the sendemail function
python black_code.py
```



