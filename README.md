# Flask Web App Demo

Installed plugins:
```
# flask core
pip install Flask
# flask wtforms
pip install Flask-WTF
# flask SQLAlchemy
pip install flask-sqlalchemy
```

P.S. In order to create the database and tables one time you can execute this lines:
```
from flaskblog import db
db.create_all()
```
you can also access ```engine.dialect.has_table(engine, Variable_tableName)``` and then create tables manually, check out:
https://stackoverflow.com/questions/33053241/sqlalchemy-if-table-does-not-exist/33054597

SQLAlchemy usage example:
```
>>> from flaskblog.models import User, Post
>>> User.query.all()
[]
>>> # Create some users
>>> u1 = User(username='admin', email='admin@demo.com',password='admin')
>>> u2 = User(username='master', email='master@demo.com',password='master')
>>> db.session.add(u1)
>>> db.session.add(u2)
>>> db.session.commit()
>>> User.query.all()
[User('admin', 'admin@demo.com', 'default.jpg'), User('master', 'master@demo.com', 'default.jpg')]
>>> User.query.get(1)
User('admin', 'admin@demo.com', 'default.jpg')
>>> User.query.get(3)
>>> User.query.filter_by(username='admin').all()
[User('admin', 'admin@demo.com', 'default.jpg')]
>>> User.query.first()
User('admin', 'admin@demo.com', 'default.jpg')
>>> User.query.filter_by(username='admin').first()
User('admin', 'admin@demo.com', 'default.jpg')
>>> # Create some posts
>>> p2=Post(title='Title2',content='Content for post2', user_id=u1.id)
>>> db.session.add(p1)
>>> db.session.add(p2)
>>> db.session.commit()
>>> Post.query.first()
Post('Title1', '2019-05-27 17:10:21.773807')
>>> Post.query.get(1)
Post('Title1', '2019-05-27 17:10:21.773807')
>>> Post.query.get(2)
Post('Title2', '2019-05-27 17:10:21.774470')
>>> Post.query.get(0)
>>> # Get user's posts
>>> u1.posts
[Post('Title1', '2019-05-27 17:10:21.773807'), Post('Title2', '2019-05-27 17:10:21.774470')]
>>> u1.posts[0]
Post('Title1', '2019-05-27 17:10:21.773807')
>>> Post.query.get(2)
Post('Title2', '2019-05-27 17:10:21.774470')
>>> Post.query.get(2).author
User('admin', 'admin@demo.com', 'default.jpg')
>>> # delete everything
>>> db.drop_all()
>>> # recreate everything
>>> db.create_all()
```

# Tutorial by Corey Schafer
https://www.youtube.com/watch?v=CSHx6eCkmv0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=6
