from flask import Blueprint, render_template, session, url_for, redirect

# homepage blueprint definition
published = Blueprint('published', __name__, static_folder='static', static_url_path='/published', template_folder='templates')

# Routes
@published.route('/published/<int:VIDEO_ID>', methods=['POST']) #user must come from session
def index(VIDEO_ID: int):
    session["logedIn"] = True
    if ("logedIn" in session and session['logedIn'] == True):
        if VIDEO_ID == -1:
            print('todo in python')
            # todo write this code
            # insert new video to db
            # only than render this page
        else:
            print('todo in python')
            # todo write this code
            # try to update this row
            # expect create this row

        '''found_video, video_info = get_video(VIDEO_ID)
            return render_template('new_audio_creator.html', video_id=-1, video_info=video_info)'''
    else:
        return redirect(url_for('login.index'))
