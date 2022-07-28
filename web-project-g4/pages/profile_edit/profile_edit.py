from flask import Blueprint, render_template, session, url_for, redirect, request
from utilities.db.users import get_user_by_id, update_user, delete_user

# homepage blueprint definition
from utilities.db.videos import get_all_videos

profile_edit = Blueprint('profile_edit', __name__, static_folder='static', static_url_path='/profile_edit', template_folder='templates')


# Routes
@profile_edit.route('/profile_edit' ,defaults={'userid':-1}) #user must come from session
@profile_edit.route('/profile/<int:userid>')
def index(userid):
    rout_userID = userid
    session["logedIn"] = True
    # and rout_userID == session['userid']
    if ("userid" in session and session['logedIn'] == True ):
        # if(VIDEO_ID == None):
        video_info = {
            'audio': url_for('audio_player.static', filename='media/music/happybday.mp3'),
            'img': url_for('audio_player.static', filename='media/img/Black.png'),
            'sender_name': 'Sender Name',
            'card_banner': 'Card Banner',
            'color': 'white',
            'shape': 'circle',
            'dir': False
        }
        #todo check if work after login page is ready

        # user_name = session['user_name']
        # nickname = session['nickname']
        # password = session['password']
        # email = session['email']
        user_name = get_user_by_id(5)[0]
        nickname = get_user_by_id(5)[1]
        password = get_user_by_id(5)[3]
        email = get_user_by_id(5)[2]
        # else go to the db and get me the video

        # make this to some kind of string
        VIDEO_ID = 'p' + str(0) #need to change and give here a list of videos
        return render_template('profile_edit.html', video_id=VIDEO_ID, video_info=video_info,user_name=user_name, nickname=nickname,password=password,email=email,update=True)
    # else:
    #     return redirect(url_for('login.index')) #todo send massage 'you need to log in'


@profile_edit.route('/update_profile') #user must come from session
def update_profile():
    # id=session['userID'] #todo check if work after login page is ready
    user_name = request.form['inputUserName']
    nickname = request.form['inputNickname']
    password = request.form['inputPassword']
    email = request.form['inputEmail']
    update_user(id, user_name, nickname, email, password)
    massage='user is updated'
    return redirect(url_for('profile.index', massage=massage))


# todo create a delete account route in edit profile
@profile_edit.route('/delete_profile')
def delete_account():
    # userid=session['userid']
    userid=5
    session.clear()
    video_dict = get_all_videos(userid)[0]
    # for video in video_dict:
    #     delete_video(id) #todo writing the right id
    delete_user(userid)
    massage ='the account was deleted'
    redirect(url_for('homepage.index',massage=massage))
