from flask import Blueprint

# main_menu blueprint definition
audio_player = Blueprint('audio_player', __name__, static_folder='static', static_url_path='/audio_player', template_folder='templates')
