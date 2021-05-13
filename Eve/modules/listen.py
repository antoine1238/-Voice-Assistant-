import speech_recognition as sr
import pyttsx3

# Reconocimiento de voz
name = "alexa"
listener = sr.Recognizer()  # Para reconocer la voz

# Configuración de Voz 
engine = pyttsx3.init()
voices = engine.getProperty("voices") # obtenemos una lista con todas las voces. son 3 en total 
engine.setProperty("voice", voices[0].id) # cambiamos la voz según el indice de la lista


def talk(rec):
    """ Repeat what you send """
    print(rec)
    engine.say(rec)
    engine.runAndWait()

def stop():
    engine.stop()


def listen():
    """ listen to what you say """
    while True:
        try:
            with sr.Microphone() as source:
                print("Escuchando...")
                voice = listener.listen(source) # convierte lo que dije en un audio
                rec = listener.recognize_google(voice, language="es-ES") # traduce lo que esta en el audio. 
                rec = rec.lower()
                if name in rec: # si encuentra su nombre en el audio, actuará
                    rec = rec.split(name)[1].strip() # quitamos el nombre de nuestro audio
                    print(rec)
                    return rec
        except:
            pass

    
def listen_light():
    """ listen to what you say """
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source) 
            rec = listener.recognize_google(voice, language="es-ES") 
            rec = rec.lower().strip()
            print(rec)
            return rec
    except:
        pass
