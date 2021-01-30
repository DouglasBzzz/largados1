import pyqrcode
import png
from pyqrcode import QRCode

qrstring = "https://www.linkedin.com/in/douglasbzz/"

url = pyqrcode.create(qrstring)

url.png(r'qr.png', scale=8)