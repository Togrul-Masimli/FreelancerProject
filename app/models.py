from datetime import date, datetime
from enum import unique
from sqlalchemy.orm import backref, lazyload
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    about_user = db.Column(db.Text)
    education = db.Column(db.Text)
    speciality = db.Column(db.String(20))
    location = db.Column(db.String(20))
    age = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    hourly_rate = db.Column(db.Integer)
    job_done = db.Column(db.Integer)
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all,delete')
    comments = db.relationship('Comment', backref='comment_author', lazy=True, cascade='all,delete')
    bids = db.relationship('Bid', backref='bid_owner', lazy=True, cascade='all,delete')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    min_pay = db.Column(db.Integer, nullable=False)
    max_pay = db.Column(db.Integer)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tag = db.relationship('Tag', secondary='posts_tags', backref=db.backref('posts', lazy='dynamic'))
    comments = db.relationship('Comment', backref='host', lazy=True)
    bids = db.relationship('Bid', backref='bid_host', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_writed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content})"


class Bid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    min_rate = db.Column(db.Integer, nullable=False)
    max_rate = db.Column(db.Integer, nullable=False)
    delivery_duration = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Bid('{self.min_rate}"

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    db.column = db.relationship(Post, backref='tags', lazy=True)

    def __repr__(self):
        return f'{self.title}'

posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))

class Privacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Privacy('{self.content})"
