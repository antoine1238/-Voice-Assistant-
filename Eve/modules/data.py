""" here is the logic behind creating tables with our VA """

from .listen import talk, listen_light
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
        rec = listen_light()

        if not rec:
            continue

        # CREATION
        if rec == "crear":
            talk("como se va a llamar la lista")
            name = listen_light()

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
                    return talk("proceso cancelado")

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
                confirm = False

                # Check if it exists 
                for i in files:
                    if name == i.replace(".csv", ""):
                        talk("listo, te escucho")
                        confirm = True
                        break
                    else:
                        pass
                
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
                            talk("leyendo :s")
                            break
                        elif read == "no":
                            break
                        else:
                            talk("no te he entendido, intenta de nuevo")
                    break
                
                # if it doesn't exist
                else:
                    talk("no he encontrado el archivo que indicas")

        # DELETE
        elif rec == "eliminar":
            pass

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
        file_csv = open(f"{path}/{name}.csv", "w")
        file_csv.write(f"{content}" + os.linesep)
        file_csv.close()

    def to_list():
        number_files = len(files)
        talk(f"tienes un total de {number_files} archivos, cuyos nombres son:")
        for i in files:
            talk(i.replace(".csv", ""))

    def add(name, content):
        save = open(f"{path}/{name}.csv", "a", encoding="utf-8")
        save.write(content + os.linesep)
        save.close()

    def delete():
        print("delete")


    def update():
        print("update")


# main_data()