from flask import Blueprint, redirect
from flask import render_template, request, session, url_for
from utilities.db.users import get_user_by_name , create_user

# homepage blueprint definition
register = Blueprint('register', __name__, static_folder='static', static_url_path='/register', template_folder='templates')

# Routes
@register.route('/register')
def index():
    return render_template('register.html')

@register.route('/register/try_register', methods=['GET'])
def try_register():
    print(request.form)
    if('inputUserName' in request.args or 'inputNickname' in request.args or 'inputPassword'  in request.args or 'inputEmail' in request.args):
            password = request.args['inputPassword']
            print(password)
            confirm_password = request.args['inputConfirmPassword']
            print(confirm_password)
            user_name=request.args['inputUserName']
            Nickname=request.args['inputNickname']
            Email=request.args['inputEmail']
            if (confirm_password == password):
                if (create_user(user_name, Nickname, password,Email)[1]):
                    massage='user was created'
                    print(massage)
                    return render_template('login.html' ,massage=massage)
            else:
                massage = 'wrong password'
                print(massage)
                return render_template('register.html',massage=massage)


