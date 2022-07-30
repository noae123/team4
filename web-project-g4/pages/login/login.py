from flask import Blueprint, redirect
from flask import render_template, request, session, url_for
from utilities.db.users import get_user_by_name, get_user_id_by_name, get_user_id_by_name_password, get_user_by_id

# homepage blueprint definition
login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')

@login.route('/login', methods=['GET', 'POST'])
def index(massage=None):
    return render_template('login.html',massage=massage)

@login.route('/login_try', methods=['POST'])
def try_login():
    user_name=request.form['inputUserName']
    password=request.form['inputPassword']
    if (get_user_by_name(user_name)[1]):
        if(get_user_id_by_name_password(user_name, password)[1]):
            session['logedIn'] = True
            session['userId'] = get_user_id_by_name_password(user_name, password)[0]
            session['user_name']=get_user_by_id(session['userId'])[0]
            session['nickname'] = get_user_by_id(session['userId'])[1]
            session['email'] = get_user_by_id(session['userId'])[2]
            session['password']=get_user_by_id(session['userId'])[3]
            return redirect(url_for('profile.index'))

        else:
            massage="user name or password incorrect"
            print(massage)
            return redirect(url_for('login.index', massage=massage))

    else:
        massage = "user name incorrect"
        print(massage)
        return redirect(url_for('login.index',massage=massage))

