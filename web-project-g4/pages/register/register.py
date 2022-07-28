from flask import Blueprint, redirect
from flask import render_template, request, session, url_for
from utilities.db.users import get_user_by_name , create_user

# homepage blueprint definition
register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')

# Routes
@register.route('/register')
def index():
    return render_template('register.html')

@register.route('/register', methods=['GET'])
def try_register():
    print(request.form)
    if (create_user(request.form['user_name'], request.form['nickname'], request.form['password'], request.form['email'])[1]):
        #session['isRegister'] = True
        # session['userId'] = get_id_by_user(request.form['user_name'])[]  todo eden this function
        return redirect(url_for('login.index'))
    else:
        return redirect(url_for('register.index')) #todo think