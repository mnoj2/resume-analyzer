from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Candidate(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    raw_analysis = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
