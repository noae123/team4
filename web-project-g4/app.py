from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# files folder
UPLOAD_FOLDER = './static/media_users'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## Login
from pages.login.login import login
app.register_blueprint(login)

## Register
from pages.register.register import register
app.register_blueprint(register)

## Profile
from pages.profile.profile import profile
app.register_blueprint(profile)

## Profile_Edit
from pages.profile_edit.profile_edit import profile_edit
app.register_blueprint(profile_edit)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Shared
from pages.shared.shared import shared
app.register_blueprint(shared)

## Published
from pages.published.published import published
app.register_blueprint(published)

## New Audio Creator
from pages.new_audio_craetor.new_audio_craetor import new_audio_creator
app.register_blueprint(new_audio_creator)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

## Baloons
from components.baloons.baloons import baloons
app.register_blueprint(baloons)

## Audio Player
from components.audio_player.audio_player import audio_player
app.register_blueprint(audio_player)

## Profile Form
from components.profile_form.profile_form import profile_form
app.register_blueprint(profile_form)
