# importaciones de funciones
from modules.music import find_url, download_video, play, play_in_dir
from modules.listen import listen, listen_light, talk
from modules.data import Data, main_data

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
        # rec = listen()
        rec = input("comand: ") # for test

        # Music
        if "reproduce" in rec or "pon" in rec:
            if rec == "pon" or rec == "reproduce":
                continue
            else:
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

        # List creation
        elif rec == "muéstrame la lista" or rec == "abre la lista":
            talk("listo, que quieres hacer")
            main_data()


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
            
            talk(f"cuanto quieres que te lea sobre {search}")
            
            while True:
                question = listen_light()

                if not question:
                    continue
                
                if question == "bastante" or question == "mucho" or question == "demasiado":
                    amount = 7
                elif question == "no demasiado" or question == "mas o menos":
                    amount = 3
                elif question == "un poco" or question == "poco" or question == "poquito":
                    amount = 2
                elif question == "muy poco":
                    amount = 1
                else:
                    talk("no te he entendido, vuelve a intentarlo")
                    
                data = wikipedia.summary(search, sentences=amount)
                talk(data)
                break

        # Time
        elif rec == "qué hora es" or rec == "qué dia es hoy":
            if "qué hora es" in rec:
                hour = f"son las {now.hour} con {now.minute} minutos"
            else:
                month = months[now.month - 1]
                hour = f"hoy es {now.day} de {month}"

            talk(hour)
        
        elif rec == "qué puedes hacer":
            talk("""vale: 
                puedo descargar la musica que me digas y luego reproducirla, ya una vez descargada puedes reproducirla instantaneamente en otro momento si prefieres.
                puedo hacer las busquedas que quieras y usaré wikipedia para leerte sus conceptos, según me indiques puedo leerte mucho o poco.
                puedo crear listas para guardar texto dentro y cuando quieras tambien puedo leertelas, agregarle mas contenido o eliminarlas si prefieres.
                puedo hacer funciones básicas como dar la hora actual o en que dia estamos.
             """)

        # Close
        elif rec == "ciérrate":
            exit()
        
        else:
            talk("No te he entendido. intenta de nuevo")
Eve()