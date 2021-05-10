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

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_sale=db.Column(db.String(50))
    product_category=db.Column(db.String(100))
    product_category_title=db.Column(db.String(100))
    product_img=db.Column(db.String(50))
    product_title=db.Column(db.String(50))
    product_price=db.Column(db.String(50))

class Products_info(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_list_title=db.Column(db.String(100))
    product_info_title=db.Column(db.String(80))
    product_info_img=db.Column(db.String(50))
    product_info_sale=db.Column(db.String(50))
    product_info_price=db.Column(db.String(50))
    product_simple_description=db.Column(db.Text)
    product_info_category=db.Column(db.String(50))
    product_details_description=db.Column(db.Text)

class Similar_products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    similar_product_sale=db.Column(db.String(50))
    similar_product_photo=db.Column(db.String(50))
    similar_product_category=db.Column(db.String(50))
    similar_product_title=db.Column(db.String(50))
    similar_product_price=db.Column(db.String(50))
    



class Gallery_img(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    post_info_img=db.Column(db.String(50))
