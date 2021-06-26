import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.kompas.com/tren')

hai = BeautifulSoup(html_doc.text, 'html.parser')

berita_trending = hai.find(attrs={'class': 'trenLatest'})
#print(berita_trending)

titles = berita_trending.findAll(attrs={'class': 'trenLatest__title'})
#for judul in titles:
#print(judul.text)

images = berita_trending.findAll(attrs={'class': 'trenLatest__img'})
#for gambar in images:
 #  print(gambar.find('a').find('img'))
 #  print(gambar.find('a').find('img')['alt'])
 #  print(gambar.find('a').find('img')['src'])
