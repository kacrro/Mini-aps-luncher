import PySimpleGUI as Sg
from calculator.gui import calculator_window
from converter.gui import converter_window
from qr_code.gui import qr_window
from Hate_detect.gui import Hate_window

def main_menu():
    # Sg.theme('DarkGrey2')
    layout = [
        [Sg.Button("Calculator", size=(20, 1))],
        [Sg.Button("Converter", size=(20, 1))],
        [Sg.Button("Qr code generator", size=(20, 1))],
        [Sg.Button("Hate detector", size=(20, 1))],
        [Sg.Button("Back", size=(20, 1))]

    ]

    window_menu = Sg.Window("Menu", layout)

    while True:
        event, values = window_menu.read()
        if event in (Sg.WINDOW_CLOSED, "Back"):
            break



        elif event == "Converter":
            window_menu.hide()
            converter_window()
            window_menu.un_hide()

        elif event == "Calculator":
            window_menu.hide()
            calculator_window()
            window_menu.un_hide()

        elif event == "Hate detector":
            window_menu.hide()
            Sg.popup_no_wait("Please wait, it can take a moment.")
            Hate_window()
            window_menu.un_hide()

        elif event == "Qr code generator":
            window_menu.hide()
            qr_window()
            window_menu.un_hide()

    window_menu.close()


# main_menu()


