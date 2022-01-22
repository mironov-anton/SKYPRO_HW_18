from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from services.director import DirectorService
from services.genre import GenreService
from services.movie import MovieService
from app.setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
