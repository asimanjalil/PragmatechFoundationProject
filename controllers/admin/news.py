from run import app
import os
from flask import render_template,redirect,request
from werkzeug.utils import secure_filename

@app.route('/admin/news',methods=['GET','POST'])
def admin_news_index():
    from run import db
    from models import Post
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
            post_img=filename
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/news')
    return render_template('admin/news.html',posts=posts)

@app.route('/admin/news/info',methods=['GET','POST'])
def news_info():
    from run import db
    from models import Post_info
    posts=Post_info.query.all()

    if request.method=='POST':
        file=request.files['post_info_img']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        filename=file.filename
        title_info=secure_filename(request.form['post_info_title'])
        file_extention=filename.split(".")[-1]
        filename=title_info+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        post=Post(
            post_list_title=request.form['post_list_title'],
            post_info_title=request.form['post_info_title'],
            post_info_time=request.form['post_info_time'],
            post_info_description=request.form['post_info_description'],
            post_info_img=filename
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/news/info')
    return render_template('admin/news_about.html',posts=posts)





