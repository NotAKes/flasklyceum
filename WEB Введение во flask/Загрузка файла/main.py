from flask import Flask
from flask import url_for
from flask import request, send_file

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    list_of_promotion = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся']
    return '</br>'.join(list_of_promotion)


@app.route('/promotion_image')
def image():
    return f"""<!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
       <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles.css')}"/>
        <title>Привет, Марс!</title>
      </head>
      <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='img/mars.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
        <div class="alert alert-primary" role="alert">
          Человечество вырастает из детства.
        </div>
        <div class="alert alert-secondary" role="alert">
          Человечеству мала одна планета.
        </div>
        <div class="alert alert-success" role="alert">
          Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-danger" role="alert">
          И начнем с Марса!
        </div>
        <div class="alert alert-warning" role="alert">
         Присоединяйся!
        </div>
      </body>
    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='styles.css')}" />
                            <title>Отбор космонавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента<br> на участие в миссии</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="get_image">
                                </div>
                                <div class="img">
                                    <img src="{url_for('static', filename='img/image.jpg')}" 
                                               alt="здесь должна была быть картинка, но не нашлась">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                    
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['get_image']
        print(f.save('static/img/image.jpg'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


