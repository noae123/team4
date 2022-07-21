from flask import Blueprint, render_template, session, url_for, redirect
from utilities.db.videos import get_video

# homepage blueprint definition
shared = Blueprint('shared', __name__, static_folder='static', static_url_path='/shared', template_folder='templates')


# Routes
@shared.route('/shared/<int:VIDEO_ID>/<int:USER_ID>') #user must come from session
def index(VIDEO_ID: int, USER_ID:int):
    video_info, found_video = get_video(VIDEO_ID, USER_ID)
    if found_video:
        return render_template('shared.html', video_id=VIDEO_ID, video_info=video_info)
    else:
        return redirect(url_for('page_not_found.index'))
