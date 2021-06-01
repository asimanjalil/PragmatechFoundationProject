from run import app
from flask import render_template,redirect,request
from models import *
@app.context_processor
def inject_user():
    return dict(categories=Categories.query.all(),brands=Brands.query.all(),Brands=Brands,Products=Products)
@app.route('/')
def main_index():
   
    posts=Post.query.all()
    return render_template('app/index.html',posts=posts)

@app.route('/about')
def about_index():
  
    posts=Post.query.all()
    return render_template('app/about.html',posts=posts)

@app.route('/products')
def products_index():
    from models import Products
    products=Products.query.all()
    return render_template('app/products.html',products=products,Categories=Categories,Products=Products)

@app.route('/products_ext/<id>',methods=['GET','POST'] )
def products_ext_index(id):
    
    product=Products.query.get(id)
    return render_template('app/products_ext.html',product=product,Categories=Categories,Products=Products)

@app.route('/choose')
def choose_index():
    return render_template('app/choose_oil.html')
    
@app.route('/news')
def news_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/news.html',posts=posts)

@app.route('/news/about/<int:id>')
def news_about_index(id):
    selected_post=Post.query.get(id)
    all_posts=Post.query.all()
    all_posts.reverse()
    
    return render_template('app/news_about.html',post=selected_post,reverse_post=all_posts)

@app.route('/gallery')
def gallery_main_index():
    from models import Gallery_img
    gallery_img=Gallery_img.query.all()
    return render_template('app/gallery.html',gallery_img=gallery_img)

@app.route('/contact')
def contact_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/contact.html',posts=posts)

@app.route('/category/<int:id>')
def category(id):
    from models import Products
   
    selected_category=Categories.query.get(id)
    return render_template('app/category.html',Products=Products,selected_category=selected_category,Categories=Categories)

app.route('/brand/<int:id>')
def brand(id):
    from models import Products
    selected_brand=Brands.query.get(id)
    return render_template('app/brand.html',Products=Products,selected_brand=selected_brand,Categories=Categories)
