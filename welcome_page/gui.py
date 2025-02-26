import PySimpleGUI as sg
import webbrowser
from mini_aps_menu.menu import main_menu

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

    readme_layout = [
        [sg.Text('Welcome to my aplication')],
        [sg.Text('It is one of my first full built apps. I made it just for '
                 'practice codin bc on studies I have never rly learnt codin '
                 'U could ask why python? - I want to explore AI world python loves AI')],
        # [sg.Text('practice codin bc on studies I have never rly learnt codin ')],
        # [sg.Text('U could ask why python? - I want to explore AI world python loves AI')],
        # [sg.Text('')],
        # [sg.Text('')],
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
            break


    window_welcome.close()

welcome_window()