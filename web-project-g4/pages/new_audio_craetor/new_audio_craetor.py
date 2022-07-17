from flask import Blueprint, render_template

# homepage blueprint definition
new_audio_creator = Blueprint('new_audio_creator', __name__, static_folder='static', static_url_path='/new_audio_creator', template_folder='templates')


# Routes
@new_audio_creator.route('/new_audio_creator')
def index():
    return render_template('new_audio_creator.html')