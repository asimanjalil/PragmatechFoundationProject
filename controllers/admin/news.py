from run import app
from models import Post
from run import db
import os
from flask import render_template,redirect,request,url_for
from werkzeug.utils import secure_filename

@app.route('/admin/news',methods=['GET','POST'])
def admin_news_index():
    from run import db
    posts=Post.query.all()

    if request.method=='POST':
        file=request.files['post_img']
        filename=file.filename
        title=secure_filename(request.form['post_title'])
        file_extention=filename.split(".")[-1]
        filename=title+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        post=Post(
            post_title=request.form['post_title'],
            post_time=request.form['post_time'],
            post_info=request.form['post_info'],
            post_img=filename,
            post_description=request.form['post_description']
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/news')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template('admin/news.html',posts=posts)
    else:
        return redirect(url_for('login'))


@app.route('/admin/news/delete/<id>')
def delete_news(id):
    from models import Post
    from run import db
    user=Post.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/news')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template('admin/news.html',posts=posts)
    else:
        return redirect(url_for('login'))

@app.route("/admin/news/edit/<id>",methods=["GET","POST"])
def edit_news(id):
    selected_news=Post.query.get(id)
    posts=Post.query.all()
    if request.method=="POST":
        selected_news.post_title=request.form["post_title"]
        selected_news.post_time=request.form["post_time"]
        selected_news.post_info=request.form["post_info"]
        selected_news.post_description=request.form["post_description"]
        selected_news.post_img=request.form["post_img"]
        db.session.commit()
        return redirect('/admin/news')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template("admin/news.html",post=posts,selected_news=selected_news)
    else:
        return redirect(url_for('login'))




