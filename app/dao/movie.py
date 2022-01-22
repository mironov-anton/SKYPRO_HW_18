from app.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_data):
        ent = Movie(**movie_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie
