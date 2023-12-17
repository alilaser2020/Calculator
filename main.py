import PySimpleGUI as sg
from pgzero.loaders import sounds


def create_window(theme):
    """
    A method for update theme for calculator
    :param theme:
    :return:
    """
    sg.theme(theme)
    sg.set_options(font="Calibre 14", button_element_size=(6, 3))
    button_size = (6, 3)
    button_size2 = (12, 3)
    layout = [
        # [sg.Push(), sg.Text("Output", font="Calibre, 30")],
        [sg.Text("Output", font="Calibre 30", expand_x=True, justification="right", pad=(20, 10),
                 right_click_menu=theme_menu, key="-OUTPUT-")],
        [sg.Button("Clear", key="-CLEAR-", size=button_size2, expand_x=True), sg.Button("Enter", key="-ENTER-", size=button_size2, expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button("*", size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button("/", size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button("-", size=button_size)],
        [sg.Button(0, expand_x=True), sg.Button(".", size=button_size), sg.Button("+", size=button_size)]
    ]
    return sg.Window("calculater", layout)


current_num = []
full_operation = []
theme_menu = ["menu", ["dark", "Black", "BlueMono", "random"]]
win = create_window("Black")
while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        win.close()
        win = create_window(event)

    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_num.append(event)
        num_string = "".join(current_num)
        win["-OUTPUT-"].update(num_string)

    if event in ["*", "/", "-", "+"]:
        full_operation.append("".join(current_num))
        current_num = []
        full_operation.append(event)

    if event == "-ENTER-":
        full_operation.append("".join(current_num))
        result = eval("".join(full_operation))
        win["-OUTPUT-"].update(result)

    if event == "-CLEAR-":
        current_num = []
        full_operation = []
        win["-OUTPUT-"].update("")

win.close()
