import PySimpleGUI as Sg
from calculator.gui import calculator_window
from converter.gui import converter_window
from qr_code.gui import qr_window

def main_menu():
    Sg.theme('DarkGrey2')
    layout = [
        [Sg.Button("Calculator", size=(20, 1))],
        [Sg.Button("Converter", size=(20, 1))],
        [Sg.Button("Qr code generator", size=(20, 1))],
        [Sg.Button("Exit", size=(20, 1))]

    ]

    window_menu = Sg.Window("Menu", layout)

    while True:
        event, values = window_menu.read()
        if event in (Sg.WINDOW_CLOSED, "Exit"):
            break
        elif event == "Converter":
            window_menu.hide()
            converter_window()
            window_menu.un_hide()

        elif event == "Calculator":
            window_menu.hide()
            calculator_window()
            window_menu.un_hide()

        elif event == "Qr code generator":
            window_menu.hide()
            qr_window()
            window_menu.un_hide()

main_menu()


