""" here is the logic behind creating tables with our VA """

# modules
from .listen import talk

# python lib
import os

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


class Data:
    """ CRUD manager """

    def create(name, content):
        doc = open(f"{path}/{name}.csv", "w", encoding="utf-8")
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

