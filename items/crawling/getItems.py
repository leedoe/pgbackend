import json
import pprint
import environ
import os
import sys
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs
import django
from django.conf import settings


def getItemsFromMyLeatherTool():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    categories = ['4', '294', '25', '26', '9', '7', '113', '12']

    for category in categories:
        pageNumber = 1
        while True:
            response = requests.get(
                f'http://myleathertool.com/product/list.html?cate_no={category}&page={pageNumber}',
                headers=headers)
            soup = bs(response.text, 'lxml')
            itemsLi = soup.findAll('li', class_='item')
            if len(itemsLi) == 0:
                break
            
            for itemli in itemsLi:
                itemImg = f'http:{itemli.find("img", class_="thumb")["src"]}'
                itemName = itemli.find('p', class_='name').findAll('span')[1].text
                itemPrice = int(itemli.find('li', class_='product_price').findAll('span')[1].text.replace(',', '').replace('원', ''))
                link = f'http://myleathertool.com{itemli.find("a", class_="link")["href"]}'

                itemData.append({
                    'image': itemImg,
                    'title': itemName,
                    'price': itemPrice,
                    'link': link,
                    'soldout': False,
                    'homepage': '마이레더툴'
                })
            pageNumber += 1
    
    return itemData


def getItemsFromLeathercraftTool():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    categories = [
        ('실/215/', 52),
        ('지퍼/228/', 37),
        ('재단면-마감재/133/', 19),
        ('약품/134/', 13),
        ('공구/371/', 3),
        ('금속장식/220/', 28),
        ('펀치/363/', 24),
        ('각인/222/', 25),
        ('심재료/331/', 3),
        ('안감/632/', 6),
        ('부자재/729/', 5)
    ]

    for category, page in categories:
        pageNumber = 1
        while True:
            if pageNumber > page:
                break
            response = requests.get(
                f'http://leathercrafttool.co.kr/category/{category}?page={pageNumber}',
                headers=headers)
            soup = bs(response.text, 'lxml')
            itemsListUl = soup.find_all('ul', class_='prdList')
            if itemsListUl is None:
                break
            if len(itemsListUl) == 0:
                break

            if len(itemsListUl) != 1:
                itemsLi = itemsListUl[1].findAll('li', class_='xans-record-')
            else:
                itemsLi = itemsListUl[0].findAll('li', class_='xans-record-')

            for itemLi in itemsLi:
                try:
                    if itemLi['id'] is None:
                        continue
                except KeyError:
                    continue
                itemImg = f'http:{itemLi.find("div", class_="prdImg").find("img")["src"]}'
                itemName = itemLi.find("div", class_="prdImg").find("img")["alt"]
                itemPrice = itemLi \
                    .find('ul', class_='xans-element- xans-product xans-product-listitem spec') \
                    .findAll('span')[1].text.replace(',', '').replace('₩', '')
                try:
                    itemPrice = int(itemPrice)
                except ValueError:
                    itemPrice = 0
                link = f'http://leathercrafttool.co.kr{itemLi.find("a")["href"]}'

                itemData.append({
                    'image': itemImg,
                    'title': itemName,
                    'price': itemPrice,
                    'link': link,
                    'soldout': False,
                    'homepage': '다양상사'
                })
            pageNumber += 1
    return itemData


def getItemsFromLeatherNori():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    pageNumber = 1

    while True:
        response = requests.get(
            f'https://www.leathernori.com/shop/search_result.php?page={pageNumber}&search_str=&x=0&y=0&sort=',
            headers=headers)
        soup = bs(response.text, 'lxml')
        
        itemsDiv = soup.findAll('tbody')[1].findAll('div', class_='info')
        if len(itemsDiv) == 0:
            break

        for itemDiv in itemsDiv:
            itemImg = itemDiv.find('img')['src']
            itemName = itemDiv.find('p', class_='name').find('a').text
            itemPrice = int(itemDiv.find('span', class_='sell').text.replace(',', '').replace('원', ''))
            link = itemDiv.find('div', class_='img').find('a')['href']
            
            itemData.append({
                'image': itemImg,
                'title': itemName,
                'price': itemPrice,
                'link': link,
                'soldout': False,
                'homepage': '레더노리'
            })

        pageNumber += 1
    return itemData


def getItemsFromKingsLeather():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    pageNumber = 1

    while True:
        response = requests.get(
            f'http://www.campnews.co.kr/shop/goods/goods_search.php?searched=Y&page={pageNumber}',
            headers=headers)
        soup = bs(response.text, 'lxml')
        
        itemsTd = soup.find_all('td', attrs={'width': '25%', 'valign': 'top', 'align': 'center'})
        if len(itemsTd) == 0:
            break
        for itemTd in itemsTd:
            divs = itemTd.find_all('div')

            itemImg = divs[0].find('img')['src'].replace('..', 'http://www.campnews.co.kr/shop')
            itemName = itemTd.find('div', attrs={'style': 'padding:5'}).find('a').text
            priceDiv = itemTd.find('div', attrs={'style': 'padding-bottom:3px'})
            if priceDiv is None:
                continue
            itemPrice = int(priceDiv.find('b').text.replace(',', '').replace('원', ''))
            link = divs[0].find('a')['href'].replace('..', 'http://www.campnews.co.kr/shop')
            soldoutDiv = itemTd.find('div', attrs={'style': 'padding:3px'})
            if soldoutDiv is None:
                soldout = False
            else:
                soldout = True

            itemData.append({
                'image': itemImg,
                'title': itemName,
                'price': itemPrice,
                'link': link,
                'soldout': soldout,
                'homepage': '성안상사'
            })

        pageNumber += 1
    return itemData


def getItemsFromGoodNLeather():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    categories = ['239', '86', '141', '142', '91', '92', '93', '284', '277']

    for category in categories:
        pageNumber = 1
        while True:
            response = requests.get(
                f'https://goodnleather.com/product/list.html?cate_no={category}&page={pageNumber}',
                headers=headers)
            soup = bs(response.text, 'lxml')
            itemsLi = soup.findAll('li', class_='item')
            if len(itemsLi) == 0:
                break
            
            for itemli in itemsLi:
                itemImg = f'https:{itemli.find("img")["src"]}'
                itemName = itemli.find('p', class_='name').findAll('span')[2].text
                itemPrice = int(itemli.find('ul', class_='xans-element- xans-product xans-product-listitem spec').find_all('span')[1].text.replace(',', '').replace('원', ''))
                link = f'https://goodnleather.com{itemli.find("a")["href"]}'
                soldout = itemli.find('img', attrs={'alt': '품절'})
                if soldout is None:
                    soldout = False
                else:
                    soldout = True

                itemData.append({
                    'image': itemImg,
                    'title': itemName,
                    'price': itemPrice,
                    'link': link,
                    'soldout': soldout,
                    'homepage': '굿앤레더'
                })
            pageNumber += 1

    return itemData


def getItemsFromLeatherfeel():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    categories = ['75', '85', '101', '77', '71', '76', '51', '175', '174']

    for category in categories:
        pageNumber = 1
        while True:
            response = requests.get(
                f'http://www.leatherfeel.kr/product/list.html?cate_no={category}&page={pageNumber}',
                headers=headers)
            soup = bs(response.text, 'lxml')
            itemsLi = soup.find_all('li', class_='item xans-record-')
            if len(itemsLi) == 0:
                break
            
            for itemli in itemsLi:
                itemImg = f'http:{itemli.find("img")["src"]}'
                itemName = itemli.find('p', class_='name').findAll('span')[1].text
                try:
                    price = itemli.find('ul', class_='xans-element- xans-product xans-product-listitem').find('font', attrs={'color': 'red'})
                except AttributeError:
                    continue
                
                if price is None:
                    try:
                        itemPrice = int(itemli.find('ul', class_='xans-element- xans-product xans-product-listitem').find_all('span')[1].text.replace('원', ''))
                    except ValueError:
                        # itemPrice = itemli.find('ul', class_='xans-element- xans-product xans-product-listitem').find_all('span')[1].text.replace('원', '')
                        continue
                else:
                    try:
                        itemPrice = int(price.text.replace('원', ''))
                    except ValueError:
                        # itemPrice = price.text.replace('원', '')
                        continue
                link = f'http://www.leatherfeel.kr{itemli.find("a")["href"]}'
                soldout = itemli.find('img', attrs={'alt': '품절'})
                if soldout is None:
                    soldout = False
                else:
                    soldout = True

                itemData.append({
                    'image': itemImg,
                    'title': itemName,
                    'price': itemPrice,
                    'link': link,
                    'soldout': soldout,
                    'homepage': '레더필'
                })
            pageNumber += 1
    return itemData


def getItemsFromSeiwa():
    headers = {
        'User-Agent': 'PostmanRuntime/7.26.2'
    }
    itemData = []
    categories = ['103']

    for category in categories:
        pageNumber = 1
        while True:
            response = requests.get(
                f'https://seiwa-net.kr/product/list.html?cate_no={category}&page={pageNumber}',
                headers=headers)
            soup = bs(response.text, 'lxml')
            itemsUl = soup.find('ul', class_='prdList grid5')
            if itemsUl is None:
                break
            itemsLi = itemsUl.find_all('li', id=re.compile('anchorBoxId_*'))

            for itemli in itemsLi:
                itemImg = f'https:{itemli.find("img")["src"]}'
                itemName = itemli.find("img")["alt"]
                try:
                    price = itemli.find_all('span', attrs={'style': 'font-size:13px;color:#000000;font-weight:bold;'})[1]
                    itemPrice = price.text.replace('원', '').replace(',', '')
                except IndexError:
                    continue
                link = f'https://seiwa-net.kr{itemli.find("a")["href"]}'
                soldout = itemli.find('img', attrs={'alt': '품절'})
                if soldout is None:
                    soldout = False
                else:
                    soldout = True

                itemData.append({
                    'image': itemImg,
                    'title': itemName,
                    'price': itemPrice,
                    'link': link,
                    'soldout': soldout,
                    'homepage': '세이와'
                })
            pageNumber += 1
    return itemData



items = []
items += getItemsFromMyLeatherTool()
items += getItemsFromLeathercraftTool()
items += getItemsFromLeatherNori()
items += getItemsFromKingsLeather()
items += getItemsFromGoodNLeather()
items += getItemsFromLeatherfeel()
items += getItemsFromSeiwa()

# print(len(items))
# with open('./items.json', 'w', encoding='utf8') as fp:
#     json.dump(items, fp, ensure_ascii=False)


####
PROJECT_ROOT = Path(os.path.realpath(__file__)).parent.parent
sys.path.append(os.path.dirname(PROJECT_ROOT))
# print(sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgbackend.settings.local")
env = environ.Env()

# settings.configure(default_settings=env('DJANGO_SETTINGS_MODULE'), DEBUG=True)
django.setup()

from items.models import Item
from users.models import User

# with open('./items/crawling/items.json', 'r', encoding='utf8') as fp:
#     items = json.load(fp)

Item.objects.all().delete()
item_instances = []
for item in items:
    item_instances.append(Item(
        name=item['title'],
        thumbnail=item['image'],
        price=item['price'],
        link=item['link'],
        soldout=item['soldout'],
        store_name=item['homepage']
    ))

Item.objects.bulk_create(item_instances)