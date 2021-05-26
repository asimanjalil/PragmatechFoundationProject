from run import app
import os
from flask import render_template,redirect,request
from werkzeug.utils import secure_filename

@app.route('/admin/news/about',methods=['GET','POST'])
def news_info(): 
    from run import db
    from models import Post   
    posts=Post.query.all()
    # Necəsə oldu,bilmirəm 
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
            post_description=request.form['post_description'],
            post_img=filename
        )
        db.session.add(post)
        db.session.commit()
        
        return redirect("/admin/news/about")

    
    return render_template("admin/news_about.html",posts=posts)
