import PySimpleGUI as Sg
import qrcode
import io

def generate_qr_code(data, save_path=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if save_path:
        img.save(save_path)
    return img


def qr_window():
    layout=[
        [Sg.Text('Write what you want to code as QR:')],
        [Sg.Multiline(key='input_text', size=(40, 5))],
        [Sg.Button('Generate'),Sg.Button('Save into file', disabled=True, key='saving_button' ), Sg.Push() ,Sg.Button('Back')],
        [Sg.Text('', key='QR_Preview')],
        [Sg.Image(key='QR_Image')],
    ]

    window_qr=Sg.Window("QR Code Generator", layout)

    while True:
        event, values = window_qr.read()
        if event in (Sg.WIN_CLOSED,"Back"):
            break
        if event == 'Generate':
            window_qr['saving_button'].update(disabled=False)
            window_qr['QR_Preview'].update('Preview of QR:')
            data = values['input_text'].strip()
            if not data:
                Sg.popup("Please enter your text!")
                continue
            qr_img = generate_qr_code(data)

            bio = io.BytesIO()
            qr_img.save(bio, format="png")
            window_qr['QR_Image'].update(data=bio.getvalue())

        elif event == 'saving_button':
            if qr_img is None:
                Sg.popup("Please enter your text!")
                continue
            save_path = Sg.popup_get_file("Save into file", save_as=True, no_window=True, file_types=(("PNG Files","*.png"),))

            if save_path:
                qr_img.save(save_path)
                Sg.popup("File has been saved successfully!")

    window_qr.close()