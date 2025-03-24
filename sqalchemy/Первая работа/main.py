from flask import Flask

app = Flask(__name__)
global_init(input())
db_sess = create_session()
for user in db_sess.query(User).filter(User.address == "module_1", User.age < 21).all():
    user.address = 'module_3'
db_sess.commit()