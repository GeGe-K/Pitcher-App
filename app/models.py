from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User (UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref='user', lazy="dynamic")

    def save_user(self):

        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password) 

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)  

    def get_user_pitches(self):
        user = User.query.filter_by(id = self.id).first()
        return user.pitches
    
    def get_user_comments(self):
        user  = User.query.filter_by(id = self.id).first()
        return user.comments


class Pitch (db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    category = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    
    comments = db.relationship('Comment', backref='user', lazy="dynamic")
    upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')
    
    def save_pitch(self):

        db.session.add(self)
        db.session.commit()

    def get_pitch_comments(self):

        pitch = Pitch.query.filter_by(id = self.id).first()
        comments = Comment.query.filter_by(pitch_id = pitch.id).order_by(Comment.time.desc())
        return comments

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    comment=db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()

    
