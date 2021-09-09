from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap

#Initializing the app
app = Flask(__name__, instance_relative_config=True)
#__name__ variable provides functionality to the main function

#setting up the configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Flask Extensions
bootstrap = Bootstrap(app)

#importing views file which has the routes to various templates.
from app import views
from app import error