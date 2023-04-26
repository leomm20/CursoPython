import speech_recognition as sr
import winsound


def transformar_audio_en_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        print('Esperá...')
        winsound.Beep(2000, 75)
        winsound.Beep(2000, 75)
        # escucha por 5 segundos y calcula el nivel de ruido ambiente
        r.adjust_for_ambient_noise(origen, duration=2)
        r.dynamic_energy_threshold = True  # si cambia continuamente el ruido ambiente, poner en True
        winsound.Beep(2100, 110)
        print("Dime: ")
        audio = r.listen(origen, timeout=100, phrase_time_limit=10)
        try:
            q = r.recognize_google(audio, language="es-AR")
            return q.lower()
        except sr.UnknownValueError as err:
            print("No entendí - Repetilo por favor", err)
            return ""
        except sr.RequestError as err:
            print("Request Error", err)
            return ""
        except:
            print("No entendí - Error Genérico")
            return ""


while True:
    dijiste = transformar_audio_en_texto()
