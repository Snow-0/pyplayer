import PySimpleGUI as sg
import os
from music_player import MusicPlayer

sg.theme("Default 1")

script_dir = os.path.dirname(__file__)
play_button = os.path.join(script_dir, "images/play.png")
pause_button = os.path.join(script_dir, "images/pause.png")

layout = [
    [sg.Text("PyPlayer")],
    [
        sg.Input(enable_events=True, key="SONG"),
        sg.FileBrowse(file_types=(("All MP3 Files", "*.mp3"),)),
    ],
    [
        sg.Button(
            key="Play", image_source=play_button, border_width=0, pad=((50, 15), (0, 0))
        ),
        sg.Button(
            key="Pause", image_source=pause_button, image_size=(25, 25),
            border_width=0, pad=((15, 30), (0, 0))
        ),
        sg.Slider(
            orientation="horizontal",
            pad=((0, 0), (0, 20)),
            key="VOLUME",
            range=(0, 10),
            default_value=5,
        ),
    ],
]


window = sg.Window("PyPlayer", layout, debugger_enabled=True, finalize=True)
music_player = MusicPlayer()

# get current volume when mouse is released
window["VOLUME"].bind("<ButtonRelease-1>", " Release")

while True:
    event, values = window.read()
    path = values["SONG"]
    volume = values["VOLUME"]
    if event == sg.WIN_CLOSED:
        break
    if event == "Play":
        music_player.play(path)
    if event == "Pause":
        music_player.toggle_music()
    if event == "VOLUME Release":
        music_player.set_volume(volume * 0.1)


window.close()
