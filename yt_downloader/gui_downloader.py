import PySimpleGUI as sg
from dotenv import (
    load_dotenv,
)
import os


load_dotenv()
DIRECTORY_PATH = os.getenv("DIRECTORY_PATH")


def gui_download(downloader, theme="DarkRed1"):
    sg.theme(theme)

    layout = [
        [sg.Text("YouTube video url:"), sg.InputText(key="url", s=(25, 2))],
        [
            sg.Text("Directory path:"),
            sg.InputText(default_text=DIRECTORY_PATH, key="directory", s=(25, 2)),
            sg.FolderBrowse(),
        ],
        [
            sg.Text("Format:"),
            sg.Combo(["mp4", "mp3"], default_value="mp4", key="format"),
        ],
        [sg.Button("Download"), sg.Button("Exit")],
    ]

    window = sg.Window("YouTube Downloader", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Download":
            url = values["url"]
            directory_path = values["directory"]
            formatter = values["format"]

            try:
                downloader(url, directory_path, formatter)
                sg.popup("Successfully downloaded!")

            except Exception:
                sg.popup_error(f"Something has gone wrong. Try again")

        window.close()
