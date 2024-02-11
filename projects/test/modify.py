from app import Song, db, app

with app.app_context():
    print(Song.query.all())
    song_data = Song.query.filter_by(id=3).first()
    song_data.title = '노래제목수정'
    db.session.add(song_data)
    db.session.commit()
    print(Song.query.all())
