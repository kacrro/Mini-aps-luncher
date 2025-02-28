import PySimpleGUI as sg


def Hate_window():
    from transformers import pipeline
    # Mapa etykiet - do interpretacji wyników
    label_map = {
        "LABEL_0": "Non-toxic",
        "LABEL_1": "Toxic"
    }

    classifier = pipeline(
        "text-classification",
        model="ptaszynski/bert-base-polish-cyberbullying",
        tokenizer="ptaszynski/bert-base-polish-cyberbullying",
        # use_fast=False
    )

    layout = [
        [sg.Text('Write text to rate how toxic is it (polish):')],
        [sg.Multiline(key="input_text", size=(50,5))],
        [sg.Button('Analize'), sg.Push(),sg.Button('Back')],
        [sg.Text("", key="result_text",size=(40,1))],
    ]

    window_hate = sg.Window('Hate detection', layout)
    while True:
        event, values = window_hate.read()
        if event == 'Analize':
            input_text = values["input_text"].strip()
            if not input_text:
                sg.popup("Please enter text to analyze")
                continue
            result = classifier(input_text)

            top_result = result[0]
            raw_label = top_result["label"]
            score = top_result["score"]

            label_name=label_map.get(raw_label, raw_label)

            window_hate['result_text'].update(f"{label_name}: sure[%] : {score*100:.1f}%")


        elif event in (sg.WINDOW_CLOSED,'Back'):
            break
    window_hate.close()

