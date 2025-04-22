import qrcode 
# img = qrcode.make("https://chatgpt.com/")
# print(img.save("chatgpt.png"))

from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,box_size = 10, border=4,)

link = "https://chatgpt.com/"


qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="pink",back_color="blue")
print(img.save("link_qrcode.png"))