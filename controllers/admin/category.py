from run import app
from models import Categories
from run import db
import os
from flask import render_template,redirect,request

@app.route("/admin/categories",methods=["GET","POST"])
def add_and_show_categories():
    all_categories = Categories.query.all()
    if request.method=="POST":
        category_name=request.form["category_name"]
        category=Categories(categories_name=category_name)
        db.session.add(category)
        db.session.commit()
        return redirect("/admin/categories")
    return render_template("admin/category.html",categories=all_categories)

@app.route('/admin/categories/delete/<id>')
def delete_category(id):
    from models import Categories
    from run import db
    user=Categories.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/categories')