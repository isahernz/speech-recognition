from gtts import gTTS
from playsound import playsound
import os 
import speech_recognition as speech_r
import webbrowser

r = speech_r.Recognizer() 
mic  = speech_r.Microphone()  

def createVoiceDialog(text):
  try:
    text_voice = gTTS(text = text, lang='es-us')
    text_voice.save("archivo.mp3")
    playsound("archivo.mp3")
  except Exception as e:
    print("Error: ", e)
  finally:
    os.remove("archivo.mp3")

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

    if "AIRBAG" in transcript:
      createVoiceDialog("Listo fue un placer ayudarte, te dejo con un poco de música")
      url = 'https://youtu.be/ue0RP3C1Brg?si=x3XPRkU4GxaojIjZ'
      webbrowser.get().open(url)
    else:
        createVoiceDialog("No entiendo")

createConversation()
