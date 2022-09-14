import http
import PySimpleGUI as sg
from requests import get

data = get("http://localhost:5000/userdata")


main_layout = [
    [
        sg.Listbox(
            values=[v["firstname"] + " " + v["lastname"] for v in data],
            size=(20, 15),
            key="valuesList",
        )
    ],
    [sg.Button("Einfügen") , sg.Button("Ändern")],
    [sg.Button("Löschen"), sg.Button("Schließen")],
]
main_window = sg.Window("LNW", layout=main_layout)