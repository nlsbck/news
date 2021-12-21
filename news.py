from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='3f975a645c834ecea4847e8726122157')
import pandas as pd
from bs4 import BeautifulSoup

print("news")
def top_headlines():
    country = input("Which country are you interested in?")
    category = input("""Which category are you interested in?
    Here are the categories to choose from:
    business
    entertainment   
    general
    health
    science
    technology""")
    top_headlines = newsapi.get_top_headlines(category=category,
    language='en', country=country)
    top_headlines = pd.json_normalize(top_headlines['articles'])
    newdf = top_headlines[["title", "url"]]
    dic = newdf.set_index('title')['url'].to_dict()
    print(dic)


top_headlines()
