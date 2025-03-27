from flask import Flask

app = Flask(__name__)
global_init(input())
db_sess = create_session()
for departament in db_sess.query(Department).filter(Department.id == 1).all():
    for member in departament.members.split(', '):
        work_size = 0
        for job in db_sess.query(Jobs).all():
            if int(member) in list(map(int, job.collaborators.split(', '))):
                work_size += int(job.work_size)
        if work_size > 25:
            worker = db_sess.query(User).filter(User.id == int(member)).all()[0]
            print(worker.name, worker.surname)