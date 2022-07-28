from flask import Blueprint, redirect
from flask import render_template, request, session, url_for
from utilities.db.users import get_user_by_name, get_user_id_by_name
import js2py
from tkinter import *
from tkinter import messagebox

# homepage blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')

@login.route('/login', methods=['GET'])
def index():
    # if message == None:
    return render_template('login.html')
    # else:
    #     return render_template('login.html', message=message)

@login.route('/login', methods=['POST'])
def try_login():
    print(request.form)
    if (get_user_by_name(request.form['user_name'])[1]): #todo wait to eden for another function
        session['logedIn'] = True
        #messagebox.showinfo("improve", "success") #todo english not good
        session['userId'] = get_user_id_by_name(request.form['user_name'])[1]
        return redirect(url_for('profile.index'))
    else:
        #print('faild')
        #messagebox.showinfo("fail", "not in") #todo english not good
        return redirect(url_for('login.index', message='user not found')) #todo think
        #url_for('published.create', VIDEO_ID=video_id)

    # if 'user_name' in request.args:
    #     user_name = request.args['user_name']
    #     user = next((item for item in customers if item['user_name'] == user_name), None)
    #
    #     if request.args['user_name'] == "":
    #         return render_template('login.html',
    #                                customers=customers)
    #     if user in customers:
    #         return render_template('login.html',
    #                                user_name=user_name,
    #                                user=user)
    #     else:
    #         return render_template('login.html',
    #                                message='user not found')
    # if request.method == 'POST':
    #     user_name = request.form['user_name']
    #     password = request.form['password']
    #     user = next((item for item in customers if item['name'] == user_name), None)
    #     if user in customers:
    #         user_password = user['password']
    #         if user_password == password:
    #             session['user_name'] = user_name
    #             session['logedin'] = True
    #             return render_template('homepage.html',
    #                                    message2='Success Logged-in, ' + user_name,
    #                                    username=user_name)
    #         else:
    #             return render_template('login.html',
    #                                    message2='Wrong password!')
    #     else:
    #         return render_template('login.html',
    #                                message2='The user dose not exist, Please sign in!')