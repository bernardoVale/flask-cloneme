from flask import Blueprint
from app.models import Version, db
main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    v = Version()
    v.version = '0.4'
    v.latest = True
    db.session.add(v)
    db.session.commit()
    return v.version
