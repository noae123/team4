from flask import Blueprint, render_template,session, url_for, redirect

# homepage blueprint definition
profile_edit = Blueprint('profile_edit', __name__, static_folder='static', static_url_path='/profile_edit', template_folder='templates')


# Routes
@profile_edit.route('/profile_edit') #user must come from session
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
        return render_template('profile_edit.html', video_id=VIDEO_ID, video_info=video_info)
    else:
        return redirect(url_for('login.index'))