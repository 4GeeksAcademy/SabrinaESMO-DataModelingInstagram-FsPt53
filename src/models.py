import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__='User'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(15), index=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    email = Column(String(40), nullable=False)

class Post(Base):
    __tablename__='Post'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('User.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__='Comment'
    id = Column (Integer, primary_key=True)
    comment_text = Column(String(200))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column (Integer, ForeignKey('Post.id'))
    user = relationship(User)
    post = relationship(Post)

class Follower(Base):
    __tablename__='Follower'
    id = Column (Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)


class Like(Base):
    __tablename__='Like'
    id = Column (Integer, primary_key=True)
    like_post_id = Column(Integer, ForeignKey('Post.id'))
    like_from_user_id = Column(Integer, ForeignKey('User.id'), ForeignKey('Post.id'))
    post = relationship(Post)
    user = relationship(User)



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
