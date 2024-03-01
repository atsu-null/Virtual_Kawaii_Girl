from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Take(db.Model):
    __tablename__ = "takes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    take = db.Column(db.Text)
    