from flask import Blueprint, redirect
from flask import render_template, request, session, url_for
from utilities.db.users import get_user_by_name , create_user
import js2py
from tkinter import *
from tkinter import messagebox

# homepage blueprint definition
register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')

# Routes
@register.route('/register')
def index():
    return render_template('register.html')

@register.route('/register', methods=['GET'])
def try_register():
    print(request.form)
    if (create_user(request.form['user_name'], request.form['user_nockname'], request.form['user_password'], request.form['user_email'])[1]):
        #session['isRegister'] = True
        #messagebox.showinfo("improve", "success") #todo english not good
        # session['userId'] = get_id_by_user(request.form['user_name'])[]  todo eden this function
        #print()
        return redirect(url_for('homepage.index'))
    else:
        #print('faild')
        #messagebox.showinfo("fail", "not in") #todo english not good
        return redirect(url_for('register.index')) #todo think
        #url_for('published.create', VIDEO_ID=video_id)


