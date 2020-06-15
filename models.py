from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
	""" Users Table """
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(25), unique=True, nullable=False)
	password = db.Column(db.String(), nullable=False)

db.create_all()