"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_username():
    return auth.current_user.get('username') if auth.current_user else None

def get_user_id():
    return auth.current_user.get('id') if auth.current_user else None


def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

db.define_table(
    'qa',
    Field('answer1'),
    Field('answer2'),
    Field('answer3'),
    Field('answer4'),
    Field('question'),
)

db.define_table(
    'results',
    Field('qa_id', 'reference qa'),
    Field('user_id', default=get_user_id),
    Field('answer_id', 'integer', requires=IS_INT_IN_RANGE(1, 4)),
    Field('state'),
)

db.define_table(
    'userStates',
    Field('user_id', default=get_user_id),
    Field('stateName'),
)

db.commit()
