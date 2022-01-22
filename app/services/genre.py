from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_data):
        return self.dao.create(genre_data)

    def update(self, genre_data):
        gid = genre_data.get("id")
        genre = self.get_one(gid)
        genre.name = genre_data.get("name")
        self.dao.update(genre)

    def update_partial(self, genre_data):
        gid = genre_data.get("id")
        genre = self.get_one(gid)
        if "name" in genre_data:
            genre.name = genre_data.get("name")
        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)
