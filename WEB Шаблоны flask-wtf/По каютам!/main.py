from flask import Flask
from flask import url_for
from flask import request, render_template, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def mission_():
    return render_template('base.html')


@app.route('/distribution')
def distribution():
    astronaut_list = ["Ридли Скотт", "Энди Уир", "Марк Уотни"]
    return render_template('distribution.html', astronaut_list=astronaut_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
