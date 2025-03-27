from flask import Flask
from flask import url_for
from flask import request, render_template, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def mission_():
    return render_template('base.html')


@app.route('/table_param/<sex>/<age>')
def distribution(sex, age):
    return render_template('table.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
