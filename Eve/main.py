# importaciones de funciones
from modules.music import find_url, download_video, play, play_in_dir
from modules.listen import listen, listen_light, talk
from modules.data import Data

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

            while True:
                rec = listen_light()

                # Creation
                if rec == "crear":
                    talk("como se va a llamar la lista")
                    name = listen_light()
                    talk(f"{name}. te parece bien el nombre?")

                    while True:
                        confirm = listen_light()    

                        if confirm == "si":
                            break
                        elif confirm == "no":
                            while confirm == "no":
                                talk("vale, dime el nombre que quieres ponerle")
                                name = listen_light()
                                talk(f"{name}. te parece bien el nombre?")
                                confirm = listen_light()    
                            break
                        else: 
                            talk("no te he entendido, intenta de nuevo")

                    talk(f"que quieres poner dentro de la lista {name}?")
                    content = listen_light()
                    Data.create(name, content)
                    talk("listo, quieres que lea tu lista?")

                    while True:
                        lead = listen_light()

                        if lead == "si":
                            talk(f"{name}: {content}")
                            break
                        elif lead == "no":
                            break
                        else: 
                            talk("no te he entendido, intenta de nuevo")
                    break
                
                # List
                elif rec == "listar":
                    pass 

                # Add
                elif rec == "agregar":
                    pass

                # Delete
                elif rec == "eliminar":
                    pass

                # Help
                elif rec == "qué puedes hacer":
                    talk("""
                        1: crear una tabla con datos dentro, 
                        2: añadir datos a una tabla existente, 
                        3: listar datos de una tabla, 
                        4: eliminar una un dato o toda la tabla si prefieres
                    """)
                
                # Quit
                elif "cancela" in rec or "cancelar" in rec:
                    talk("cancelando operación")
                    break
                else:
                    talk("no te he entendido, intenta de nuevo")
                


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
        elif rec == "qué hora es" or rec == "qué dia es hoy":
            if "qué hora es" in rec:
                hour = f"son las {now.hour} con {now.minute} minutos"
            else:
                month = months[now.month - 1]
                hour = f"hoy es {now.day} de {month}"

            talk(hour)
        

        # Close
        elif rec == "ciérrate":
            exit()
        
        else:
            talk("No te he entendido. intenta de nuevo")
Eve()