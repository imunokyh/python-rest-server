import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

user = os.environ['DATABASE_USER']
password = os.environ['DATABASE_PASSWORD']
host = os.environ['DATABASE_HOST']
port = os.environ['DATABASE_PORT']
name = os.environ['DATABASE_NAME']

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}:{port}/{name}?charset=utf8'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    return app