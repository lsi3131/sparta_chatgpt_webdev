from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

url = "https://www.melon.com/chart/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/melon')
def melon():
    data_list = []
    trs = soup.select('.lst50') + soup.select('.lst100')
    for tr in trs:
        rank = tr.select_one('.rank').text
        title = tr.select_one('.rank01 > span > a').text
        artist = tr.select_one('.rank02 > a').text
        image_url = tr.select_one('img')['src']
        data_list.append({'title' : title, 'artist' : artist, 'image_url' : image_url})

    context = data_list
    return render_template('index.html', data=context)

if __name__ == '__main__':
    app.run(debug=True, port=5000)