from flask import Flask,render_template
app = Flask(__name__)
app.config['SECRET_KEY']= 'e60b224224c50fb846f1b04b'

import models,routes
    

if __name__ == '__main__':
    app.run(debug=True)

