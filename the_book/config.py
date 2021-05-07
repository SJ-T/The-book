# file to configure flask, loaded into our flask application
# using the line: app.config.from_pyfile("config.py") in website.py
import os
# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))


# class Config:
    # TESTING = True
    # DEBUG = True
    # FLASK_ENV = 'development'
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


# DATABASE_PASSWORD = environ.get('DB_PASSWORD')
