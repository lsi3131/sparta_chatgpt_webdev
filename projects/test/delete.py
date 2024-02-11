from app import Song, db, app

with app.app_context():
    print(Song.query.all())
    delete_data = Song.query.filter_by(id=3).first()
    db.session.delete(delete_data)
    db.session.commit()
    print(Song.query.all())
