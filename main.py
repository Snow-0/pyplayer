import PySimpleGUI as sg
from music_player import MusicPlayer

sg.theme("Dark")  # Add a touch of color

layout = [
    [sg.Text("PyPlayer")],
    [
        sg.Input(enable_events=True, key="-SONG-"),
        sg.FileBrowse(file_types=(("All MP3 Files", "*.mp3"),)),
    ],
    [
        sg.Button("Play"),
        sg.Button("Pause"),
        sg.Button("Exit"),
        sg.Slider(
            orientation="horizontal",
            pad=((0, 0), (0, 20)),
            key="-VOLUME-",
            range=(0, 10),
            default_value=5,
        ),
    ],
]


window = sg.Window("PyPlayer", layout, debugger_enabled=True, finalize=True)
music_player = MusicPlayer()

# get current volume when mouse is released
window["-VOLUME-"].bind("<ButtonRelease-1>", " Release")

while True:
    event, values = window.read()
    path = values["-SONG-"]
    volume = values["-VOLUME-"]
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Play":
        music_player.play(path)
    if event == "Pause":
        music_player.toggle_music()
    if event == "-VOLUME- Release":
        music_player.set_volume(volume * 0.1)


window.close()
