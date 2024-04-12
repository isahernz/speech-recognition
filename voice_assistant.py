from gtts import gTTS
from playsound import playsound
import os 
import speech_recognition as speech_r
import webbrowser


# Dicctionaries of words
synonymsThanks = ["GRACIAS", "NADA", "ES TODO", "ADIÓS", "BYE"]
synonymsMusic = ["MÚSICA", "CANCIONES", "ROLA", "ROLITA", "CANCIÓN"]
synonymsRock = ["ROCK"]
synonymsPop = ["POP"]
synonymsLove = ["BALADA", "ROMÁNTICA", "AMOR"]
synonymsSonidero = ["SONIDERA", "BAILE", "CUMBIA"]

def searchWordInDicctionary(dicctionaryWordsContext, sentence):
    words = sentence.split()
    for word in words:
      if word in dicctionaryWordsContext:
        return True
    return False

def createVoiceDialog(text):
  try:
    text_voice = gTTS(text = text, lang='es-us')
    x = open("archivo.mp3","wb+")
    text_voice.write_to_fp(x)
    x.close()
    playsound("archivo.mp3")
  except Exception as e:
    print("Error: ", e)
  finally:
    os.remove("archivo.mp3")

def recognizeAudio():
  r = speech_r.Recognizer()
  mic  = speech_r.Microphone()
  with mic as dialog:
          try:
            print("Escuchando")
            audio = r.listen(dialog)
          except TypeError as e: 
            print ("No entiendo", e)
  transcript = r.recognize_google(audio, language="es-MX")
  transcript = transcript.upper()
  print(f"El audio dice {transcript.format()}")
  return transcript

def askIfExit():
  createVoiceDialog("¿Te puedo ayudar en algo más")
  transcript = recognizeAudio()
  if searchWordInDicctionary(synonymsThanks, transcript):
    return True
  else:
    createVoiceDialog("¿Qué puedo hacer por ti?")

def createConversation():
    createVoiceDialog("Hola, soy tu asistente virtual, ¿en qué puedo ayudarte?")
    transcript = recognizeAudio()
    while True:
      if searchWordInDicctionary(synonymsThanks, transcript):
        createVoiceDialog("¡Fue un placer ayudarte!")
        return False

      # "Quiero escuchar música, cancion, melodia, sonido"
      if searchWordInDicctionary(synonymsMusic, transcript):
          createVoiceDialog("¿Qué tipo de música te gustaría escuchar?")
          transcript = recognizeAudio()

          if searchWordInDicctionary(synonymsRock, transcript):
              createVoiceDialog("¡Aquí tienes tu canción!")
              url = "https://www.youtube.com/watch?v=HQMdiGXYtCM"
              webbrowser.get().open(url)
              if askIfExit():
                createVoiceDialog("¡Fue un placer ayudarte!")
                break
              else:
                transcript = recognizeAudio()
                continue
      
          elif searchWordInDicctionary(synonymsLove, transcript):
              createVoiceDialog("¡Aquí tienes tu canción!")
              url = "https://www.youtube.com/watch?v=ipICdGojxug&t=1s"
              webbrowser.get().open(url)
              if askIfExit():
                createVoiceDialog("¡Fue un placer ayudarte!")
                break
              else:
                transcript = recognizeAudio()
                continue

          elif searchWordInDicctionary(synonymsSonidero, transcript):
            createVoiceDialog("¡Aquí tienes tu canción!")
            url = "https://www.youtube.com/watch?v=aGpEBxazyq4"
            webbrowser.get().open(url)
            if askIfExit():
              createVoiceDialog("¡Fue un placer ayudarte!")
              break
            else:
              transcript = recognizeAudio()
              continue

          elif searchWordInDicctionary(synonymsPop, transcript):
            createVoiceDialog("¡Aquí tienes tu canción!")
            url = "https://www.youtube.com/watch?v=wkJxbV1ZlE0"
            webbrowser.get().open(url)
            if askIfExit():
              createVoiceDialog("¡Fue un placer ayudarte!")
              break
            else:
              transcript = recognizeAudio()
              continue

      else:
          createVoiceDialog("No entiendo, ¿puedes repetir?")
          transcript = recognizeAudio()

createConversation()
