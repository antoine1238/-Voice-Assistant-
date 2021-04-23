# importaciones de funciones
from modules.music import find_url, download_video, play
from modules.listen import listen, listen_light, talk

import time

def Eve():
    """ start """
    while True: 
        rec = listen()

        if "reproduce" in rec or "pon" in rec:
            if "reproduce" in rec:
                music = rec.replace("reproduce", "")
            else:
                music = rec.replace("pon", "")

            talk("Reproduciendo" + music)
            search = find_url(music)
            print(search)
            download_video(search)
            play()
            
        if "muéstrame la lista" in rec:
            lista = ["antoine", "jesus roberto", "junior jesus", "emelin"]
            for idx, i in lista:
                talk(f"numero {idx} {i}")
                time.sleep(1)
                print(i)

        if "crear lista" in rec: 
            talk("quieres agregar datos o crear una lista nueva")
            while True:
                rec = listen_light()
                if "agregar" in rec:
                    pass
                if "crear lista nueva" in rec:
                    pass
                if "cancela" in rec or "cancelar" in rec:
                    return talk("cancelando operación")

        if "ciérrate" in rec:
            exit()
        
Eve()