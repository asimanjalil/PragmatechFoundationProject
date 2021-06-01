from run import app
import os,sys
from flask import render_template,redirect,request,url_for
from werkzeug.utils import secure_filename
from run import db
from models import Products,Categories,Brands

@app.route('/admin/products',methods=['GET','POST'])
def admin_products():
    
    products=Products.query.all()
    categories=Categories.query.all()

    if request.method=='POST':
        file=request.files['product_img']
        filename=file.filename
        title=secure_filename(request.form['product_name'])
        file_extention=filename.split(".")[-1]
        filename=title+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        product=Products(
            product_status=request.form['product_status'],
            category_id=request.form['product_category'],
            brand_id=request.form['product_brand'],
            product_name=request.form['product_name'],
            product_price=request.form['product_price'],
            product_img=filename,
            product_simple_description=request.form['product_simple_description'],
            product_details_description=request.form['product_details_description'],
            product_old_price=request.form['product_old_price']
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/products')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template('admin/products.html',products=products,categories=categories,Categories=Categories,brands=Brands.query.all())
    else:
        return redirect(url_for('login'))
    

@app.route('/admin/products/delete/<id>')
def delete_product(id):
    
    user=Products.query.get(id)
    db.session.delete(user)
    
    db.session.commit()
    return redirect('/admin/products')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template('admin/products.html',products=products,categories=categories,Categories=Categories)
    else:
        return redirect(url_for('login'))

@app.route("/admin/products/edit/<id>",methods=["GET","POST"])
def edit_products(id):
    selected_products=Products.query.get(id)
    products=Products.query.all()
    if request.method=="POST":
        selected_products.product_status=request.form['product_status']
        selected_products.product_name=request.form["product_name"]
        selected_products.product_price=request.form["product_price"]
        selected_products.product_simple_description=request.form["product_simple_description"]
        selected_products.product_details_description=request.form["product_details_description"]
        file=request.files["product_img"]
        filename=file.filename
        title=secure_filename(request.form['product_name'])
        file_extention=filename.split(".")[-1]
        filename=title+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        selected_products.product_img=filename
        db.session.commit()
        return redirect('/admin/products')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template("admin/products.html",product=products,selected_products=selected_products)
    else:
        return redirect(url_for('login'))