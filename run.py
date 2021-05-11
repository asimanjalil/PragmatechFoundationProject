from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
UPLOAD_FOLDER='static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

db=SQLAlchemy(app)
migrate = Migrate(app, db)

# App routları
from controllers.app.main import *
# Admin routları
from controllers.admin.news_about import *
from controllers.admin.news import *
from controllers.admin.main import *

from controllers.admin.gallery import *


from controllers.admin.main_page import *
from models import *
if __name__=='__main__':
    app.run(debug=True)