from flask import Blueprint, render_template, session, url_for, redirect
import os

# homepage blueprint definition
new_audio_creator = Blueprint('new_audio_creator', __name__, static_folder='static', static_url_path='/new_audio_creator', template_folder='templates')


# Routes
@new_audio_creator.route('/new_audio_creator', defaults={'VIDEO_ID': None}) #user id i get from the session
@new_audio_creator.route('/new_audio_creator/<int:VIDEO_ID>')
def index(VIDEO_ID: int):
    session["logedIn"] = True
    if("logedIn" in session and session['logedIn'] == True):
        #if(VIDEO_ID == None):
        video_info = {
            'audio': url_for('audio_player.static', filename='media/music/happybday.mp3'),
            'img': url_for('audio_player.static', filename='media/img/Black.png'),
            'sender_name': 'Sender Name',
            'card_banner': 'Card Banner',
            'color': 'white',
            'shape': 'circle',
            'dir': False
        }

        #else go to the db and get me the video

        #make this to some kind of string
        VIDEO_ID = 'p' + str(VIDEO_ID)
        return render_template('new_audio_creator.html', video_id=VIDEO_ID, video_info=video_info)
    else:
        return redirect(url_for('login.index'))
