from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.genre import GenreSchema
from app.container import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        req_json = request.json
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200

    def put(self, gid: int):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update(req_json)
        return "", 204

    def patch(self, gid: int):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = gid
        genre_service.update_partial(req_json)
        return "", 204

    def delete(self, gid: int):
        genre_service.delete(gid)
        return "", 204
