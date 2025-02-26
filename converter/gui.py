import PySimpleGUI as Sg


def converter_window():

    layout = [
        [Sg.Text('Steps and Kilometers Converter', font=("Helvetica", 14)), Sg.Text('(use . in floats)', font=("Helvetica", 9))],
        [Sg.Text('Amount:'), Sg.InputText(key='amount', size=(35, 1))],
        [Sg.Button('Km -> Steps'), Sg.Button('Steps -> Km'), Sg.Button('Back')],
        [Sg.Text('This is '), Sg.Text('0', key='amount_view'), Sg.Text('', key='steps_km_view')]
    ]

    window_convert = Sg.Window("Converter", layout)

    def convertin_km_to_steps(amount):
        return amount*1400

    def convertin_steps_to_km(amount):
        return amount/1400

    while True:
        event, values = window_convert.read()
        if event in (Sg.WINDOW_CLOSED, 'Back'):
            break
        try:
            amount = float(values['amount'])
            if event == 'Km -> Steps':
                result = convertin_km_to_steps(amount)
                window_convert['amount_view'].update(result)
                window_convert['steps_km_view'].update('Steps')

            elif event == 'Steps -> Km':
                result = convertin_steps_to_km(amount)
                window_convert['amount_view'].update(result)
                window_convert['steps_km_view'].update('Km')

        except ValueError:
            window_convert['amount_view'].update('    ERROR   ')
            window_convert['steps_km_view'].update('------------')
            Sg.Popup('ERROR', 'Please enter a correct number!')

    window_convert.close()