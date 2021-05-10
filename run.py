from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
UPLOAD_FOLDER='static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

db=SQLAlchemy(app)
from models import *
# App routları
from controllers.app.main import *
# Admin routları
from controllers.admin.news import *
from controllers.admin.main import *
from controllers.admin.gallery import *
if __name__=='__main__':
    app.run(debug=True)