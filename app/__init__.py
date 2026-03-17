from flask import Flask
from app.extensions import db


def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
   db.init_app(app)

#avoid circular imports
   from app.routes import main_bp
   app.register_blueprint(main_bp)
   
   return app

