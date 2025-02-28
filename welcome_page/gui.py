import PySimpleGUI as sg
import webbrowser
from mini_aps_menu.menu import main_menu
from Readme.gui import readme_window

def open_github():
    webbrowser.open_new_tab('https://github.com/kacrro')

def welcome_window():
    layout = [
        [sg.Text('Welcome to my aplication')],
        [sg.HorizontalLine()],
        [sg.Button('Mini Aps',size=(19,1) )],
        [sg.Button('GitHub',size=(19,1))],
        [sg.Button('What am I?',size=(19,1))],
        [sg.Button('Exit',size=(19,1))],
    ]



    window_welcome = sg.Window(' ', layout)



    while True:
        event, values = window_welcome.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Mini Aps':
            window_welcome.hide()
            main_menu()
            window_welcome.un_hide()
        elif event == 'GitHub':
            open_github()
            sg.Popup('Github opened in ur browser!')
        elif event == 'What am I?':
            window_welcome.hide()
            readme_window()
            window_welcome.un_hide()




    window_welcome.close()

welcome_window()