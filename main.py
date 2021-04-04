import datetime

from fastapi import FastAPI

from fastapi_rss import (
    RSSFeed, RSSResponse, Item, Category,
    CategoryAttrs, GUID,
)

import google_news

app = FastAPI()

@app.get("/news")
def get_news():
    news = []

    for n in google_news.get():
        news.append(
                Item(
                    title=n["title"],
                    link=n["url"],
                    guid=GUID(content=n["title"])
                )
        )

    feed_data = {
        'title': 'Google news',
        'link': 'https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt-419',
        'description': '',
        'language': 'pt-BR',
        'generator': 'SoftwrDev',
        'item': news 
    }

    feed = RSSFeed(**feed_data)
    return RSSResponse(feed) 


