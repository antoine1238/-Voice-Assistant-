# you can ignore this


# from pygame import *

# mixer.init()
# mixer.music.load("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica3.mp3")
# mixer.music.play()

# while mixer.music.get_busy():
#     time.Clock().tick(10)

import os

os.system("youtube-dl.exe -x  https://www.youtube.com/watch?v=5skBr_96dPc&list=RD5skBr_96dPc&")
   


# from playsound import playsound
# playsound("C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica3.mp3")

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
# print(f"****** {text_2} ******")
