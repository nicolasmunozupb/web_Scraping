import urllib

from scrapy.item import Field
from scrapy.item import Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider
import re;
from bs4 import BeautifulSoup;
import pandas as pd;
import requests;

url = "https://articulo.mercadolibre.com.co/MCO-515122915-sudadera-tactica-miltiples-bolsillos-y-colores-para-hombre-_JM?searchVariation=37816077494&quantity=1#searchVariation=37816077494&position=4&type=item&tracking_id=49224c38-ce04-46a1-b201-55b15b221699"

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
eq = soup.find_all('div', 'review-tooltip-full-body')
titulo=soup.find('header', class_='item-title').find('h1').text.strip()
precio=soup.find('span', class_='price-tag').find('span', class_='price-tag-fraction').text.strip()
print(titulo)
print(precio)
eq2 = list()
cont =0
for i in eq:
    if cont<=20:
     eq2.append(i.text)
    else:
        break
    cont +=1
print(eq2)