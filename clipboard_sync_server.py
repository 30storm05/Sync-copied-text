
# clipboard_sync_server.py
from flask import Flask, request, jsonify
import pyperclip

app = Flask(__name__)

# Endpoint to receive clipboard content from iPhone
@app.route('/copy', methods=['POST'])
def copy_to_pc():
    data = request.json
    content = data.get('content', '')
    pyperclip.copy(content)  # Copy content to PC's clipboard
    return jsonify({'status': 'success', 'message': 'Copied to PC clipboard'})

# Endpoint to send clipboard content to iPhone
@app.route('/paste', methods=['GET'])
def paste_from_pc():
    content = pyperclip.paste()  # Get content from PC's clipboard
    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the server on all network interfaces
