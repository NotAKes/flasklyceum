from flask import Flask

app = Flask(__name__)
global_init(input())
db_sess = create_session()
for departament in db_sess.query(Departament).filter(Departament.id == 1).all():
    for member in departament.members:
        work_size = 0
        for job in db_sess.query(Jobs).all():
            if str(member) in job.collaborators:
                work_size += job.work_size
        if job > 25:
            print(member.name, member.surname)