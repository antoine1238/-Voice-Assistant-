# importaciones de funciones
from modules.music import find_url, download_video, play
from modules.listen import listen, talk


def run():
    """ start """
    rec = listen()

    if "reproduce" in rec or "pon" in rec:
        if "reproduce" in rec:
            music = rec.replace("reproduce", "")
        else:
            music = rec.replace("pon", "")

        talk("Reproduciendo" + music)
        search = find_url(music)
        print(search)
        download_video(search)
        play()

run()