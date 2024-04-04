from gtts import gTTS
from playsound import playsound
import os 
import speech_recognition as speech_r
import webbrowser

r = speech_r.Recognizer() 
mic  = speech_r.Microphone()  

def createVoiceDialog(text):
    try:
          file = "archivo.mp3"
          text_voice = gTTS(text, lang='es-us')
          action = open(file, "wb+")
          text_voice.write_to_fp(action)
          action.close()
          playsound(file)
          os.remove(file)
    except Exception as e:
        print("Error reproduciendo el audio:", e)

def createConversation():
    createVoiceDialog("Hola, ¿en qué puedo ayudarte?")
    with mic as dialog:
          try:
            print("Escuchando")
            audio = r.listen(dialog)
          except LookupError: 
            print ("No entiendo")
    transcript = r.recognize_google(audio, language="es-MX")
    transcript = transcript.upper()
    print('el audio dice {}'.format(transcript))

    if "ENTRETENIMIENTO" in transcript:
        url = 'https://youtu.be/ue0RP3C1Brg?si=x3XPRkU4GxaojIjZ'
        createVoiceDialog("Listo fue un placer ayudarte, te dejo con un poco de música")
        webbrowser.get().open(url)
    else:
        createVoiceDialog("No entiendo")

createConversation()
