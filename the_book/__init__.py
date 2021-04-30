from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


# configure Flask using environment variables
app.config.from_pyfile("config.py")
app.config['SECRET_KEY'] = 'b238e0be14d21f94350bbd6c18b9defd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #'login' is the function name of the route
login_manager.login_message_category = 'info' #flash a message with 'info' category

from the_book import routes # to prevent circular imports, put the import below the app config
 