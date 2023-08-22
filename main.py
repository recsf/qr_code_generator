import qrcode

data = input("Enter the Data: ")
version = int(input("Enter the version (complexity): "))
box_size = int(input("Enter the box size: "))

# Creating an instance of QRCode class
qr = qrcode.QRCode(version, box_size, border=5)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

f = input("name: ")
img.save("{}.png".format(f))
print('qr code generated and saved in the gallery')
