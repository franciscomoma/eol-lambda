# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import re

url = 'http://www.elotrolado.net'  # TODO: Search if I can set the URL passing parameters from lambda


def listEOLNews(event, context):

    parameters = dict()
    if 'queryStringParameters' in event:
        parameters = event['queryStringParameters']

    try:
        markup = requests.get(url, params=parameters)
    except Exception as e:
        return { 
            'isBase64Encoded': False,
            'statusCode': 404,
            'body': json.dumps({'message': 'Service is currently unavailable', 'error': str(e)})
        }

    soup = BeautifulSoup(markup.text, 'html.parser')

    news = soup.find_all("div", class_='new')

    results = list()

    for new in news:
        mapped_new = dict()

        mapped_new['title'] = new.h2.a.get('title', '')
        mapped_new['link'] = new.find(class_="cm").get('href', None)
        mapped_new['comments'] = new.find(class_="cm").text
        mapped_new['summary'] = new.find('div', class_='body').text
        mapped_new['datetime'] = new.time.get('datetime', None)
        mapped_new['author'] = new.find(class_="author").span.text
        mapped_new['category'] = new.find(class_="newcat").get('href', None)

        mapped_new['thumbnail'] = None
        thumbnail = re.search(r'(https://[a-zA-Z0-9_\-\.\/]+)', new.find('a', class_="thumb")['style'])
        if thumbnail:
            mapped_new['thumbnail'] = thumbnail[0]

        results.append(mapped_new)

    response = dict()
    response['results'] = results

    next_news = soup.find(id="news-next")
    response['next'] = ''
    if next_news:
        response['next'] = next_news.get('href', '')

    prev_news = soup.find(id="news-prev")
    response['previous'] = ''
    if prev_news:
        response['previous'] = prev_news.get('href', '')

    return { 
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': json.dumps(response, ensure_ascii=False)
        }


print(listEOLNews(dict(), dict()))  # TODO: Look a better way to handle this
