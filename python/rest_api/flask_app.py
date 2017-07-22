#!/usr/bin/env python3
# -*- encoding: UTF-8 -*-

from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from sqlite3 import dbapi2 as sqlite

engine = create_engine('sqlite+pysqlite:///../sqlite/cafeDB.db', module=sqlite)
meta = MetaData()
meta.reflect(bind=engine)
meta.bind = engine
users_table = meta.tables['User']


def add_route(app, methods=['GET']):
    @app.route('/users/<id>')
    def hello(id):
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
