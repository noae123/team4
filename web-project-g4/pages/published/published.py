from flask import Blueprint, render_template

# homepage blueprint definition
published = Blueprint('published', __name__, static_folder='static', static_url_path='/published', template_folder='templates')


# Routes
@published.route('/published')
def index():
    return render_template('published.html')