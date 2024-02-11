from app import Song, db, app

song1 = Song(username="추천자", title="노래제목1",
             artist="가수1", image_url="이미지 주소1")

song2 = Song(username="스파르타", title="노래제목2",
             artist="가수2", image_url="이미지 주소2")

song3 = Song(username="스파르타", title="노래제목3",
             artist="가수3", image_url="이미지 주소3")

with app.app_context():
    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)

    db.session.commit()