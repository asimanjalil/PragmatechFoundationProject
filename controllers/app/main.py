from run import app
from flask import render_template,redirect,request
@app.route('/')
def main_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/index.html',posts=posts)

@app.route('/about')
def about_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/about.html',posts=posts)

@app.route('/products')
def products_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/products.html',posts=posts)

@app.route('/products_ext')
def products_ext_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/products_ext.html',posts=posts)

@app.route('/choose')
def choose_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/choose_oil.html',posts=posts)
    
@app.route('/news')
def news_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/news.html',posts=posts)

@app.route('/news/about')
def news_about_index():
    from models import Post_info
    posts=Post_info.query.all()
    return render_template('app/news_about.html',posts=posts)

@app.route('/gallery')
def gallery_main_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/gallery.html',posts=posts)

@app.route('/contact')
def contact_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/contact.html',posts=posts)