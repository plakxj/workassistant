from work import db

class Note(db.Model):
    from work import db
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String)
    keyword1 = db.Column(db.Text)
    keyword2 = db.Column(db.Text)
    text = db.Column(db.Text)

