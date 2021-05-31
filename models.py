import email
from enum import unique

from click import password_option
from run import db
    
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_title=db.Column(db.String(50))
    post_time=db.Column(db.String(50))
    post_img=db.Column(db.String(50))
    post_info=db.Column(db.String(50))
    post_description=db.Column(db.Text)

class Brands(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    brands_name=db.Column(db.String(100))
    products=db.relationship('Products', backref='brands', lazy=True)    

class Categories(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    categories_name=db.Column(db.String(100))
    products=db.relationship('Products', backref='categories', lazy=True)    
    
class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_sale=db.Column(db.String(50))
    product_sale_name=db.Column(db.String(20))
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'))
    brand_id=db.Column(db.Integer,db.ForeignKey('brands.id'))
   
    product_img=db.Column(db.String(50))
    product_name=db.Column(db.String(50))
    product_price=db.Column(db.String(50))
    product_simple_description=db.Column(db.Text)
    product_details_description=db.Column(db.Text)
    product_old_price=db.Column(db.String(50))

class Gallery_img(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    gallery_title=db.Column(db.String(50))
    gallery_img=db.Column(db.String(50))

