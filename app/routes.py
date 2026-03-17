from flask import Flask, jsonify, Blueprint
from app.extensions import db
from app.models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
   return "<h1>Welcome to the API</h1>"

@main_bp.route('/add_user',)
def add_user():
    user = User(name='Asher', email = "asherk.2250@gmail.com")
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'})