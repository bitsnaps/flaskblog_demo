# Flask Web App Demo

Installed plugins:
```
# flask core
pip install Flask
# flask wtforms
pip install Flask-WTF
# flask SQLAlchemy
pip install flask-sqlalchemy
# flask bcrypt
pip install flask-bcrypt
# or
# easy_install flask-bcrypt
# conda install -c conda-forge flask-bcrypt
# Flask Login
pip install flask-login
# Pillow to resize image
pip install Pillow
# Flask Email
pip install flask-mail

```
Notes:
- If you're using conda use ```conda install PACKAGE_NAME``` instead of ```pip install PACKAGE_NAME```
- In order to create the database and tables one time you can execute this lines:
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

Flask BCrypt usage example:
```
>>> from flask_bcrypt import Bcrypt
>>> b = Bcrypt()
>>> b.generate_password_hash('hello') # gets hash in bytes
b'$2b$12$ytOK4rsGCjP3G/C8cBby5OQ6U0szXeRQ.kwo5CwvelaxNzINFDoLq'
>>> b.generate_password_hash('hello').decode('utf-8')
'$2b$12$O8H3GqZwXMKANIfUR5wcROc8E1.Tehv7rvdIeb3yn89JUAmbkAF5.'
>>> b.generate_password_hash('hello').decode('utf-8') # different hash for each generation
'$2b$12$mTGKgmeOEBWk8d23VgeZ2ushBIPz.96MqRaqYv0rT7oCgczQPpD6K'
>>> h=b.generate_password_hash('hello').decode('utf-8')
>>> h
'$2b$12$Dme7sAWexBB8iI0T/l3QJe1sXlBiKe7SpUYqaZkuV2KwpSJP8NtCa'
>>> b.check_password_hash(h, '1hello') # Wrong password check
False
>>> b.check_password_hash(h, 'hello') # Correct password check
True
```

Using itsdangerous ecryption library
```
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer('secret', 30) # 30 is an expiration time in seconds
>>> token = s.dumps({'user_id':1}).decode('utf-8')
>>> token
'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1OTM4NTY1MywiZXhwIjoxNTU5Mzg1NjgzfQ.eyJ1c2VyX2lkIjoxfQ.aGoobkmjf4mz2lAUDZ1jYa6tLOoxEx1gt7PnpW7RY8
EaBUpDaJ1rCokyXBmE_TZI3XiJ0IP1aFY5ocZrjOU5oA'
>>> s.loads(token) # check if token is valid
{'user_id': 1}
>>> s.loads(token) # token is expired
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/miniconda2/envs/py3/lib/python3.7/site-packages/itsdangerous/jws.py", line 205, in loads
    date_signed=self.get_issue_date(header),
itsdangerous.exc.SignatureExpired: Signature expired
```

# Tutorial by Corey Schafer
https://www.youtube.com/watch?v=uVNfQDohYNI&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=12
