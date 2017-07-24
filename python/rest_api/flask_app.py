#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from flask import jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlite3 import dbapi2 as sqlite

engine = create_engine('sqlite+pysqlite:///../sqlite/cafeDB.db', module=sqlite)
meta = MetaData()
meta.reflect(bind=engine)
meta.bind = engine
users_table = meta.tables['User']


def add_route(app):
    @app.route('/users/<id>', methods=['GET'])
    def get_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        print(id)
        result = users_table.select().where(users_table.c.id == id).execute().first()
        if result:
            return jsonify(dict(result.items()))
        else:
            return "User not found", 404
        return "Hello world"

    @app.route('/users', methods=["POST"])
    def new_user():
        body = request.get_json()
        try:
            username, intensity, volume = [body[k] for k in ("username", "intensity", "volume")]
        except KeyError:
            return "Incorrect body", 400

        id_max = engine.execute("SELECT seq FROM SQLITE_SEQUENCE WHERE name='User'").first()
        new_id = id_max[0] + 1
        stmt = users_table.insert().values(id=new_id, name=username, intensity=intensity, volume=volume)
        stmt.execute()
        result = users_table.select().where(users_table.c.id == new_id).execute().first()
        return jsonify(dict(result.items()))

    @app.route('/users/<id>', methods=["PUT"])
    def modify_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400

        find = users_table.select().where(users_table.c.id == id).execute().first()
        if find:
            body = request.get_json()
            username, intensity, volume = [body.get(k) for k in ("username", "intensity", "volume")]

            query = users_table.update().where(users_table.c.id == id)
            if username:
                query = query.values(name=username)
            if intensity:
                query = query.values(intensity=intensity)
            if volume:
                query = query.values(volume=volume)
            query.execute()

            result = users_table.select().where(users_table.c.id == id).execute().first()
            return jsonify(dict(result.items()))
        else:
            return "User not found", 404

    @app.route('/users/<id>', methods=["DELETE"])
    def delete_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400

        find = users_table.select().where(users_table.c.id == id).execute().first()
        if find:
            users_table.delete().where(users_table.c.id == id).execute()
            return "User succesfuly destroyed"
        else:
            return "User not found", 404
