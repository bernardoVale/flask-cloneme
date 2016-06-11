from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Version(db.Model):

    __tablename__ = 'version'

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String, nullable=True)
    latest = db.Column(db.Boolean, nullable=False)


class Another(db.Model):

    __tablename__ = 'another'

    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String, nullable=True)