import qrcode

url = input("Enter the URL: ").strip()
file_path = (ex: "C:\\Users\\HP\\Desktop\\qrcode.png")

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save(file_path)

print("QR Code generated successfully!")
