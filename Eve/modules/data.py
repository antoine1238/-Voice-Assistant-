""" here is the logic behind creating tables with our VA """

from .listen import talk
import os

# My data path
path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/Data"

class Data:

    def create(name, content):
        files = os.listdir(path)
        for i in files:
            if i == f"{name}.csv":
                return talk("ya hay un archivo con ese nombre")

        file_csv = open(f"{path}/{name}.csv", "w")
        file_csv.write(f"{content}" + os.linesep)
        file_csv.close()

    def to_list():
        print("list")


    def delete():
        print("delete")


    def update():
        print("update")


# Data.create("antoine", "contenido en formato csv")
