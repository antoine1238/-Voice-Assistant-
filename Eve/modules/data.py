""" here is the logic behind creating tables with our VA """

# modules
from .listen import say, listen_light

# python lib
import os
from pygame import mixer


# My data path
path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/Data"

# All files in my dir 
files = []
search = os.listdir(path)
for i in search:
    files.append(i)

# only name files
name_files = []
for i in files:
    name_files.append(i.replace(".csv", ""))


def main_data_create(my_list):
    # Check if it exists
    if my_list in name_files:
        while my_list in name_files:
            say(f"ya existe un archivo con el nombre {my_list}, dime otro nombre")
            my_list = listen_light()

    # content
    say(f"{my_list}, dime lo que quieres que ponga dentro")
    while True:
        content = listen_light()
        while not content:
            content = listen_light()

        if content == "cancela":
            say("operación cancelada")
            break

        Data.create(my_list, content)

        # add more content
        say("listo, quieres agregar algo más?")
        while True:
            choice = listen_light()
            while not choice:
                choice = listen_light()

            if choice == "ok" or choice == "si":                
                while choice == "si" or choice == "ok":
                    say("te escucho") 

                    content = listen_light()
                    while not content:
                        content = listen_light() 

                    Data.add(my_list, content) 

                    say("dato agregado, quieres agregar otro?")
                    choice = listen_light()
                    
                if choice == "cancela":
                    say("operación cancelada")
                    break
                elif choice == "no":
                    say("operación finalizada")
                    break
                else: 
                    say("no te he entendido, vuelve a intentarlo")
                
            elif choice == "cancela" or choice == "no":
                say("operación terminada")
                break
            else: 
                say("no te he entendido, vuelve a intentarlo")
        break


def main_data_add(my_list):
    say("vale, te escucho")
    while True:
        content = listen_light()
        while not content:
            content = listen_light()

        if content == "cancela":
            say("operación cancelada")
            break

        Data.add(my_list, content)
        
        say("dato agregado, quieres agregar otro?")
        
        while True:
            choice = listen_light()
            while not choice:
                choice = listen_light()
            
            if choice == "ok" or choice == "si":
                while choice == "si" or choice == "ok":
                    say("te escucho") 
                    content = listen_light()

                    Data.add(my_list, content) 

                    say("dato agregado, quieres agregar otro?")
                    choice = listen_light()
                break
            elif choice == "cancela":
                say("operación cancelada")
                break
            elif choice == "no":
                say("operación finalizada")
                break
            else: 
                say("no te he entendido, vuelve a intentarlo")
        break


def main_data_delete(my_list):
    say(f"{my_list}, quieres borrarla completa o solo una parte?")
    while True:
        choice = listen_light()

        if choice == "completa" or choice == "completo":
            Data.delete(my_list)

        elif choice == "una parte" or choice == "solo una parte":
            say("ok, dime como empieza")
            while True:
                starts = listen_light()

                while not starts:
                    starts = listen_light()
                
                # exit
                if starts == "cancela" or starts == "cancelar":
                    say("operacion cancelada")
                    break

                exist = Data.update(my_list, starts)

                if exist == False:
                    say("no he conseguido ese dato dentro de la lista, vuelve a intentarlo")
                    while exist == False:
                        starts = listen_light()
                        
                        exist = Data.update(my_list, starts)

                        if exist == True:
                            say("eliminación completa")
                            break
                        else:
                            talk("no he conseguido ese dato dentro de la lista, vuelve a intentarlo")

                    # exit
                    if exist == "cancela" or exist == "cancelar":
                        say("operación cancelada")
                        break
                else: 
                    say("eliminacion completa")
                    break
                break                    

        elif choice == "cancela" or choice == "no":
            say("operación cancelada")
        else:
            say("no te he entendido, vuelve a intentarlo")
        break


class Data:
    """ CRUD manager """

    def create(name, content):
        doc = open(f"{path}/{name}.csv", "w", encoding="utf-8")
        doc.write(f"-{content}" + os.linesep)
        doc.close()

    def to_list():
        number_files = len(files)
        try:
            mixer.music.set_volume(0.1)
            say(f"tienes un total de {number_files} archivos, cuyos nombres son:")
            for i in files:
                say(i.replace(".csv", ""))
            mixer.music.set_volume(0.5)
        except pygame.error:
            say(f"tienes un total de {number_files} archivos, cuyos nombres son:")
            for i in files:
                say(i.replace(".csv", ""))

    def add(name, content):
        doc = open(f"{path}/{name}.csv", "a", encoding="utf-8")
        doc.write(f"-{content}" + os.linesep)
        doc.close()

    def read(name):
        doc = open(f"{path}/{name}.csv")
        text = doc.read()
        try: 
            mixer.music.set_volume(0.1)
            say(text)
            mixer.music.set_volume(0.5)
        except pygame.error:
            say(text)
        doc.close()

    def delete(name):
        os.remove(f"{path}/{name}.csv")

    def update(name, starts):
        doc = open(f"{path}/{name}.csv", "r")
        text = doc.read().replace("\n", "").split("-")[1:]
        new_doc = []
        
        for i in text:
            if starts == i:
                pass
            elif starts[:15] == i[:15]:
                pass
            elif starts[:10] == i[:10]:
                pass
            elif starts[:5] == i[:5]:
                pass
            else:
                new_doc.append(i)

        doc.close()

        if text == new_doc:
            return False
        else: 
            Data.delete(name)
            for i in new_doc: 
                Data.add(name, i)

        return True       

