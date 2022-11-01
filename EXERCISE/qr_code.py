import qrcode
import image

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=11,
        border=5
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(back_color="black", fill_color="white")
    img.save("wiki_img.png")


generate_qrcode("https://fr.wikipedia.org/wiki/Livre_des_morts_des_Anciens_%C3%89gyptiens")
