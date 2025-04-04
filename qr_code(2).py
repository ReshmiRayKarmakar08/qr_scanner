import qrcode
from PIL import Image
#PIL (Pillow): Helps with image processing (used for saving the image).
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=24,border=4,)
#version=1: Controls the size of the QR code.

#error_correction=qrcode.constants.ERROR_CORRECT_H: Allows the QR code to be readable even if partially damaged.

#box_size=24: Each small square in the QR code will be 24 pixels wide.

#border=4: The QR code will have a 4-box-wide white border around it.
qr.add_data("https://in.pinterest.com/")
#qr.make(fit=True): Automatically adjusts the QR code size to fit the data.
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("pinterest_web.png")
