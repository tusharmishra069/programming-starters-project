import pyqrcode
import png
from pyqrcode import QRCode

#put link here 
s = "your_link"

#Gentrate qr code 
url = pyqrcode.create(s)

#Create and save the svg file 
url.svg("myqr.svg",scale=8)

#Create and save the svg file 
url.png("myqr.png",scale=8)
