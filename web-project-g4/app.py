from flask import Flask

###### App setup
app = Flask(__name__)
try: #todo when subbmit remove this line
    app.config.from_pyfile('settings.py')
except:
    print('using a pc without .env')
#

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)
