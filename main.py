from flask import Flask
from data import db_session
from data.users import User

import os
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = '123'
    db_sess.add(user)
    user2 = User()
    user2.surname = "Hopkins"
    user2.name = "James"
    user2.age = 37
    user2.position = "captain"
    user2.speciality = "doctor"
    user2.address = "module_2"
    user2.email = "james_hopkins@mars.org"
    user2.hashed_password = '123'
    db_sess.add(user2)
    user3 = User()
    user3.surname = "Peterson"
    user3.name = "Louis"
    user3.age = 21
    user3.position = "captain"
    user3.speciality = "builder"
    user3.address = "module_3"
    user3.email = "louis_peterson@mars.org"
    user3.hashed_password = '123'
    db_sess.add(user3)
    db_sess.commit()

    # port = int(os.environ.get("PORT", 8080))
    # app.run(host='127.0.0.1', port=port)


if __name__ == '__main__':
    main()
