from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns


def create_app(config_object: Config):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    configure_app(application)
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)


if __name__ == '__main__':
    app = create_app(Config())
    app.run()  # debug set in config
