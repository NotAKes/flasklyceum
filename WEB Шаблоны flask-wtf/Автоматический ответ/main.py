from flask import Flask
from flask import url_for
from flask import request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def mission_(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>/')
def mission(prof):
    return render_template('training.html', prof=prof)


@app.route('/')
@app.route('/list_prof/<list>/')
def list_of_prof(list):
    prof_list = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
                 'климатолог', 'гляциолог', 'астрогеолог', 'метеоролог', 'штурман']
    return render_template('list_of_prof.html', prof_list=prof_list, list_type=list)


@app.route('/answer/')
@app.route('/auto_answer/')
def answer():

    dicts = {'title': 'Анкета',
            'surname': 'Watny',
            'name': 'Mark',
            'education': 'выше среднего',
            'profession': 'штурман марсохода',
            'sex': 'male',
            'motivation': 'Всегда мечтал застарять на Марсе!',
            'ready': 'True'}
    return render_template('auto_answer.html', **dicts)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')