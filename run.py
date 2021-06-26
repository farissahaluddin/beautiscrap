import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    data_idr_json = source.json()
    return render_template('idr-rates.html', datas=data_idr_json.values())


@app.route('/kompas-trending')
def kompas_trending():
    html_doc = requests.get('https://www.kompas.com/tren')

    hai = BeautifulSoup(html_doc.text, 'html.parser')

    berita_trending = hai.find(attrs={'class': 'trenLatest'})

    titles = berita_trending.findAll(attrs={'class': 'trenLatest__title'})

    images = berita_trending.findAll(attrs={'class': 'trenLatest__img'})

    return render_template('kompas-scrap.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)