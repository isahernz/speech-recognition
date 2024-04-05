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

def recognizeAudio():
  with mic as dialog:
          try:
            print("Escuchando")
            audio = r.listen(dialog)
          except LookupError: 
            print ("No entiendo")
  transcript = r.recognize_google(audio, language="es-MX")
  transcript = transcript.upper()
  print('el audio dice {}'.format(transcript))
  return transcript

def createConversation():
    createVoiceDialog("Hola, ¿en qué puedo ayudarte?")
    transcript = recognizeAudio()
    while "GRACIAS" not in transcript:
      if "PELÍCULAS" in transcript:
        createVoiceDialog("Puedes ir al cine o ver una película en casa")
        transcript = recognizeAudio()
        if "ABRE" in transcript:
            url = "https://www.youtube.com/watch?v=jzfJU-J9UL8"
            webbrowser.get().open(url)
            createVoiceDialog("¿Hay algo más en lo que pueda ayudarte?")
            transcript = recognizeAudio()
      else:
          createVoiceDialog("No entiendo, ¿puedes repetir?")
          transcript = recognizeAudio()
    createVoiceDialog("Fue un placer ayudarte")
createConversation()
