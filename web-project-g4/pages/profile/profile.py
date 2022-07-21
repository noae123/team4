from flask import Blueprint, render_template, session, url_for, redirect, request
from utilities.db.videos import get_all_videos, delete_video

# homepage blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')

# Routes
@profile.route('/profile')
def index():
    session["logedIn"] = True
    session["userId"] = 0
    if ("logedIn" in session and session['logedIn'] == True):
        video_dict = get_all_videos(session["userId"])[0]  # get a video from user 0
        return render_template('profile.html', video_dict=video_dict)
    else:
        return redirect(url_for('login.index'))

# todo create a logout route

# todo create a delete a video route
@profile.route('/profile', methods=['POST'])
def delete_a_video():
    delete_video(request.args['id_video'])
    return redirect(url_for('profile.index'))

# todo create a delete account route
