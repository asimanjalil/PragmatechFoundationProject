from run import app
from flask import render_template,redirect,request
@app.route('/')
def main_index():
    from models import Post
    posts=Post.query.all()
    return render_template('app/news.html',posts=posts)

def main_gallery_index():
    from models import Post
    posts=Post_info.query.all()
    return render_template('app/gallery.html',posts=posts)