from the_book import db, login_manager
from flask_login import UserMixin
#from sqlalchemy_imageattach.entity import Image, image_attachment

#reload the user from the userid stored in this session, 
#because extension has to know how to find one of your users by ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#many-to-many relationship, only 2 foreign keys
to_read_list = db.Table('to_read_list',
    # db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.UniqueConstraint('user_id','book_id')
)


# SQLAlchemy create db table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    shelf = db.relationship('Book', secondary=to_read_list, backref=db.backref('readers'), lazy='dynamic')
    ratings = db.relationship('BookRating', backref='rater', lazy='dynamic')


    # # backref similar to adding another column to the post model, when we have a post we can simply use this 'author' attribute to get the user who created the post. post_instance.author => User('[username]','[email]')
    # posts = db.relationship('Post', backref='author', lazy=True)
    # # 'Post' reference the Post class.
    # # it runs an addtional query on the post table that grabs any post from that user

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), nullable=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True) 
    num_page = db.Column(db.Integer,nullable=True)
    average_rating = db.Column(db.Float,nullable=True)
    ratings_count = db.Column(db.Integer,nullable=True) 
    publication_date = db.Column(db.Text,nullable=True)
    publisher = db.Column(db.String(200),nullable=True)
    # ratings = db.relationship('BookRating', backref='book', lazy='dynamic')
    def __repr__(self):
        return f"Book('{self.id}','{self.title}')"


#many-to-many relationship, 2 foreign keys with extra data 
class BookRating(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    rating = db.Column(db.Integer)
    user = db.relationship("User", backref="books")
    book = db.relationship("Book", backref="raters")





# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column
#     date_posted = db.Column
#     content = db.Column()
#     # user reference the table 'user'
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}','{self.date_posted}')"
