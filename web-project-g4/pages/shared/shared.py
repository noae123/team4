from flask import Blueprint, render_template

# homepage blueprint definition
shared = Blueprint('shared', __name__, static_folder='static', static_url_path='/shared', template_folder='templates')


# Routes
@shared.route('/shared')
def index():
    return render_template('shared.html')