from flask import Blueprint, render_template, session, url_for, redirect

# homepage blueprint definition
shared = Blueprint('shared', __name__, static_folder='static', static_url_path='/shared', template_folder='templates')


# Routes
@shared.route('/shared/<int:VIDEO_ID>/<int:USER_ID>') #user must come from session
def index(VIDEO_ID: int, USER_ID:int):
    #this must return a valid user or id , else rederict it to '/error_video_not_found'
    video_info = {
        'audio': url_for('audio_player.static', filename='media/music/happybday.mp3'),
        'img': url_for('audio_player.static', filename='media/img/Black.png'),
        'sender_name': 'Sender Name',
        'card_banner': 'Card Banner',
        'color': 'white',
        'shape': 'circle',
        'dir': False
    }

    # else go to the db and get me the video

    # make this to some kind of string
    VIDEO_ID = 'p' + str(0) #need to change and give here a list of videos
    return render_template('shared.html', video_id=VIDEO_ID, video_info=video_info)
