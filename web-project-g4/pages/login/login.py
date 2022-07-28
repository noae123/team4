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
    user_name=request.arg['user_name']
    password=request.arg['password']
    if (get_user_by_name()[1]):
        if(get_user_id_by_name_password(user_name, password)[1]):
            session['logedIn'] = True
            session['userId'] = get_user_id_by_name_password(user_name, password)[0]
            session['nickname'] = get_user_by_id(session['userId'])[1]
            session['email'] = get_user_by_id(session['userId'])[2]
            session['password']=get_user_by_id(session['userId'])[3]
            return redirect(url_for('profile.index'))

        else:
            massage="user name or password incorrect"
            return redirect(url_for('login.index', massage=massage))

    else:
        massage = "user name incorrect"
        return redirect(url_for('login.index',massage=massage))
#
# @login.route('/login', methods=['POST'])
# def try_login():
#     # print(request.form)
#     if (get_user_by_name(request.args['user_name'])[1]):
#         session['logedIn'] = True
#         session['userId'] = get_user_id_by_name(request.form['user_name'])[0]
#         session['nickname'] = request.args['nickname']
#         session['email'] = request.args['email']
#         return render_template('login.html')
#     else:
#         session['logedIn'] = False
#         return render_template('login.html',message='user not found')
#




        # if user_name == "":
        #     return render_template('login.html')
        #
        # if (get_user_by_name(request.form['user_name'])[1]):
        #     return render_template('login.html',
        #                            user_name=user_name,
        #                            user=user)
        # else:
        #     return render_template('login.html',
        #                            message='user not found')
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


    #if message == None:
    #return render_template('login.html')
    # else:
    #     return render_template('login.html', message=message)
    # return redirect(url_for('login.index'))