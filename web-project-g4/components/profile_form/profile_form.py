from flask import Blueprint

# main_menu blueprint definition
profile_form = Blueprint('profile_form', __name__, static_folder='static', static_url_path='/profile_form', template_folder='templates')
