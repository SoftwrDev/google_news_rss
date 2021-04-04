#!/usr/bin/env python
import json
import requests

import bs4
from bs4 import BeautifulSoup

BASE_URL = "https://news.google.com"
QUERY_STRINGS = "?hl=pt-BR&gl=BR&ceid=BR:pt-419"

def get():
    news = requests.get(f"{BASE_URL}/topstories{QUERY_STRINGS}")
    soup = BeautifulSoup(news.text, "html.parser")

    news_list = []

    for article in soup.select("article"):
        title = article.select("h3 a")
        
        if not title:
            title = article.select("h4 a")[0].text
            url = article.select("h4 a")[0].get("href")
        elif type(title) == bs4.element.ResultSet:
            url = title[0].get("href")
            title = title[0].text
        
        news_list.append({
            "title": title, 
            "url": f"{BASE_URL}/{url}{QUERY_STRINGS}"
        })
    
    return news_list
