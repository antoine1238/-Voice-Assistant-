# functions modules
from modules.music import main_music, play_in_dir, mixer
from modules.listen import listen, listen_light, say, engine, name
from modules.data import Data, files, name_files, main_data_create, main_data_add, main_data_delete

data_path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/Data"

# python lib
import multiprocessing
import pygame
import time
import os

# Music words
close = ["cierra la música", "quita la música", "cancela"]
resume = ["play", "reanuda", "quita el pause"]
pause = ["silencio", "pause", "pausa"]

# list words
c_words = ["crea una lista llamada", "crea una lista con el nombre", "crea una nueva lista llamada", "crea una lista nueva con el nombre"]
a_words = ["agrega datos a la lista", "añade datos a la lista", "dale datos a la lista", "ingresa datos a la lista", "mete datos a la lista"]
d_words = ["elimina la lista", "elimina la lista llamada", "eliminame la lista", "eliminame la lista llamada"]
l_words = ["cuántas listas tengo", "qué cantidad de listas tengo", "cuáles son mis listas"]
r_words = ["léeme la lista", "léeme la lista llamada", "lée la lista", "lée la lista llamada"]

# Wikipedia
import wikipedia
wikipedia.set_lang("es")
w_words = ["quién es", "qué es", "qué es el", "qué es la", "háblame sobre", "háblame de"]

# Time
from datetime import datetime
now = datetime.now()
months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")


def talk(rec):
    """ Multiprocessing. to be able to cancel while talking """
    if __name__ == "__main__":
        p = multiprocessing.Process(target=say, args=(rec,))
        p.start()
        while p.is_alive():
            comand = listen_light()
            if comand == f"{name} silencio" or comand == f"{name} cállate":
                p.terminate()
                return
        p.close()
                

def Eve():
    """ start """
    while True: 
        rec = listen()


        # File update
        for i in os.listdir(data_path):
            name_files.append(i.replace(".csv", ""))


        # Music
        if "reproduce" in rec or "pon" in rec:
            if rec == "pon" or rec == "reproduce":
                continue
            else:
                if "reproduce" in rec:
                    music = rec.replace("reproduce", "").strip()
                else:
                    music = rec.replace("pon", "").strip()

                say("reproduciendo " + music)

                main_music(music)
        
        # Pause
        elif rec == pause[0] or rec == pause[1] or rec == pause[2]:
            try:
                mixer.music.pause()
            except pygame.error:
                say("no esta sonando nada")

        # Resume
        elif rec == resume[0] or rec == resume[1] or rec == resume[2]:
            try:
                mixer.music.unpause()    
            except pygame.error:
                say("no has puesto música")

        # Music close
        elif rec == close[0] or rec == close[1] or rec == close[2]:
            try:
                mixer.music.stop() 
                mixer.quit()
            except pygame.error:
                say("no hay música que quitar")


        # List creation
        elif c_words[0] in rec or c_words[1] in rec or c_words[2] in rec or c_words[3] in rec:
            if "crea una lista llamada" in rec:
                my_list = rec.replace("crea una lista llamada ", "")
            elif "crea una lista con el nombre" in rec:
                my_list = rec.replace("crea una lista con el nombre ", "")
            elif "crea una lista nueva con el nombre" in rec:
                my_list = rec.replace("crea una lista nueva con el nombre ", "")
            else:
                my_list = rec.replace("crea una nueva lista llamada ", "")

            main_data_create(my_list)


        # Add data 
        elif a_words[0]  in rec or a_words[1] in rec or a_words[2] in rec or a_words[3] in rec or a_words[4] in rec:
            if "agrega datos a la lista" in rec:
                my_list = rec.replace("agrega datos a la lista ", "")
            elif "añade datos a la lista" in rec:
                my_list = rec.replace("añade datos a la lista ", "")
            elif "dale datos a la lista" in rec:
                my_list = rec.replace("dale datos a la lista ", "")
            elif "ingresa datos a la lista" in rec:
                my_list = rec.replace("ingresa datos a la lista ", "")
            else:
                my_list = rec.replace("mete datos a la lista ", "")
            
            if not my_list in name_files:
                say("esa lista no existe, intenta de nuevo")
            else:
                main_data_add(my_list)
                

        # List delete
        elif d_words[0] in rec or d_words[1] in rec or d_words[2] in rec or d_words[3] in rec:
            if "eliminame la lista llamada" in rec:
                my_list = rec.replace("eliminame la lista llamada ", "")
            elif "elimina la lista llamada" in rec:
                my_list = rec.replace("elimina la lista llamada ", "")
            elif "eliminame la lista" in rec:
                my_list = rec.replace("eliminame la lista ", "")
            else:
                my_list = rec.replace("elimina la lista ", "")
            
            if not my_list in name_files:
                say("no tengo ninguna lista con ese nombre")
            else:
                main_data_delete(my_list)


        # List 
        elif rec == l_words[0] or rec == l_words[1] or rec == l_words[2]:
            number_files = len(files)
            talk(f"tienes un total de {number_files} archivos, cuyos nombres son:")
            for i in name_files:
                talk(i)


        # Read a list
        elif r_words[0] in rec or r_words[1] in rec or r_words[2] in rec or r_words[3] in rec:
            if "léeme la lista llamada" in rec:
                my_list = rec.replace("léeme la lista llamada ", "")
            elif "lée la lista llamada" in rec:
                my_list = rec.replace("lée la lista llamada ", "")
            elif "léeme la lista" in rec:
                my_list = rec.replace("léeme la lista ", "")
            else:
                my_list = rec.replace("lée la lista ", "")

            try:
                Data.read(my_list)
                while True:
                    say("quieres que lo lea de nuevo?")
                    choice = listen_light()

                    if choice == "si" or choice == "ok":
                        Data.read(my_list)
                    elif choice == "no" or choice == "cancela":
                        say("ok, saliendo")
                        break 
                    else:
                        say("no te he entendido, intenta de nuevo")
            except FileNotFoundError:
                say("no existe esa lista, intenta de nuevo")
            

        # Wikipedia searches
        elif w_words[0] in rec or w_words[1] in rec or w_words[2] in rec or w_words[3] in rec or w_words[4] in rec or w_words[5] in rec:
            if "quién es" in rec:
                search = rec.replace("quién es ", "")
            elif "qué es el" in rec:
                search = rec.replace("qué es el ", "") 
            elif "qué es la" in rec:
                search = rec.replace("qué es la ", "")   
            elif "háblame sobre" in rec:
                search = rec.replace("háblame sobre ", "") 
            elif "háblame de" in rec:
                search = rec.replace("háblame de ", "")   
            else:
                search = rec.replace("qué es ", "")
            
            say(f"cuanto quieres que te lea sobre {search}")
            
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
                    say("no te he entendido, vuelve a intentarlo")
                    
                data = wikipedia.summary(search, sentences=amount)

                try:
                    mixer.music.set_volume(0.0)
                    talk(data)
                    mixer.music.set_volume(0.5)
                except pygame.error:
                    talk(data)
        

        # Scraping
        

        # Time
        elif rec == "qué hora es" or rec == "qué dia es hoy":
            if "qué hora es" in rec:
                hour = f"son las {now.hour} con {now.minute} minutos"
            else:
                month = months[now.month - 1]
                hour = f"hoy es {now.day} de {month}"

            try:
                mixer.music.set_volume(0.1)
                say(hour)
                mixer.music.set_volume(0.5)
            except pygame.error:
                say(hour)
        

        # Help
        elif rec == "qué puedes hacer":
            try:
                mixer.music.set_volume(0.1)
            except pygame.error:
                pass
            talk("""vale: 
                puedo descargar la musica que me digas y luego reproducirla, ya una vez descargada puedes reproducirla instantaneamente en otro momento si prefieres.
                puedo hacer las busquedas que quieras y usaré wikipedia para leerte sus conceptos, según me indiques puedo leerte mucho o poco.
                puedo crear listas para guardar texto dentro y cuando quieras tambien puedo leertelas, agregarle mas contenido o eliminarlas si prefieres.
                puedo hacer funciones básicas como dar la hora actual o en que dia estamos.
            """)
            try:
                mixer.music.set_volume(0.5)
            except pygame.error:
                pass


        # Close
        elif rec == "ciérrate":
            exit()
        
        else:
            try:
                mixer.music.set_volume(0.1)
                say("No te he entendido. intenta de nuevo")
                mixer.music.set_volume(0.5)
            except pygame.error:
                say("No te he entendido. intenta de nuevo")


if __name__ == "__main__":
    Eve()
