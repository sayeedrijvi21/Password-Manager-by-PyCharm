from flask import Flask, request, jsonify, render_template
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

def load_key():
    return open("key.key", "rb").read()

key = load_key()
fer = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def view():
    passwords = []
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                passwords.append({"user": user, "password": fer.decrypt(passw.encode()).decode()})
    return jsonify(passwords)

@app.route('/add', methods=['POST'])
def add():
    name = request.json.get('name')
    pwd = request.json.get('password')
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    return jsonify({"message": "Password added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
