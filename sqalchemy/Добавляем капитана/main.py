from flask import Flask
from data import db_session
from data.__all_models import User
from data.__all_models import Jobs

app = Flask(__name__)
db_session.global_init("db/mars_explorer.db")
user = User()
user.surname = 'Scott'
user.name = 'Ridley'
user.age = 21
user.position = 'captain'
user.speciality = 'research engineer'
user.address = 'module_1'
user.email = 'scott_chief@mars.org'
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


