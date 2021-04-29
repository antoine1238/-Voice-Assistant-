# importaciones de funciones
from modules.music import find_url, download_video, play, play_in_dir
from modules.listen import listen, listen_light, talk

import time

def Eve():
    """ start """
    while True: 
        rec = listen()
    
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
            lista = ["antoine", "jesus roberto", "junior jesus", "emelin"]
            for i in lista:
                talk(i)

        elif "crear lista" in rec: 
            talk("quieres agregar datos o crear una lista nueva")
            while True:
                rec = listen_light()
                if "agregar" in rec:
                    pass
                if "crear lista nueva" in rec:
                    pass
                if "cancela" in rec or "cancelar" in rec:
                    return talk("cancelando operación")

        elif "ciérrate" in rec or "chao" in rec:
            exit()
        
        else:
            talk("No te he entendido. intenta de nuevo")
Eve()