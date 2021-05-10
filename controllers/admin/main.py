from run import app
from flask import render_template,redirect,request
@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/news')
def news_admin_index():
    return render_template('admin/news.html')

@app.route('/admin/news/info')
def news_info_about():
    return render_template('admin/news_about.html')

@app.route('/admin/products')
def products_admin_():
    return render_template('admin/products.html')

@app.route('/admin/products/ext')
def products_ext_admin():
    return render_template('admin/products_ext.html')

@app.route('/admin/gallery')
def gallery_admin():
    return render_template('admin/gallery.html')
    