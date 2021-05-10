from run import app
import os
from flask import render_template,redirect,request

@app.route('/admin/gallery',methods=['GET','POST'])
def gallery_index():
    if request.method=='POST':
        file=request.files['post_img']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        posts=Gallery_img(
            gallery_img=filename
        )
        db.session.add(post)
        db.session.commit()
        return redirect('/admin/gallery')
    return render_template('admin/gallery.html',posts=posts)