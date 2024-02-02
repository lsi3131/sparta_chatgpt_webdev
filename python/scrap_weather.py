import requests
from bs4 import BeautifulSoup

#URL = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=날씨"
URL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98+%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&tqi=ik44%2Flqo1aVssDdpMo0ssssst8G-325682"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

weather_info = soup.select('.weather_info')
weather_info2 = soup.select_one('.weather_info').contents

temperature_text = soup.select_one('.temperature_text')
print(temperature_text)

temperature_text_contents = soup.select_one('.temperature_text > strong').contents
print(temperature_text_contents)
print(temperature_text_contents[1])


# temperature_text_strong = soup.select_one('.temperature_text > strong')
# print(temperature_text_strong)
# print(temperature_text.text)
# print(temperature_text_strong.contents)

temp = soup.select_one('.temperature_text > strong').contents[1]
cloud = soup.select_one('.weather').text
humid = soup.select_one('.summary_list > div:nth-child(2) > dd').text
wind = soup.select_one('.summary_list > div:nth-child(3) > dd').text

# print(temp, cloud, humid, wind)