from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
    return "Yes"
    return "hop in that foreign"
app.run(debug = True)