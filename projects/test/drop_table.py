from app import Song, db, app

with app.app_context():
    db.drop_all()