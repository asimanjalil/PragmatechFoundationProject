from run import app
from flask import render_template,redirect,request
from models import Post
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
    from models import Products
    products=Products.query.all()
    return render_template('app/products.html',products=products)

@app.route('/products_ext/<id>',methods=['GET','POST'] )
def products_ext_index(id):
    from models import Products
    product=Products.query.get(id)
    return render_template('app/products_ext.html',product=product)

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