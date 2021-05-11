
from run import app
import os
from flask import render_template,redirect,request
from werkzeug.utils import secure_filename
from models import Gallery_img

@app.route('/admin/gallery',methods=['GET','POST'])
def admin_gallery_index():
    from run import db
    
    gallery_img=Gallery_img.query.all()

    if request.method=='POST':
        file=request.files['gallery_img']
        filename=file.filename
        title=secure_filename(request.form['gallery_img'])
        file_extention=filename.split(".")[-1]
        filename=title+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        gallery=Gallery_img(
            gallery_img=filename
        )
        db.session.add(gallery)
        db.session.commit()
        return redirect('/admin/gallery')
    return render_template('admin/gallery.html',gallery_img=gallery_img)