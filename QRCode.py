import qrcode

url = input("Enter the URL: ").strip()
file_path = "D:\\MainUser\\VSCode Project Files\\2. Personal VSCode Projects\\3. Extra Projects\\qrcode.png"

qr = qrcode.QRCODE()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code generated successfully!")