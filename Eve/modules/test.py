# # you can ignore this. here I do experiments, it's very messy

from listen import listen, listen_light, talk, stop
# from data import Data, name_files
import os
path_data = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/Data"

# https://www.youtube.com/watch?v=EgBJmlPo8Xw
# import os

# os.system("youtube-dl.exe -x --audio-format mp3 --encoding UTF-8 https://www.youtube.com/watch?v=EgBJmlPo8Xw")

# from playsound import playsound
# playsound("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3")
   
# from pygame import *

# mixer.init()

# try:
#     mixer.music.load("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.m4a")
#     mixer.music.play()
#     print("m4a")
# except:
#     pass
    
# try:
#     mixer.music.load("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3")
#     mixer.music.play()
#     print("mp3")
# except:
#     mixer.music.load("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.opus")
#     mixer.music.play()
#     print("opus")

# while mixer.music.get_busy():
    # time.Clock().tick(10)


# C:/Users/antoi.DESKTOP-26ARF9V/Downloads/%(title)s.%(ext)s
# C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/%(title)s.%(ext)s


# from pydub import AudioSegment
 
# song = AudioSegment.from_mp3("musica.mp3")
# song.export("musica.ogg", format="ogg")


# Código que funcionó en LC
# youtube-dl.exe -x --audio-format mp3 https://www.youtube.com/watch?v=Ap-HeMIKi-c



# codigo de descarga que no funciona bien:
#  video_info = youtube_dl.YoutubeDL().extract_info(url=url_video, download=False)
    
#     # Opciones para la descarga del video
#     opciones = {
#     'format': 'bestaudio/best',
#     'outtmpl': "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.ogg", #Seteamos la ubicacion deseada
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }
#     # Descargar
#     with youtube_dl.YoutubeDL(opciones) as ydl:
#         ydl.download([url_video])
#         # if "musica.ogg" in os.listdir("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/"):
#         #     os.remove("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.ogg")

# string = "a partir de mañana todo estará mejor"
# text = string.split("mañana")[0]
# text_2 = string.split("mañana")[1]

# print(f"****** {text} ******")
# # print(f"****** {text_2} ******")


# import os

# archivos = os.listdir("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/")
# cancion = input("dime la cacion: ")
# for i in archivos:
#     archivos2 = i.split(".mp3")[0].split("(")[0]
#     if cancion in archivos2:
#         print(archivos2)

# import os

# search = input("dame nombre: ")
# path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3" 
# # new_path = f"C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/{search}.mp3" 
# # os.rename(path, new_path)

# files = os.listdir(path.replace("musica.mp3", ""))
# print(files)

# for i in files:
#     if i == f"{search}.mp3":
#         print("funciona")
#         break


# from listen import talk
# import wikipedia

# # lenguaje
# wikipedia.set_lang("es")

# # contenido resumido, dependiendo de el valor de sentences, este será mas o menos largo
# data = wikipedia.summary("coldplay", sentences=3)

# # mas especificos
# dat = wikipedia.page("Coldplay")
# title = dat.title
# url = dat.url
# content = dat.content
# links = dat.links

# print(data)

# import os 


# file_csv = open(f"{path}/antoine.csv", "w")
# file_csv.write("Primera línea" + os.linesep)
# file_csv.write("Segunda línea")
# file_csv.close()

# import os 

# files = []
# def files_in_dir():
#     search = os.listdir(path)
#     for i in search:
#         files.append(i)

# files_in_dir()

# print(files)

# f = open(f"{path_data}/naruto.csv", "r")
# data = f.read().replace("\n", "").split("-")[1:]
# borrado = input("que quieres borrar: ")
# lista = []

# for i in data:
#     if borrado == i:
#         print("borrado total")
#     elif borrado[:5] == i[:5]:
#         print(f"borrado completo de la lista {i}")
#     else:
#         print("nope..")
#         lista.append(i)

#     if lista == data:
#         print("no hemos conseguido la lista que mencionaste")

# print(data)
# print(lista)

# import threading
# import time
# import logging


# def daemon():
#     talk("Usar argumentos para identificar o nombrar el hilo es engorroso e innecesario. Usar argumentos para identificar o nombrar el hilo es engorroso e innecesario.Usar argumentos para identificar o nombrar el hilo es engorroso e innecesario.Usar argumentos para identificar o nombrar el hilo es engorroso e innecesario.")

# def non_daemon():
#     content = listen_light()
#     print(content)

# t = threading.Thread(name='non-daemon', target=non_daemon)
# t.start()
# daemon()
