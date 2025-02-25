import PySimpleGUI as sg

def calculator_window():
    layout = [
        [sg.Input(key="display", disabled=True, font=("Helvetica", 20), justification="right", size=(13,1))],
        [sg.Button("7", size=(4, 2)), sg.Button("8", size=(4, 2)), sg.Button("9", size=(4, 2)), sg.Button("/", size=(5, 2))],
        [sg.Button("4", size=(4, 2)), sg.Button("5", size=(4, 2)), sg.Button("6", size=(4, 2)), sg.Button("*", size=(5, 2))],
        [sg.Button("1", size=(4, 2)), sg.Button("2", size=(4, 2)), sg.Button("3", size=(4, 2)), sg.Button("-", size=(5, 2))],
        [sg.Button(".", size=(4, 2)), sg.Button("0", size=(4, 2)), sg.Button("=", size=(4, 2)), sg.Button("+", size=(5, 2))],
        [sg.Button("Clear", size=(8, 1)),sg.Push(),sg.Button("exit", size=(8, 1))],
    ]
    window_calc = sg.Window('Calculator', layout)
    current_display= ""

    while True:
        event, values = window_calc.Read()

        #close event
        if event in (sg.WINDOW_CLOSED, "exit"):
            break

        #make it clear
        elif event == "Clear":
            current_display = ""
            window_calc["display"].update(value=current_display)

        elif event == "=":
            try:
                result = str(eval(current_display))
                window_calc["display"].update(value=result)
                current_display = result
            except Exception:
                window_calc["display"].update(value="Error")
                current_display = ""
        else:
            current_display += event
            window_calc["display"].update(value=current_display)

calculator_window()