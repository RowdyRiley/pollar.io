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
from .models import get_user_email, update_qa_id
from py4web.utils.form import Form, FormStyleBulma

url_signer = URLSigner(session)

#This is the question id that is currently being seen by all users.
current_question_id = 1

#This is the maximum number of questions
max_questions = 4

@action('index')
@action.uses('index.html', db, auth.user, url_signer)
def index():
    stateName = request.params.get("stateName")
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
        redirect(URL('get_state'))
    return dict(
        # COMPLETE: return here any signed URLs you need.
        my_callback_url = URL('my_callback', signer=url_signer),
        get_qa_url = URL('get_qa', signer=url_signer),
        get_state_url = URL('get_state', signer=url_signer),
        submit_answer = URL('submit_answer', signer=url_signer),
        get_next_question_url = URL('get_next_question', signer=url_signer),
    )

@action("get_qa")
@action.uses(db, auth.user, url_signer.verify())
def get_qa():
    global current_question_id
    global max_questions
    #Select all of the questions from the database and return it.
    question_answer_database = db(db.qa.id==current_question_id).select().as_list()
    # question_answer_database = db(db.qa).select().first()
    return dict(qa=question_answer_database)

@action("get_next_question")
@action.uses(db, auth.user, url_signer.verify())
def get_next_question():
    # print("INCREMENTING QUESTION ID")

    #Must define global variable within the function when using global variables
    global current_question_id

    #If the current_question_id is less than the maximum number of questions, set the current_question_id to the next question in the database
    if(current_question_id < max_questions):
        current_question_id = current_question_id + 1
        update_qa_id(current_question_id)
        return "ok"

    #If the current_question_id is the last question set the current_question_id to be 1 (works like a circular array)
    if(current_question_id >= max_questions):
        current_question_id = 1
        update_qa_id(current_question_id)
        return "ok"

@action("second_page")
@action.uses('second_page.html', db, auth.user, url_signer)
def second_page():
    #get the id of the current user
    current_user_id = auth.current_user.get("id")
    current_user_stateName_database = db(db.userStates.user_id == current_user_id).select().first()
    current_user_stateName = current_user_stateName_database.stateName

    #Get results database and all the ones from current user statename and make sure qa id is the same as the one he answered.
    results_database = db((db.results.state == current_user_stateName) &
                          (db.results.qa_id == current_question_id)).select().as_list()
    #Afterwards do math from the answer ids. 
    a1_count = 0
    a2_count = 0
    a3_count = 0
    a4_count = 0
    for r in results_database:
        if r['answer_id'] == 1:
            a1_count += 1
        if r['answer_id'] == 2:
            a2_count += 1
        if r['answer_id'] == 3:
            a3_count += 1
        if r['answer_id'] == 4:
            a4_count += 1
    #Then return math.
    return dict(
        a1_count=a1_count,
        a2_count=a2_count,
        a3_count=a3_count,
        a4_count=a4_count,
        current_user_stateName=current_user_stateName,
    )

@action('get_state')
@action.uses('get_state.html', db, url_signer, auth.user)
def get_state():
    #This is doing the same thing as index because we have two js files. 
    return dict(
        get_state_url = URL('insert_state', signer=url_signer),
    )

@action('insert_state', method="POST")
@action.uses(db, url_signer.verify(), auth.user)
def get_state():
    #Gets the stateName from the js and then inserts it into the database.
    stateName = request.json.get("stateName")
    newState = db.userStates.insert(
            stateName = stateName,
        )
    #Right now index is not being redirected.    
    return dict(new_url=URL('index', vars=dict(stateName=stateName)))

@action('submit_answer', method="POST")
@action.uses(db, url_signer.verify(), auth.user)
def submit_answer():
    user_id = auth.get_user()['id']
    qa_id = request.json.get("qa_id")
    answer_id = request.json.get("answer_id")
    user_state = db(db.userStates.user_id == user_id).select().first()
    if user_state:
        state_name = user_state.stateName
        db.results.insert(
            user_id=user_id,
            qa_id=qa_id,
            answer_id=answer_id,
            state=state_name,
        )
    return "OK"