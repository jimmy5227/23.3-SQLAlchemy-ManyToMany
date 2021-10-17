from models import db, users, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

default = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'

Larry = users(first_name='Larry', last_name='Rockland', image_url=default)
Joel = users(first_name='Joel', last_name='Burton',
             image_url='https://pbs.twimg.com/profile_images/1217917608/IMG_3419_400x400.jpg')
Alda = users(first_name='Alda', last_name='Alva', image_url=default)

post1 = Post(title='First Post', content='Hello World', user_id='1')
post2 = Post(title='Yet Another Post', content='Another post!', user_id='1')

tag1 = Tag(name='Fun')
tag2 = Tag(name='Even More')
tag3 = Tag(name='Bloop')

db.session.add(Larry)
db.session.add(Joel)
db.session.add(Alda)

db.session.add(post1)
db.session.add(post2)

db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)

db.session.commit()

posttag1 = PostTag(post_id='1', tag_id='1')
posttag2 = PostTag(post_id='1', tag_id='2')
posttag3 = PostTag(post_id='2', tag_id='3')

db.session.add(posttag1)
db.session.add(posttag2)
db.session.add(posttag3)

db.session.commit()
