from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from the_book.config import Config
import os
app = Flask(__name__)


# Initialize database
if os.environ.get('DATABASE_URL'):
  # Set the database URL from the environment variable if it is set. 
  # The .replace() is a workaround because of a mismatch between Heroku's default set up and SQLAlchemy
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
else:
  # Use SQLite as a fallback and locally
    app.config.from_object(Config)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #'login' is the function name of the route
login_manager.login_message_category = 'info' #flash a message with 'info' category

from the_book import routes # to prevent circular imports, put the import below the app config
 