from flask import Blueprint, render_template, session, url_for, redirect
import os

from utilities.db.videos import get_video, create_empty_video

# homepage blueprint definition
new_audio_creator = Blueprint('new_audio_creator', __name__, static_folder='static', static_url_path='/new_audio_creator', template_folder='templates')


# Routes
@new_audio_creator.route('/new_audio_creator', defaults={'VIDEO_ID': None}) #user id i get from the session
@new_audio_creator.route('/new_audio_creator/<int:VIDEO_ID>')
def index(VIDEO_ID: int):
    print(session['userId'])
    if("logedIn" in session and session['logedIn'] == True):
        message = None
        if VIDEO_ID == None:
            VIDEO_ID,  video_info = create_empty_video()
        else:
            print(session['userId'])
            video_info, found_video = get_video(VIDEO_ID, session["userId"])
            if found_video == False:
                message = 'Hi there, it seems that your are trying to access a video that is not there :(, oh well here is an  empty video that you can design'
        return render_template('new_audio_creator.html', video_id=VIDEO_ID, video_info=video_info, message=message)
    else:
        return redirect(url_for('login.index'))

# Routes
@new_audio_creator.route('/new_audio_creator/template/<int:VIDEO_ID>')
def index_template(VIDEO_ID: int):
    print(session['userId'])
    if ("logedIn" in session and session['logedIn'] == True):
        video_info, found_video = get_video(VIDEO_ID)
        if found_video:
            return render_template('new_audio_creator.html', video_id=-1, video_info=video_info, message=None)
        else:
            message = 'Hi there, it seems that your are trying to access a video that is not there :(, oh well here is an  empty video that you can design'
            return render_template('new_audio_creator.html', video_id=-1, video_info=video_info, message=message)
    else:
        return redirect(url_for('login.index'))
