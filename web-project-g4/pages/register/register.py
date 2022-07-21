from flask import Flask, redirect, Blueprint
from flask import url_for
from flask import render_template
from flask import request
from flask import session, jsonify
from datetime import timedelta
import mysql.connector
import requests

# homepage blueprint definition
register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')


# Routes
@register.route('/register')
def index():
    return render_template('register.html')

@register.route('/session')
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

@register.route('/create_profile', methods=['POST'])
def create_profile():
    name = request.form['user_name']
    nickname = request.form['nickname']
    password = request.form['password']
    confirm_password = request.form['password']
    if confirm_password != password:
        session['password'] = False
        return render_template('register.html',
                               message2='The passwords do not match!')
    email = request.form['email']
    print(f'{name} {nickname} {password} {email}')
    query = "INSERT INTO customers(name, nickname, password, email) VALUES ('%s','%s', '%s', '%s')" % (name, nickname, password, email)
    interact_db(query=query, query_type='commit')
    #session['message'] = 'the inset of User: ' + name + 'succeeded'
    return redirect('/users')

