from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return open("index.html").read()

@app.route('/contact', methods=['POST'])
def contact():
    return "Message Sent Successfully!"

app.run(host='0.0.0.0', port=5000)
