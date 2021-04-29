from urllib import parse, request
from pygame import mixer, time
import re
import os

# importacion de modulos
from .listen import listen, talk

# My music path
path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3"

# Conditionals variables
close = ["cierra la música", "quita la música", "cancela"]
resume = ["play", "reanuda"]
pause = ["silencio", "pause", "pausa"]

def play_in_dir(search):
    files = os.listdir(path.replace("musica.mp3", ""))
    for music in files:
        if music == f"{search}.mp3":
            play(search)
            return True
    return False


def play(search):
    """ Music control """
    mixer.init()
    mixer.music.load(path.replace("musica.mp3", f"{search}.mp3"))
    mixer.music.set_volume(0.3)
    mixer.music.play()

    while mixer.music.get_busy():
        time.Clock().tick(10)
        while True:
            voz = listen()
            # voz = input("comando while: ")

            if pause[0] in voz or pause[1] in voz or pause[2] in voz:
                if not mixer.music.get_busy():
                    talk("ya esta en pausa la música")
                else:
                    mixer.music.pause()

            elif resume[0] in voz or resume[1] in voz:
                if mixer.music.get_busy():
                    talk("ya esta sonando la música")
                else:
                    mixer.music.unpause()    
            
            elif close[0] in voz or close[1] in voz or close[2] in voz:
                mixer.music.stop() 
                mixer.quit()
                return talk("musica quitada")



def download_video(url_video, search):
    """ Download the video but in mp3 format """
    os.system(f"youtube-dl.exe -x --audio-format mp3 {url_video}")

    # Rename file
    path = "C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/musica.mp3" 
    new_path = f"C:/Users/antoi.DESKTOP-26ARF9V/OneDrive/Escritorio/AV Eve/Eve/music/{search}.mp3" 
    os.rename(path, new_path)


    
def find_url(search):
    """ we convert the search into a direct link to the first result """
    query = parse.urlencode({"search_query": search})
    html_content = request.urlopen("https://www.youtube.com/results?" + query)
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    video = "https://www.youtube.com/watch?v=" + search_results[0] # Url final con el video buscado :)
    return video


def main():
    """ Execution control for test """
    print("main")
    search = input("que música quieres reproducir: ")
    music_file = play_in_dir(search)

    if music_file == True:
        return 
    else:
        url_video = find_url(search)
        download_video(url_video, search)
        play(search)

# main()