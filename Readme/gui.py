import PySimpleGUI as sg

def readme_window():

    layout = [
        [sg.Text(
            'Welcome to the mini-aps-luncher project – it is a collection of desktop mini-applications that allow you to explore Python')],
        [sg.Text('\nWhat will you find in the project?', font=("Arial Black", 10))],
        [sg.Text('- Converter – unit conversion, e.g., kilometers to steps.'
                 '\n- Calculator – a classic calculator with basic operations.'
                 '\n- Hate Detection – detecting offensive content using models from Hugging Face.'
                 '\n- QR Code Generator – generating QR codes based on the entered text.')],
        [sg.Text('\n\nTechnologies used in the project', font=("Arial Black", 10))],
        [sg.Text('- PySimpleGUI – fast and easy creation of graphical interfaces.'
                 '\n- Transformers & Hugging Face – working with pre-trained NLP models.'
                 '\n- qrcode & Pillow – generating and processing QR codes.'
                 '\n- Git – version control and collaboration, ensuring the project is constantly evolving.'
                 )],

        [sg.Button('Back')]
    ]

    window_readme = sg.Window('Mini-aps-luncher', layout)


    while True:
        event, values = window_readme.read()
        if event in (sg.WIN_CLOSED, 'Back') :
            break


    window_readme.close()