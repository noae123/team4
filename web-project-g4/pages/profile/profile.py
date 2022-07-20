from flask import Blueprint, render_template, session, url_for, redirect

# homepage blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')


# Routes
@profile.route('/profile/') #user must come from session
def index():
    session["logedIn"] = True
    if ("logedIn" in session and session['logedIn'] == True):
        # if(VIDEO_ID == None):
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
        return render_template('profile.html', video_id=VIDEO_ID, video_info=video_info)
    else:
        return redirect(url_for('login.index'))
