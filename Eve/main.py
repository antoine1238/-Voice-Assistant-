# importaciones de funciones
from modules.music import find_url, download_video, play, play_in_dir
from modules.listen import listen, listen_light, talk

import time

# Wikipedia
import wikipedia
wikipedia.set_lang("es")

# Time
from datetime import datetime
now = datetime.now()
months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


def Eve():
    """ start """
    while True: 
        rec = listen()
        # rec = input("comand: ") # for test

        # Music
        if "reproduce" in rec or "pon" in rec:
            if "reproduce" in rec:
                music = rec.replace("reproduce", "").strip()
            else:
                music = rec.replace("pon", "").strip()

            talk("reproduciendo " + music)

            exist = play_in_dir(music)
            if exist == True:
                pass
            else:
                url_search = find_url(music)
                download_video(url_search, music)
                print(url_search)
                play(music)

            
        elif "muéstrame la lista" in rec:
            pass


        elif "crear lista" in rec: 
            talk("quieres agregar datos o crear una lista nueva")
            while True:
                rec = listen_light()
                if "agregar" in rec:
                    pass
                if "crear" in rec:
                    pass
                if "cancela" in rec or "cancelar" in rec:
                    return talk("cancelando operación")


        # Wikipedia searches
        elif "quién es" in rec or "qué es" in rec or "qué es el" in rec or "qué es la" in rec:
            if "quién es" in rec:
                search = rec.replace("quién es ", "")
            elif "qué es el" in rec:
                search = rec.replace("qué es el ", "") 
            elif "qué es la" in rec:
                search = rec.replace("qué es la ", "")     
            else:
                search = rec.replace("qué es ", "")

            data = wikipedia.summary(search, sentences=2)
            talk(data)

        # Time
        elif "qué hora es" in rec or "qué dia es hoy":
            if "qué hora es" in rec:
                hour = f"son las {now.hour} con {now.minute} minutos"
            else:
                month = months[now.month - 1]
                hour = f"hoy es {now.day} de {month}"

            talk(hour)
        

        # Close
        elif "ciérrate" in rec:
            exit()
        
        else:
            talk("No te he entendido. intenta de nuevo")
Eve()