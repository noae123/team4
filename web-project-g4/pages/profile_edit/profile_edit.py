from flask import Blueprint, render_template

# homepage blueprint definition
profile_edit = Blueprint('profile_edit', __name__, static_folder='static', static_url_path='/profile_edit', template_folder='templates')


# Routes
@profile_edit.route('/profile_edit')
def index():
    return render_template('profile_edit.html')