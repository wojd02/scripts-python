from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import ForeignKey

db = create_engine('sqlite:///Codecademy/unittest/projeto-teste/user.db')

Session = sessionmaker(bind=db)
session = Session()

base = declarative_base()

class User(base):
    __tablename__ = 'users'

    id = Column ('id', Integer, primary_key=True, autoincrement=True)
    user = Column ('user', String)
    password = Column ('password', String)
    email = Column ('email', String)
    phone = Column ('phone', Integer)
    status_admin = Column('status_admin', Boolean)

    def __init__(self, user, password, email, phone, status_admin = False):
        self.user = user
        self.password = password
        self.email = email
        self.phone = phone
        self.status_admin = status_admin

base.metadata.create_all(bind=db)

#CREATE USER
create_user = User(user = 'Ana Paula Soares', password = '!-03488@_', email = 'androidgirl@outlook.com', phone = '(13)2500-1312', status_admin = True)
session.add(create_user)
session.commit()
