from textwrap import fill
import qrcode
import image

url=input("Enter your link: ")

qr=qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5

)

data=("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color = "white")

print("Generating QR code.....")

img.save("test.png")
