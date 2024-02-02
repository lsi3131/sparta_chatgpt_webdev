from bs4 import BeautifulSoup
import requests

url = "https://www.melon.com/chart/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

rankers = soup.select_one('.lst50')
# print(rankers)

trs = soup.select('.lst50') + soup.select('.lst100')
for tr in trs:
    rank = tr.select_one('.rank').text
    title = tr.select_one('.rank01 > span > a').text
    artist = tr.select_one('.rank02 > a').text
    image = tr.select_one('img')['src']

    print(rank, artist, "-", title, image)

# trs = soup.select('.lst100')
