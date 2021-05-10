from run import db
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_title=db.Column(db.String(50))
    post_time=db.Column(db.String(50))
    post_img=db.Column(db.String(50))
    post_info=db.Column(db.String(50))

class Post_info(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_list_title=db.Column(db.String(100))
    post_info_title=db.Column(db.String(80))
    post_info_time=db.Column(db.String(50))
    post_info_img=db.Column(db.String(50))
    post_info_description=db.Column(db.Text)

class Gallery_img(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_info_img=db.Column(db.String(50))
