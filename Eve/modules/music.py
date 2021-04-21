from urllib import parse, request
from pygame import mixer, time
import re
import os

# importacion de modulos
from .listen import listen, talk

# pygame init
mixer.init()

path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3"

def play():
    """ Music control """
    mixer.music.load(path)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(10)
        voz = listen()
        if "silencio" in voz or "pause" in voz:
            mixer.music.stop()


def download_video(url_video):
    """ Download the video but in mp3 format """
    if "musica.mp3" in os.listdir(path.replace("musica.mp3", "")):
        os.remove(path)
    os.system(f"youtube-dl.exe -x --audio-format mp3 {url_video}")

    
def find_url(search):
    """ we convert the search into a direct link to the first result """
    query = parse.urlencode({"search_query": search})
    html_content = request.urlopen("https://www.youtube.com/results?" + query)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    video = "https://www.youtube.com/watch?v=" + search_results[0] # Url final con el video buscado :)
    return video


def main():
    """ Execution control for test """
    search = input("que música quieres reproducir: ")
    url_video = find_url(search)
    download_video(url_video)
    play()
