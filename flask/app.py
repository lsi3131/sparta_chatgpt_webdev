import flask, random, requests
from flask import Flask

app = Flask(__name__)


def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)


def count_common_elements(list1, list2):
    common = set(list1) & set(list2)
    return len(common)


@app.route('/')
def home():
    name = "이상일"
    lotto = [16, 18, 20, 23, 32, 43]

    lotto_numbers = generate_lotto_numbers()
    print("추출된 로또 번호:", lotto_numbers)

    common_count = count_common_elements(lotto, lotto_numbers)

    context = {
        "name": name,
        "lotto": lotto,
        "random_lotto": lotto_numbers,
        "common_count": common_count
    }
    return flask.render_template('index.html', data=context)


@app.route('/movie')
def movie():
    print(flask.request.args.get('query'))
    query = flask.request.args.get('query')
    URL = (f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/"
           f"searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}")
    res = requests.get(URL)
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    print(movie_list)

    return flask.render_template('movie.html', data=movie_list)

@app.route('/answer')
def answer():
    query = flask.request.args.get('query')
    if len(query) == 0:
        query = '20230611'
    URL = (f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/"
           f"searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={query}")
    res = requests.get(URL)
    rjson = res.json()
    movie_list = rjson["boxOfficeResult"]["weeklyBoxOfficeList"]

    return flask.render_template('answer.html', data=movie_list)

@app.route('/mypage')
def mypage():
    return 'This is my page'


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5001)
