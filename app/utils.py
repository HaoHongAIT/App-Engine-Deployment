from app import app
from app.models import *


def load_categories():
    return Category.query.all()


def count_news(category_id):
    if category_id != 0:
        return News.query.filter(News.category_id.__eq__(int(category_id))).count()
    return News.query.filter().count()


def load_news(category_id, keyword=None, page=1):
    news = News.query.filter()
    if category_id != 0:
        news = news.filter(News.category_id.__eq__(category_id))
    if keyword:
        news = news.filter(News.brief.contains(keyword))

    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size

    return news.slice(start, end).all()


