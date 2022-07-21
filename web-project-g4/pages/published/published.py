from flask import Blueprint, render_template, session, url_for, redirect, request
from utilities.db.videos import create_a_new_vid

# homepage blueprint definition
published = Blueprint('published', __name__, static_folder='static', static_url_path='/published', template_folder='templates')

# Routes
# updating existing video
@published.route('/published/<VIDEO_ID>', methods=['POST']) #user must come from session
def update(VIDEO_ID: int):
    print('i updating a video')
    session["logedIn"] = True
    # update only what I got
    print(request.files['image'].filename)
    '''if ("logedIn" in session and session['logedIn'] == True):
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

        found_video, video_info = get_video(VIDEO_ID)
            return render_template('new_audio_creator.html', video_id=-1, video_info=video_info)
    else:
        return redirect(url_for('login.index'))'''


# creating new video
@published.route('/published', methods=['POST']) #user must come from session
def create():
    session["logedIn"] = True
    session["userId"] = 0
    print('i creating a video')
    creation_row = create_a_new_vid(request, session['userId'])
    print(creation_row)
    '''session["logedIn"] = True
    #print(request.form)
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

        found_video, video_info = get_video(VIDEO_ID)
            return render_template('new_audio_creator.html', video_id=-1, video_info=video_info)
    else:
        return redirect(url_for('login.index'))'''

# showing the result to the user [GET]
