import pygame as py

py.mixer.init()


class MusicPlayer:
    def __init__(self):
        self.is_paused = False

    def play(self, path):
        py.mixer.music.load(path)
        py.mixer.music.play()
        print(py.mixer.music.get_pos())

    def toggle_music(self):
        if self.is_paused:
            py.mixer.music.unpause()
            self.is_paused = False

        else:
            py.mixer.music.pause()
            self.is_paused = True

    def set_volume(self, volume):
        py.mixer.music.set_volume(volume)
