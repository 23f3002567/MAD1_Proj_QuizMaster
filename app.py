from flask import Flask,render_template
app = Flask(__name__)

app.config['SECRET_KEY']= 'e60b224224c50fb846f1b04b'

import models
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login')
def login():

    return render_template("login.html")
    

if __name__ == '__main__':
    app.run(debug=True)

