import qrcode

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data('https://www.fenasosa.com')
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save('lafenasosa_qr.png')

print("QR code generated successfully and saved as 'lafenasosa_qr.png'")
