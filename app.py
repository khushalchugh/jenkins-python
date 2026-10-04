from flask import Flask

app = Flask("MyServer")

@app.route('/')
def home_page():
    return "Hello! This is my python web server."

app.run(host ='0.0.0.0', port=5000)
