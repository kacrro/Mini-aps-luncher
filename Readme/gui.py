import PySimpleGUI as sg

def readme_window():

    layout = [
        [sg.Text('Witaj w projekcie mini-aps-luncher – to zbiór mini-aplikacji desktopowych, które pozwolą eksplorować Pythona')],
                [sg.Text('\n Co znajdziesz w projekcie?', font=("Arial Black",10))],
        [sg.Text('- Converter – przeliczanie jednostek, np. kilometry na kroki.'
                '\n- Calculator – klasyczny kalkulator z podstawowymi operacjami.'
                # '\n- Hate Detection – detekcja obraźliwych treści przy użyciu modeli z Hugging Face.'
                '\n- QR Code Generator – generowanie kodów QR na podstawie wprowadzonego tekstu.')],
        [sg.Text('\n\n Technologie użyte w projekcie', font=("Arial Black",10))],
        [sg.Text('- PySimpleGUI – szybkie i proste tworzenie interfejsów graficznych.'
                '\n- Transformers & Hugging Face – praca z pretrenowanymi modelami NLP.'
                '\n- qrcode & Pillow – generowanie i przetwarzanie kodów QR.'
                '\n- Git – kontrola wersji i współpraca, dzięki czemu projekt jest stale rozwijany.'
                )],
        [sg.Button('Back')]
    ]

    window_readme = sg.Window('Mini-aps-luncher', layout)


    while True:
        event, values = window_readme.read()
        if event in (sg.WIN_CLOSED, 'Back') :
            break


    window_readme.close()