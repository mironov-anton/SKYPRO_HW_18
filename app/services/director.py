from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_data):
        return self.dao.create(director_data)

    def update(self, director_data):
        did = director_data.get("id")
        director = self.get_one(did)
        director.name = director_data.get("name")
        self.dao.update(director)

    def update_partial(self, director_data):
        did = director_data.get("id")
        director = self.get_one(did)
        if "name" in director_data:
            director.name = director_data.get("name")
        self.dao.update(director)

    def delete(self, did):
        self.dao.delete(did)
