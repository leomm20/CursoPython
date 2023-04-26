import speech_recognition as sr
from pathlib import Path
import os
import sys


print('\nSólo probado con archivos .wav!\n')
if len(sys.argv) > 1:
    if not Path(sys.argv[1]).exists():
        print('No existe la ruta')
        exit()
    else:
        path = Path(sys.argv[1])
else:
    path = Path(os.getcwd(), 'audios')

print(f'Continuará con la ruta {path}\n')

language = 'es-AR'
if len(sys.argv) > 2:
    if sys.argv[2].lower() == 'en-us':
        language = 'en-US'

if not path.exists():
    print('Ruta "audios" no encontrada')
    os.mkdir('audios')
    print('Directorio "audios" creado, poné tus audios en esta ruta')
    exit()
if not Path(path, 'processed').exists():
    os.mkdir(Path(path, 'processed'))

ls = os.listdir(path)
list_ = []
[list_.append(el) for el in ls if '.wav' in str(el)]
print('Archivos .wav encontrados: ' + str(len(list_)))
print()

r = sr.Recognizer()
for file in path.glob('*.wav'):
    print('Archivo:', file.name)
    try:
        with sr.AudioFile(str(file)) as source:
            audio_data = r.listen(source)
    except:
        print("NO PUEDO ABRIR EL ARCHIVO!!!\n")
        continue
    # Google Speech Recognition - Sólo para testing, sino, obtener una API-KEY
    # https://www.chromium.org/developers/how-tos/api-keys/
    try:
        g_text = r.recognize_google(audio_data, language=language, show_all=True)
        texto = 'Texto: ' + g_text['alternative'][0]['transcript'] + '\n'
        texto = texto + 'Aproximación: ' + str(round(float(g_text['alternative'][0]['confidence']) * 100, 2)) + '%'
        with open(Path(path, 'processed', file.stem + '.txt'), 'w') as f:
            f.write(texto)
        os.rename(file, Path(path, 'processed', file.name))
        print(texto)
        print('*' * 50)
    except sr.UnknownValueError:
        print("\nGoogle no entendió")
    except sr.RequestError as e:
        print("\nError de comunicación. Google Voice Recognition Service no respondió; {0}".format(e))
    except Exception as e:
        print('\nError genérico', e)
