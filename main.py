import os

from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from flask.ext.migrate import Migrate, MigrateCommand

from app import create_app
from app.models import db

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APP_ENV', 'dev')
app = create_app('app.settings.%sConfig' % env.capitalize())

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())
manager.add_command("db", MigrateCommand)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()


if __name__ == '__main__':
    manager.run()
