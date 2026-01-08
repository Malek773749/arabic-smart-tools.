from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password-check')
def password_check():
    return render_template('password-check.html')

@app.route('/password-generate')
def password_generate():
    return render_template('password-generate.html')

@app.route('/ip-info')
def ip_info():
    return render_template('ip-info.html')

if __name__ == '__main__':
    app.run(debug=True)
