print('\033c');from bs4 import BeautifulSoup;import requests;print(BeautifulSoup(requests.get('https://example.com').content, 'html.parser').find('th', attrs={'h2':'article-title'}).text)