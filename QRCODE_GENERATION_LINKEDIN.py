import qrcode
from PIL import Image

data="https://www.linkedin.com/in/sasibhusana-b-b30956250/"

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=10,
                 border=4,)

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("VISIT_SASI_LINKEDIN_PROFILE.png")