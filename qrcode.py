import qrcode
from PIL import Image

data = 'QR Code using make() function'
 
img = qrcode.make(data)
img.save('MyQRCode1.png')

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")
image.show()
