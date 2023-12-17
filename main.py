import PySimpleGUI as sg

sg.theme("graygraygray")
sg.set_options(font="Calibre 14", button_element_size=(6, 3))
button_size = (6, 3)
button_size2 = (12, 3)
layout = [
    # [sg.Push(), sg.Text("Output", font="Calibre 30")],
    [sg.Text("Output", font="Calibre 30", expand_x=True, justification="right", pad=(20, 10))],
        [sg.Button("Clear", key="-CLEAR-", size=button_size2, expand_x=True), sg.Button("Enter", key="-ENTER-", size=button_size2, expand_x=True)],
    [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button("*", size=button_size)],
    [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button("/", size=button_size)],
    [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button("-", size=button_size)],
    [sg.Button(0, expand_x=True), sg.Button(".", size=button_size), sg.Button("+", size=button_size)],
]

window = sg.Window("Calculator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


window.close()
