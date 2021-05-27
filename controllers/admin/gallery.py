from run import app
import os
from flask import render_template,redirect,request
from werkzeug.utils import secure_filename


@app.route('/admin/gallery',methods=['GET','POST'])
def admin_gallery_index():
    from run import db
    from models import Gallery_img
    if request.method=='POST':
        file=request.files['gallery_img']
        filename=file.filename
        title_gallery=secure_filename(filename)
        file_extention=filename.split(".")[-1]
        filename=title_gallery+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        gallery=Gallery_img(
            gallery_img=filename
        )
        db.session.add(gallery)
        db.session.commit()
        return redirect('/admin/gallery')
    return render_template('admin/gallery.html',gallery_img=Gallery_img.query.all())
@app.route('/admin/gallery/delete/<id>')
def delete_gallery(id):
    from models import Gallery_img
    from run import db
    user=Gallery_img.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/gallery')
