from flask import render_template

from app import app
import random

@app.route('/')
@app.route('/index')
def index():
    green = random.randint(0, 5000)
    orange = random.randint(0, 5000)
    blue = random.randint(0, 5000)
    return render_template('index.html', title='Home', blue_var=blue, green_var=green, orange_var=orange)
