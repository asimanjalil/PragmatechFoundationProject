from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData,event
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
UPLOAD_FOLDER='static/uploads/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

db = SQLAlchemy(app,metadata= MetaData(naming_convention=naming_convention))
migrate = Migrate()
migrate.init_app(app,db,compare_type=True,render_as_batch = True)

# App routları
from controllers.app.main import *
# Admin routları
from controllers.admin.products import *
from controllers.admin.news import *
from controllers.admin.main import *
from controllers.admin.gallery import *
from controllers.admin.main_page import *
from controllers.admin.category import *
from controllers.auth.routes import *
from controllers.admin.brand import *
from models import *
db.create_all()
if __name__=='__main__':
    app.run(debug=True)