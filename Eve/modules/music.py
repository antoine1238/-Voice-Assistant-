from urllib import parse, request
from pygame import mixer, time
import re
import os

# importacion de modulos
from .listen import listen, talk

# pygame init
mixer.init()

# My music path
path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.opus"

# Conditionals variables
quitar = ["cierra la música", "quita la música", "cancela"]
reanudar = ["play", "reanuda"]
pause = ["silencio", "pause", "pausa"]


def play():
    """ Music control """
    mixer.music.load(path)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(10)
        voz = listen()

        if quitar[0] in voz or quitar[1] in voz or quitar[2] in voz:
            mixer.music.stop() 
            return talk("musica quitada")

        if pause[0] in voz or pause[1] in voz or pause[2] in voz:
            mixer.music.pause()
            
            while True: 
                voz = listen()
                if pause[0] in voz or pause[1] in voz or pause[2] in voz:
                    if not mixer.music.get_busy():
                        talk("ya esta en pausa la musica")
                    else:
                        mixer.music.pause()

                if reanudar[0] in voz or reanudar[1] in voz:
                    mixer.music.unpause()

                if quitar[0] in voz or quitar[1] in voz or quitar[2] in voz:
                    mixer.music.stop() 
                    return talk("musica quitada")


def download_video(url_video):
    """ Download the video but in mp3 format """
    if "musica.opus" in os.listdir(path.replace("musica.opus", "")):
        os.remove(path)
    os.system(f"youtube-dl.exe -x {url_video}")

    
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

# main()