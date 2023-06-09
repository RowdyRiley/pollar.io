"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *
import random
from py4web.utils.populate import FIRST_NAMES, LAST_NAMES

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
    Field('user_id', 'reference auth_user'),
    Field('qa_id'),
    Field('answer_id'),
    Field('state'),
)

db.define_table(
    'userStates',
    Field('user_id', default=get_user_id),
    Field('stateName'),
)

db.commit()
def add_users_for_testing(num_users):
    # Test user names begin with "_".
    # Counts how many users we need to add.
    db(db.results).delete()
    db(db.auth_user.email.startswith("_")).delete()
    num_test_users = db(db.auth_user.email.startswith("_")).count()
    num_new_users = num_users - num_test_users
    print("Adding", num_new_users, "users.")
    for k in range(num_test_users, num_users):
        first_name = random.choice(FIRST_NAMES)
        last_name = first_name = random.choice(LAST_NAMES)
        username = "_%s%.2i" % (first_name.lower(), k)
        user = dict(
            email=username + "@ucsc.edu",
            first_name=first_name,
            last_name=last_name,
            password=username,  # To facilitate testing.
        )
        user_id = auth.register(user, send=False)['id']
        auth.register(user, send=False)
        # Adds some content for each user.
        for n in range(3):
            r = dict(
                user_id=user_id,
                qa_id=random.randint(1,50),
                answer_id=random.randint(1,4),
                stateName="California",
            )
            db.results.insert(**r)
    db.commit()
# Comment out this line if you are not interested.
add_users_for_testing(1)
# Comment out this line if you are not interested.'''