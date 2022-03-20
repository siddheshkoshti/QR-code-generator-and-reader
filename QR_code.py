import pycode
from pybazar.pybazar import decode
from PIL import Image

qr = pyqrcode.create("My QR code")
qr.png("myQR.png", scale=8)

d = decode(image.open("myQR.png"))
print(d[0].data.decode("ascii"))