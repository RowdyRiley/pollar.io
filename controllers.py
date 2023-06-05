"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.url_signer import URLSigner
from .models import get_user_email
from py4web.utils.form import Form, FormStyleBulma

url_signer = URLSigner(session)

@action('index')
@action.uses('index.html', db, auth.user, url_signer)
def index():
    #get the id of the current user
    current_user_id = auth.current_user.get("id")
    #Get the zip code of the user
    user_state = db(db.userStates.user_id == current_user_id).select().first()

    #Check if there is a zipcode for the user 
    if user_state:
        #There is a zip_code code so just print the user zip
        print(user_state)
    else:
        #Otherwise go to the get zip action
        redirect(URL('get_zip')) 
    return dict(
        # COMPLETE: return here any signed URLs you need.
        my_callback_url = URL('my_callback', signer=url_signer),
        get_qa_url = URL('get_qa', signer=url_signer),
        get_state_url = URL('get_state', signer=url_signer),
    )

@action('get_zip', method=["GET", "POST"])
@action.uses('get_zip.html', db, url_signer, auth.user)
def get_zip():
    return dict(
        get_state_url = URL('get_state', signer=url_signer),
    )

@action("get_qa")
@action.uses(db, auth.user, url_signer.verify())
def get_qa():
    question_answer_database = db(db.qa).select().as_list()
    return dict(qa=question_answer_database)

@action("second_page")
@action.uses('second_page.html', db, auth.user, url_signer)
def second_page():
    question_answer_database = db(db.qa).select().as_list()
    return dict(qa=question_answer_database)

@action('get_state', method=["GET", "POST"])
@action.uses(db, url_signer, auth.user)
def get_state():
    stateName = request.json.get("stateName")
    db.userStates.insert(
            stateName = stateName,
        )
    redirect(URL('index')) 
    return "ok"