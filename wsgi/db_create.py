from app import db
from models import BlogPost, User

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good.", 1))
db.session.add(BlogPost("Well", "I\'m well.", 1))

db.session.add(User("admin", "admin@admin.com", 'admin'))
# commit the changes
db.session.commit()
