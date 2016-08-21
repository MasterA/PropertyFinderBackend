import datetime
from sqlalchemy.orm import relationship

from init import db,app


class User(db.Model):
    __tablename__ = 'husers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(60))
    password = db.Column(db.String(61))


    def __init__(self,username, password):
        self.username = username
        self.password = password



class Favorite(db.Model):
    __tablename__ = 'favorites'
    
    username = db.Column(db.String(60))
    property_id = db.Column(db.String(60))
    comment = db.Text()
    
    def __init__(self,username, property_id, comment):
        self.username = username
        self.property_id = property_id
        self.comment = comment
    
    
    
    
#create
db.create_all(app=app)
