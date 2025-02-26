import PySimpleGUI as Sg

def calculator_window():
    layout = [
        [Sg.Input(key="display", disabled=True, font=("Helvetica", 20), justification="right", size=(13, 1))],
        [Sg.Button("7", size=(4, 2)), Sg.Button("8", size=(4, 2)), Sg.Button("9", size=(4, 2)), Sg.Button("/", size=(5, 2))],
        [Sg.Button("4", size=(4, 2)), Sg.Button("5", size=(4, 2)), Sg.Button("6", size=(4, 2)), Sg.Button("*", size=(5, 2))],
        [Sg.Button("1", size=(4, 2)), Sg.Button("2", size=(4, 2)), Sg.Button("3", size=(4, 2)), Sg.Button("-", size=(5, 2))],
        [Sg.Button(".", size=(4, 2)), Sg.Button("0", size=(4, 2)), Sg.Button("=", size=(4, 2)), Sg.Button("+", size=(5, 2))],
        [Sg.Button("Clear", size=(8, 1)), Sg.Push(), Sg.Button("Back", size=(8, 1))],
    ]
    window_calc = Sg.Window('Calculator', layout)
    current_display= ""

    while True:
        event, values = window_calc.Read()

        #close event
        if event in (Sg.WINDOW_CLOSED, "Back"):
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

    window_calc.close()