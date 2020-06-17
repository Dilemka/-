from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

engine = create_engine('sqlite:///python_habr.db', echo=True)
# engine = create_engine('sqlite:///my.db', echo=True)
metadata = MetaData()

post_list = Table('post', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String, nullable=False),
    Column('avtor', String, nullable=False),
    Column('url', String, unique = True, nullable=False)
)

metadata.create_all(engine)

    
class Post(object):
    def __init__(self, title, avtor, url):
        self.title = title
        self.avtor = avtor
        self.url = url

    def __repr__(self):
        return '<Post {} {} {}>'.format(self.title, self.avtor, self.url)

print(mapper(Post, post_list))
post = Post('Название', 'автор', 'url')
print(post)