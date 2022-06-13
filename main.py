import PySimpleGUI as sg
from music_player import MusicPlayer

sg.theme("Dark")   # Add a touch of color

layout = [
    [sg.Text("PyPlayer")],
    [sg.Input(enable_events=True, key='-SONG-'),
     sg.FileBrowse(file_types=(("All MP3 Files", "*.mp3"),))],
    [sg.Button("Play"), sg.Button("Pause"), sg.Button("Exit")]
]


window = sg.Window("PyPlayer", layout, debugger_enabled=True)
music_player = MusicPlayer()

while True:
    event, values = window.read()
    path = values["-SONG-"]
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Play":
        music_player.play(path)
    if event == "Pause":
        music_player.toggle_music()


window.close()
