from flask import Flask
from data import db_session
from data.__all_models import User
from data.__all_models import Jobs
from data.__all_models import Department

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

job = Jobs()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.is_finished = False

departament = Department()
departament.title = 'Departament'
departament.chief = 1
departament.members = '0, 1'
departament.email = 'email@gmail.com'

db_sess = db_session.create_session()
db_sess.add(user)
db_sess.add(job)
db_sess.add(departament)
db_sess.commit()

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
