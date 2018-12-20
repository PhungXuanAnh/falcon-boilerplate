from app.model.user import User
from app import config
import uuid

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sqlalchemy

engine = create_engine(config.DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

user_req = {}

user_index = ['0', '2']

for i in user_index:
    user = User()
    user.username = 'test{}'.format(i)
    user.email = 'test{}@gmail.com'.format(i)
    user.password = '123-{}'.format(i)
    user.info = 'this is test user {}'.format(i)
    user.sid = str(uuid.uuid4())[0:8] + i
    user.token = 'token123-{}'.format(i)
    session.add(user)

session.commit()
