from flask import Flask, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>La Fenasosa QR Code</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
                background-color: #f5f5f5;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            img {
                max-width: 90%;
                height: auto;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                background-color: white;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
    </head>
    <body>
        <h1>La Fenasosa QR Code</h1>
        <img src="/qr" alt="QR Code for La Fenasosa">
        <p>Scan to visit www.fenasosa.com</p>
    </body>
    </html>
    '''

@app.route('/qr')
def qr_code():
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data('https://www.fenasosa.com')
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to bytes buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
