from run import app
from models import Brands
from run import db
import os
from flask import render_template,redirect,request,url_for

@app.route("/admin/brand",methods=["GET","POST"])
def brands():
    all_brands = Brands.query.all()
    if request.method=="POST":
        brands_name=request.form["brand_name"]
        brand=Brands(brands_name=brands_name)
        db.session.add(brand)
        db.session.commit()
        return redirect('/admin/brand')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template("admin/brand.html",brands=all_brands)
    else:
        return redirect(url_for('login'))

@app.route('/admin/brand/delete/<id>')
def delete_brand(id):
    user=Brands.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/brand')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
            return render_template("admin/brand.html",brands=all_brands)
    else:
        return redirect(url_for('login'))
@app.route("/admin/brand/edit/<id>",methods=["GET","POST"])
def edit_brand(id):
    selected_brand=Brands.query.get(id)
    all_brands=Brands.query.all()
    if request.method=="POST":
        selected_brand.brands_name=request.form["brand_name"]
        db.session.commit()
        return redirect('/admin/brand')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template("admin/brand.html",brands=all_brands,selected_brand=selected_brand)
    else:
        return redirect(url_for('login'))
