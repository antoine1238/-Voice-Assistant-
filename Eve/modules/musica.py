import youtube_dl
from urllib import parse, request
import re
from pygame import mixer, time
import os

# importacion de modulos
from listen import listen, talk

# pygame init
mixer.init()

path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3"

def play():
    mixer.music.load(path)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(10)
        voz = listen()
        if "silencio" in voz or "pause" in voz:
            mixer.music.stop()
            

def stop(): 
    mixer.music.stop()
    if "musica.mp3" in os.listdir(path.replace("musica.mp3", "")):
        os.remove(path)


def download_video(url_video):
    """ Descarga el video pero en formato mp3 """
    if "musica.mp3" in os.listdir(path.replace("musica.mp3", "")):
        os.remove(path)
    os.system(f"youtube-dl.exe -x --audio-format mp3 {url_video}")

    
def find_url(search):
    """ convertimos la busqueda en un enlace directo al primer resultado """
    query = parse.urlencode({"search_query": search})
    html_content = request.urlopen("https://www.youtube.com/results?" + query)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    video = "https://www.youtube.com/watch?v=" + search_results[0] # Url final con el video buscado :)
    return video


def main():
    search = input("que música quieres reproducir: ")
    url_video = find_url(search)
    download_video(url_video)
    play()


main()