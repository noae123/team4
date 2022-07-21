from flask import Flask, redirect, Blueprint
from flask import url_for
from flask import render_template
from flask import request
from flask import session, jsonify
from datetime import timedelta
import mysql.connector
import requests

# homepage blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')

# Routes
@login.route('/login')
def index():
    return render_template('login.html')

@login.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='web-project-g4')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

#
# @login.route('/users')
# def users_func():
#         query = 'select * from users'
#         users_list = interact_db(query, query_type='fetch')
#         return render_template('users.html', users=users_list)

@login.route('/log-in', methods=['GET', 'POST'])
def login_func():
    if 'user_name' in request.args:
        user_name = request.args['user_name']
        user=next((item for item in customers if item['user_name'] == user_name), None)

        if request.args['user_name'] == "":
            return render_template('login.html',
                                   customers=customers)
        if user in customers:
            return render_template('login.html',
                                   user_name=user_name,
                                   user=user)
        else:
            return render_template('login.html',
                                    message='user not found')

    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user = next((item for item in customers if item['name'] == user_name), None)
        if user in customers:
            user_password = user['password']
            if user_password == password:
                session['user_name'] = user_name
                session['logedin'] = True
                return render_template('homepage.html',
                                       message2='Success Logged-in, ' + user_name,
                                       username=user_name)
            else:
                return render_template('login.html',
                                       message2='Wrong password!')
        else:
            return render_template('login.html',
                                    message2='The user dose not exist, Please sign in!')
    return render_template('login.html')

@login.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('index'))