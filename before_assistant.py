from gtts import gTTS
from playsound import playsound
import os 
import speech_recognition as sr
import webbrowser

fileP = "archivo.mp3" 
tts = gTTS ('¿que quieres buscar hoy', lang='es-us')
x = open(fileP,"wb+")
tts.write_to_fp(x)
x.close()
playsound(fileP)
os.remove(fileP)

r = sr.Recognizer() 
mic  = sr.Microphone()  

with mic as source:
    
    audio = r.listen(source) 
    
    try:
        print("Escuchando ")
    except LookupError: 
        print ("No entiendo")
transcript = r.recognize_google(audio, language="es-MX") 
transcript = transcript.upper()
print('el audio dice {}'.format(transcript))

url = 'https://google.com/search?q=' + transcript
webbrowser.get().open(url)
