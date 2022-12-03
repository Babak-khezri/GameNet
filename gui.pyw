from curses import resize_term
from flaskwebgui import FlaskUI
from config.wsgi import application as app


ui = FlaskUI(app,maximized=True, start_server='django')

ui.run()
