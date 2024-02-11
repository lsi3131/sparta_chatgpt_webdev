import os
import flask
from flask import Flask, render_template
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = 'sqlite:///' + os.path.join(basedir, 'database.db')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbpath
db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.artist} {self.title} 추천 by {self.username}'


@app.route("/")
def home():
    name = '이상일'
    motto = '행복은 현재 당연히 누려야할 것이다'
    context = {
        "name": name,
        "motto": motto
    }
    return render_template("motto.html", data=context)


@app.route("/iloveyou/<name>")
def iloveyou(name):
    motto = f'{name}야 행복해라'
    context = {
        "name": name,
        "motto": motto
    }
    return render_template("motto.html", data=context)


@app.route('/music/')
def music():
    songs_list = Song.query.all()
    return render_template('music.html', data=songs_list)

@app.route('/music/<username>/')
def render_music_filter(username):
    filter_list = Song.query.filter_by(username=username).all()
    return render_template('music.html', data=filter_list)


@app.route('/music/create')
def music_create():
    username_receive = flask.request.args.get("username")
    title_receive = flask.request.args.get("title")
    artist_receive = flask.request.args.get("artist")
    image_receive = flask.request.args.get("image_url")

    song = Song(username=username_receive, title=title_receive, artist=artist_receive, image_url=image_receive)
    with app.app_context():
        db.session.add(song)
        db.session.commit()

    return flask.redirect(flask.url_for('render_music_filter', username=username_receive))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
