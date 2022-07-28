from flask import Blueprint, render_template, session, url_for, redirect, request

from utilities.db.users import get_user_id_by_name_password, get_user_by_id, delete_user
from utilities.db.videos import get_all_videos, delete_video

# homepage blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')

# Routes
@profile.route('/profile')
def index():
    session["logedIn"] = True
    session["userId"] = 5
    session["user_name"]=get_user_by_id(5)[0]
    if ("userId" in session and session['logedIn'] == True):
        user_name = session['user_name'] #todo check if work after login page ready
        userID= session['userId']
        video_dict = get_all_videos(userID)[0]
        return render_template('profile.html', video_dict=video_dict, user_id=userID,
                           user_name=user_name)

        # user_id= get_user_id_by_name_password(user_name, password)[0]
        # video_dict = get_all_videos(user_id)[0]
        # video_dict = get_all_videos(session["userId"])[0]  # get a video from user 0

    else:
        return redirect(url_for('login.index'))

# todo create a logout route
@profile.route('/profile', methods=['POST'])
def log_out():
    session.clear()
    return redirect(url_for('homepage.index'))

# todo create a delete a video route
@profile.route('/profile/delete_vid', methods=['GET'])
def delete_a_video():
    delete_video(request.args['id_video'])
    return redirect(url_for('profile.index'))





