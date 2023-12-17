import PySimpleGUI as sg


def create_window(theme):
    """
    A method for determine and create a new window for calculator
    :param theme:
    :return:
    """
    sg.theme(theme)
    sg.set_options(font="Calibre 14", button_element_size=(6, 3))
    button_size = (6, 3)
    button_size2 = (12, 3)
    layout = [
        # [sg.Push(), sg.Text("Output", font="Calibre 30")],
        [sg.Text("Output", key="-OUTPUT-", font="Calibre 30", expand_x=True, justification="right", pad=(20, 10), right_click_menu=theme_menu)],
        [sg.Button("Clear", key="-CLEAR-", size=button_size2, expand_x=True), sg.Button("Enter", key="-ENTER-", size=button_size2, expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button("*", size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button("/", size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button("-", size=button_size)],
        [sg.Button(0, expand_x=True), sg.Button(".", size=button_size), sg.Button("+", size=button_size)],
    ]
    return sg.Window("Calculator", layout)


current_num = []
theme_menu = ["menu", ["Black", "dark", "BlueMono", "random"]]
window = create_window("Black")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
        current_num = []

    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_num.append(event)
        window["-OUTPUT-"].update("".join(current_num))

window.close()
