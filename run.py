import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kompas-trending')
def kompas_trending():
    html_doc = requests.get('https://www.kompas.com/tren')

    hai = BeautifulSoup(html_doc.text, 'html.parser')

    berita_trending = hai.find(attrs={'class': 'trenLatest'})

    titles = berita_trending.findAll(attrs={'class': 'trenLatest__title'})

    images = berita_trending.findAll(attrs={'class': 'trenLatest__img'})

    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)