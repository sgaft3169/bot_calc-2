
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

def run_http_server():
    app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)

def start_server():
    server_thread = threading.Thread(target=run_http_server, daemon=True)
    server_thread.start()
