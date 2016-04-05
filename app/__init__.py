from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:zen@localhost/project3"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://lpqgkfgnjwrgog:oZCtNcHwhsoOxugx46r1AoXz7K@ec2-54-235-93-178.compute-1.amazonaws.com:5432/dd1mgh01kj3m1n"
db = SQLAlchemy(app)
db.create_all()

from app import views,models