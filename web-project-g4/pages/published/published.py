from flask import Blueprint, render_template, session, url_for, redirect, request
from utilities.db.videos import create_a_new_vid, update_video, get_video

# homepage blueprint definition
published = Blueprint('published', __name__, static_folder='static', static_url_path='/published', template_folder='templates')

# showing the result to the user [GET]
@published.route('/published/<VIDEO_ID>')
def index(VIDEO_ID: int):
    video_info, found_video = get_video(VIDEO_ID, session["userId"])
    if found_video:
        return render_template('published.html', video_id=VIDEO_ID, video_info=video_info)
    else:
        return redirect(url_for('page_not_found.index'))

# Routes
# updating existing video
@published.route('/published/<VIDEO_ID>', methods=['POST']) #user must come from session
def update(VIDEO_ID: int):
    session["logedIn"] = True
    update_video(request, session['userId'], VIDEO_ID)
    return redirect(url_for('published.index', VIDEO_ID=VIDEO_ID))

# creating new video
@published.route('/published', methods=['POST']) #user must come from session
def create():
    creation_row = create_a_new_vid(request, session['userId'])
    return redirect(url_for('published.index', VIDEO_ID=creation_row))


