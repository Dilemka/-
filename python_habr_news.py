# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
import codecs
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my.db', echo=True)


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestEception, ValueError):
        print("Сетевая ошибка")
        return False


def get_habr_news(html):

    soup = BeautifulSoup(html, "html.parser")
    all_news = soup.findAll("article", class_="post post_preview")
    result_all_news = []

    for news in all_news:
        title = news.find("a", class_="post__title_link").text
        avtor = news.find(
            "span",
            class_="user-info__nickname user-info__nickname_small").text
        url = news.find("a", class_="post__title_link")["href"]
        result_all_news.append({
            "title": title,
            "avtor": avtor,
            "url": url
        })
    return result_all_news

Base = declarative_base()
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    avtor = Column(String)
    url = Column(String)

    def __repr__(self):
        return '<Post {} {} {}>'.format(self.title, self.avtor, self.url)


def write_news_bd(res):
    for new_post in res:
        p1 = Post(
            title=new_post['title'], avtor=new_post['avtor'],
            url=new_post['url'])
        session.add(p1)
    session.commit()

def avtor_post_bd(res):
   for user in session.query(Post).\
        filter(Post.avtor=='itsoft'):
        print(user)
        session.add(user)
        session.commit()

if __name__ == "__main__":
    
    Session = sessionmaker(bind=engine)
    session = Session()
    html = get_html("https://www.habr.com/ru/all/")
    if html:
        get_habr_news(html)
        res = get_habr_news(html)
        write_news_bd(res)
