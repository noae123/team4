from flask import Blueprint, render_template, session
from utilities.db.videos import get_all_videos

# catalog blueprint definition
catalog = Blueprint('catalog', __name__, static_folder='static', static_url_path='/catalog', template_folder='templates')

# Routes
@catalog.route('/catalog')
def index():
    video_dict = get_all_videos(0)[0] # get a video from user 0
    #call to dbmangger call card4you
    return render_template('catalog.html', video_dict = video_dict)

