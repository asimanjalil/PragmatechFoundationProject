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
        post_info=Post_info(
            post_list_title=request.form['post_list_title'],
            post_info_title=request.form['post_info_title'],
            post_info_time=request.form['post_info_time'],
            post_info_description=request.form['post_info_description'],
            post_info_img=filename
        )
        db.session.add(post_info)
        db.session.commit()
        return redirect('/admin/news/info')
    return render_template('admin/news_about.html',posts=posts)