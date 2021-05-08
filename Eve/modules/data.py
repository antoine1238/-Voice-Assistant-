""" here is the logic behind creating tables with our VA """

# modules
from .listen import talk, listen_light

# python lib
import os

# My data path
path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/Data"

# All files in my dir 
files = []
search = os.listdir(path)
for i in search:
    files.append(i)


def files_in_dir(doc):
    """ check there is no other file with that name """
    if f"{doc}.csv" in files:
        return False
    return True

            
def main_data():
    """ Main loop"""
    while True:
        # rec = listen_light()
        rec = input("comand: ")

        if not rec:
            continue

        # CREATION
        if rec == "crear":
            talk("como se va a llamar la lista")
            name = listen_light()

            while not name:
                name = listen_light()

            # exit
            if name == "cancela" or name == "cancelar":
                talk("operacion cancelada")
                break

            # Check if it exists
            verify = files_in_dir(name)
            if verify == False:
                while verify == False:
                    talk(f"ya existe un archivo con el nombre {name}, intenta con otro")
                    name = listen_light()
                    verify = files_in_dir(name)
                                    

            talk(f"{name}. te parece bien el nombre?")

            # To change the name or continue
            while True:
                confirm = listen_light()    

                if confirm == "cancela":
                    talk("proceso cancelado")
                    break

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

            # verify that it has content
            while not content:
                talk("aun no has puesto contenido")
                content = listen_light()

            save = Data.create(name, content)
        
            talk("listo, quieres que lea tu lista?")

            # to read or continue
            while True:
                read = listen_light()

                if read == "si":
                    talk(f"{name}: {content}")
                    break
                elif read == "no":
                    break
                else: 
                    talk("no te he entendido, intenta de nuevo")
            break
        
        # LIST
        elif rec == "listar":
            Data.to_list()
            talk("que otra cosa quieres hacer con tus datos")

        # ADD
        elif rec == "agregar" or rec == "añadir":
            talk("dime la lista a la que le quieres agregar datos")
            while True:
                name = listen_light()

                if name == "cancela" or name == "cancelar":
                    talk("operacion cancelada")
                    break

                # Check if it exists 
                for i in files:
                    if name == i.replace(".csv", ""):
                        talk("listo, te escucho")
                        confirm = True
                        break
                    else:
                        confirm = False 
                
                # if it exists, ask the content and add it
                if confirm == True:
                    content = listen_light()
                    while not content:
                        content = listen_light()

                    Data.add(name, content)
                    talk("dato agregado, quieres que lea la lista?")

                    # Read or continue
                    while True:
                        read = listen_light()

                        if read == "si":
                            Data.read(name)
                            talk("quieres que lo lea de nuevo?")
                            while True:
                                choice = listen_light()
                                if choice == "si":
                                    Data.read(name)
                                elif choice == "no":
                                    return
                                else:
                                    talk("no te he entendido, intenta de nuevo")
                            
                        elif read == "no":
                            break
                        else:
                            talk("no te he entendido, intenta de nuevo")
                    break
                
                # if it doesn't exist
                else:
                    talk("no he encontrado el archivo que indicas")

        # READ 
        elif rec == "lectura" or rec == "leer un archivo" or rec == "leer archivo":
            talk("que archivo quieres revisar")
            name = listen_light()

            while not name:
                name = listen_light()
            
            # exit
            if name == "cancela" or name == "cancelar":
                talk("operacion cancelada")
                break
            
            for i in files:
                if name == i.replace(".csv", ""):
                    confirm = True
                    break
                else:
                    confirm = False 
            
            if confirm == True:
                Data.read(name)
                talk("quieres que lo lea de nuevo?")
                while True:
                    choice = listen_light()

                    # exit
                    if choice == "cancela" or choice == "cancelar":
                        talk("operacion cancelada")
                        break

                    if choice == "si":
                        Data.read(name)
                    elif choice == "no":
                        return
                    else:
                        talk("no te he entendido, intenta de nuevo")
            else:
                talk("ese archivo no existe, vuelve a intentarlo")
            

        # DELETE
        elif rec == "eliminar" or rec == "eliminación" or rec == "borrar" or rec == "borrado":   
            talk("vale, dime el nombre de la lista a eliminar") 

            while True:
                name = listen_light()

                while not name:
                    name = listen_light()

    
                for i in files:
                    if name == i.replace(".csv", ""):
                        confirm = True
                        break
                    else:
                        confirm = False 

                # exit
                if name == "cancela" or name == "cancelar":
                    talk("operacion cancelada")
                    return

                if confirm == True:
                    talk("quieres borrar la lista completa o sólo una parte")

                    while True:
                        choice = listen_light()

                        while not choice:
                            choice = listen_light()

                        # exit
                        if choice == "cancela" or choice == "cancelar":
                            talk("operacion cancelada")
                            return

                        # full erase
                        elif choice == "borrado completo" or choice == "borrar todo" or choice == "borrarlo todo" or choice == "completa":
                            Data.delete(name)
                            talk("la lista ha sido borrada")
                            return

                        # delete a part
                        elif choice == "borrar una parte" or choice == "borrar un pedazo" or choice == "una parte" or choice == "solo una parte":
                            talk("ok, dime como empieza")

                            while True:
                                starts = listen_light()

                                while not starts:
                                    starts = listen_light()


                                # exit
                                if starts == "cancela" or starts == "cancelar":
                                    talk("operacion cancelada")
                                    return
                                
                                exist = Data.update(name, starts)

                                if exist == False:
                                    talk("no he conseguido ese dato dentro de la lista, vuelve a intentarlo")
                                    while exist == False:
                                        starts = listen_light()

                                        exist = Data.update(name, starts)

                                        if exist == True:
                                            talk("eliminación completa")
                                            return
                                        
                                        else:
                                            talk("no he conseguido ese dato dentro de la lista, vuelve a intentarlo")

                                    # exit
                                    if exist == "cancela" or exist == "cancelar":
                                        talk("operacion cancelada")
                                        return
                                else: 
                                    talk("eliminacion completa")
                                return                                             
                        else:
                            talk("no te he entendido, vuelve a intentarlo")
                else:
                    talk("ese archivo no existe, vuelve a intentarlo")

        
        # HELP
        elif rec == "qué puedes hacer":
            talk("""
                1: crear una tabla con datos dentro, 
                2: añadir datos a una tabla existente, 
                3: listar datos de una tabla, 
                4: eliminar una un dato o toda la tabla si prefieres
            """)
        
        # QUIT
        elif rec == "cancela" or rec == "cancelar":
            talk("cancelando operación")
            break
        else:
            talk("no te he entendido, intenta de nuevo")




class Data:
    """ CRUD manager """

    def create(name, content):
        doc = open(f"{path}/{name}.csv", "w")
        doc.write(f"-{content}" + os.linesep)
        doc.close()

    def to_list():
        number_files = len(files)
        talk(f"tienes un total de {number_files} archivos, cuyos nombres son:")
        for i in files:
            talk(i.replace(".csv", ""))

    def add(name, content):
        doc = open(f"{path}/{name}.csv", "a", encoding="utf-8")
        doc.write(f"-{content}" + os.linesep)
        doc.close()

    def read(name):
        doc = open(f"{path}/{name}.csv")
        text = doc.read()
        talk(text)
        doc.close()

    def delete(name):
        os.remove(f"{path}/{name}.csv")

    def update(name, starts):
        doc = open(f"{path}/{name}.csv", "r")
        text = doc.read().replace("\n", "").split("-")[1:]
        new_doc = []
        
        for i in text:
            if starts == i:
                print(f"borrado total: {i}")
            elif starts[:15] == i[:15]:
                print(f"borrado por como empieza: {i}")
            elif starts[:10] == i[:10]:
                print(f"borrado por como empieza: {i}")
            elif starts[:5] == i[:5]:
                print(f"borrado por como empieza: {i}")
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


# main_data()