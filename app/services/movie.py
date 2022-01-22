from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        if filters.get("director_id"):
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id"):
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year"):
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_data):
        return self.dao.create(movie_data)

    def update(self, movie_data):
        mid = movie_data.get("id")
        movie = self.get_one(mid)
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")
        self.dao.update(movie)

    def update_partial(self, movie_data):
        mid = movie_data.get("id")
        movie = self.get_one(mid)
        if "title" in movie_data:
            movie.title = movie_data.get("title")
        if "description" in movie_data:
            movie.description = movie_data.get("description")
        if "trailer" in movie_data:
            movie.trailer = movie_data.get("trailer")
        if "year" in movie_data:
            movie.year = movie_data.get("year")
        if "rating" in movie_data:
            movie.rating = movie_data.get("rating")
        if "genre_id" in movie_data:
            movie.genre_id = movie_data.get("genre_id")
        if "director_id" in movie_data:
            movie.director_id = movie_data.get("director_id")
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
