from flask import Flask
# importing libraries
from flask import Flask, request, Response, jsonify, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__, template_folder='templates')
app.secret_key = "super secret key"
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



