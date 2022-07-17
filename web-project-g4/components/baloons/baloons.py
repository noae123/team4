from flask import Blueprint, render_template

# main_menu blueprint definition
baloons = Blueprint('baloons', __name__, static_folder='static', static_url_path='/baloons', template_folder='templates')
