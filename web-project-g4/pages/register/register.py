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
    if (create_user(request.form['inputUserName'], request.form['inputNickname'], request.form['inputPassword'], request.form['inputEmail'])[1]):
        password = request.form['inputPassword']
        confirm_password = request.form['inputConfirmPassword']
        if (confirm_password == password):
            return render_template('login.html')
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')



