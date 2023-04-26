
texto = 'Hola! How are you?'

############################################################

# Con gTTS

from gtts import gTTS
import playsound

lang = 'es'
file_name = '../temp.mp3'
final_file = gTTS(text=texto, lang=lang)
final_file.save(file_name)
playsound.playsound(file_name, True)

############################################################

# Con pyttsx3

import pyttsx3

def hablar(mensaje, lang='es-AR' or 'es-SP' or 'I'):
    spanish_mexico = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'
    spanish_spain = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'
    english_usa = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
    engine = pyttsx3.init()
    match lang:
        case 'es-SP':
            engine.setProperty('voice', spanish_spain)
        case 'I':
            engine.setProperty('voice', english_usa)
        case _:
            engine.setProperty('voice', spanish_mexico)
    engine.say(mensaje)
    engine.runAndWait()

hablar(texto)