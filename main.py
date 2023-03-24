from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

import os
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    add_user(db_sess, "Scott", "Ridley", 21, "captain", "research engineer",
             "module_1", "scott_chief@mars.org", '123')
    add_user(db_sess, "Hopkins", "James", 37, "captain", "doctor",
             "module_2", "james_hopkins@mars.org", '123')
    add_user(db_sess, "Peterson", "Louis", 21, "captain", "builder",
             "module_3", "louis_peterson@mars.org", '123')

    # port = int(os.environ.get("PORT", 8080))
    # app.run(host='127.0.0.1', port=port)


def add_job(session, leader_id, job_task, work_size, collaborators, start_date, is_finished):
    job = Jobs()
    job.team_leader = leader_id
    job.job = job_task
    job.work_size = work_size
    job.collaborators = collaborators
    job.start_date = start_date
    job.is_finished = is_finished
    session.add(job)
    session.commit()


def add_user(session, surname, name, age, position, speciality, address, email, hashed_password):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    user.hashed_password = hashed_password
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
