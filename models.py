"""Models for Blogly."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


default = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'


class users(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        return f'<id: {self.id} firstName: {self.first_name} lastName: {self.last_name} profilePic: {self.image_url}>'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(
        db.String, nullable=False, default=default)

    def greet(self):
        return f'Hello, my name is {self.first_name} {self.last_name}.'

    def update_image(self, url=default):
        self.image_url = url


class Post(db.Model):
    __tablename__ = 'post'

    def __repr__(self):
        return f'<id: {self.id} title: {self.title} content: {self.content} created_at: {self.created_at} user_id: {self.user_id}>'

    users = db.relationship('users', backref='post')
    # tag = db.relationship('Tag', secondary='posttag', backref='post')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Tag(db.Model):
    __tablename__ = 'tag'

    posts = db.relationship('Post', secondary='posttag', backref='tag')

    def __repr__(self):
        return f'<tag id: {self.id} name: {self.name}>'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)


class PostTag(db.Model):
    __tablename__ = 'posttag'

    def __repr__(self):
        return f'<post id: {self.post_id} tag id: {self.tag_id}>'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id'), primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tag.id'), primary_key=True, nullable=False)
