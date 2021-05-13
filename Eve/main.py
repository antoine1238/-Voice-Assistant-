# importaciones de funciones
from modules.music import find_url, download_video, play, play_in_dir
from modules.listen import listen, listen_light, talk
from modules.data import Data, main_data, files, name_files

data_path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/Data"


# python lib
import time
import os

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
        elif c_words[0] in rec or c_words[1] in rec or c_words[2] in rec or c_words[3] in rec:
            if "crea una lista llamada" in rec:
                my_list = rec.replace("crea una lista llamada ", "")
            elif "crea una lista con el nombre" in rec:
                my_list = rec.replace("crea una lista con el nombre ", "")
            elif "crea una lista nueva con el nombre" in rec:
                my_list = rec.replace("crea una lista nueva con el nombre ", "")
            else:
                my_list = rec.replace("crea una nueva lista llamada ", "")

            # Check if it exists
            if my_list in name_files:
                while my_list in name_files:
                    talk(f"ya existe un archivo con el nombre {my_list}, dime otro nombre")
                    my_list = listen_light()

            # content
            talk(f"{my_list}, dime lo que quieres que ponga dentro")
            while True:
                content = listen_light()
                while not content:
                    content = listen_light()

                if content == "cancela":
                    talk("operación cancelada")
                    break

                Data.create(my_list, content)

                # add more content
                talk("listo, quieres agregar algo más?")
                while True:
                    choice = listen_light()
                    while not choice:
                        choice = listen_light()

                    if choice == "ok" or choice == "si":                
                        while choice == "si" or choice == "ok":
                            talk("te escucho") 

                            content = listen_light()
                            while not content:
                                content = listen_light() 

                            Data.add(my_list, content) 

                            talk("dato agregado, quieres agregar otro?")
                            choice = listen_light()
                            
                        if choice == "cancela":
                            talk("operación cancelada")
                            break
                        elif choice == "no":
                            talk("operación finalizada")
                            break
                        else: 
                            talk("no te he entendido, vuelve a intentarlo")
                        
                    elif choice == "cancela" or choice == "no":
                        talk("operación terminada")
                        break
                    else: 
                        talk("no te he entendido, vuelve a intentarlo")
                break


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
                talk("esa lista no existe, intenta de nuevo")
            else:
                talk("vale, te escucho")
                while True:
                    content = listen_light()
                    while not content:
                        content = listen_light()

                    if content == "cancela":
                        talk("operación cancelada")
                        break

                    Data.add(my_list, content)
                    
                    talk("dato agregado, quieres agregar otro?")
                    
                    while True:
                        choice = listen_light()
                        while not choice:
                            choice = listen_light()
                        
                        if choice == "ok" or choice == "si":
                            while choice == "si" or choice == "ok":
                                talk("te escucho") 
                                content = listen_light()

                                Data.add(my_list, content) 

                                talk("dato agregado, quieres agregar otro?")
                                choice = listen_light()
                            break
                        elif choice == "cancela":
                            talk("operación cancelada")
                            break
                        elif choice == "no":
                            talk("operación finalizada")
                            break
                        else: 
                            talk("no te he entendido, vuelve a intentarlo")
                    break


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
                talk("no tengo ninguna lista con ese nombre")
            else:
                talk(f"{my_list}, quieres borrarla completa o solo una parte?")
                while True:
                    choice = listen_light()

                    if choice == "completa" or choice == "completo":
                        Data.delete(my_list)

                    elif choice == "una parte" or choice == "solo una parte":
                        talk("ok, dime como empieza")
                        while True:
                            starts = listen_light()

                            while not starts:
                                starts = listen_light()
                            
                            # exit
                            if starts == "cancela" or starts == "cancelar":
                                talk("operacion cancelada")
                                break

                            exist = Data.update(my_list, starts)

                            if exist == False:
                                talk("no he conseguido ese dato dentro de la lista, vuelve a intentarlo")
                                while exist == False:
                                    starts = listen_light()
                                    
                                    exist = Data.update(my_list, starts)

                                    if exist == True:
                                        talk("eliminación completa")
                                        break
                                    else:
                                        talk("no he conseguido ese dato dentro de la lista, vuelve a intentarlo")

                                # exit
                                if exist == "cancela" or exist == "cancelar":
                                    talk("operación cancelada")
                                    break
                            else: 
                                talk("eliminacion completa")
                                break
                            break                    

                    elif choice == "cancela" or choice == "no":
                        talk("operación cancelada")
                    else:
                        talk("no te he entendido, vuelve a intentarlo")
                    break


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
                    talk("quieres que lo lea de nuevo?")
                    choice = listen_light()

                    if choice == "si" or choice == "ok":
                        Data.read(my_list)
                    elif choice == "no" or choice == "cancela":
                        talk("ok, saliendo")
                        break 
                    else:
                        talk("no te he entendido, intenta de nuevo")
            except FileNotFoundError:
                talk("no existe esa lista, intenta de nuevo")
            

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
        

        # Help
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

if __name__ == "__main__":
    Eve()
