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
    ''' Add routes to a flask app Class. See API swagger doc'''
    @app.route('/users/<id>', methods=['GET'])
    def get_user(id):
        try:
            id = int(id)
        except ValueError:
            return "Invalid id", 400
        print(id)
        result = users_table.select().where(users_table.c.id == id).execute().first()
        if result:
            return jsonify(dict(result.items())), 200
        else:
            return "User not found", 404

    @app.route('/users', methods=["POST"])
    def new_user():
        body = request.get_json()
        try:
            username, intensity, volume = [body[k] for k in ("username", "intensity", "volume")]
        except (KeyError, TypeError):
            return "Incorrect body", 400

        # Because sqlite engine cannot return created tuple, it's not possible to get the id after creation.
        # So we retrieve it.
        id_max = engine.execute("SELECT seq FROM SQLITE_SEQUENCE WHERE name='User'").first()
        new_id = id_max[0] + 1
        stmt = users_table.insert().values(id=new_id, username=username, intensity=intensity, volume=volume)
        stmt.execute()
        # Get the create users.
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
                query = query.values(username=username)
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
    def remove_user(id):
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

    @app.route('/recognition', methods=["POST"])
    def recognize_faceimage():
        if 'image' not in request.files:
            print('No file part')
            return "no image", 401
        file = request.files['image']
        if file.filename == '':
            return "Bad REquest", 400
        file.save(file.filename)

        print("Image received")
        return "OK", 200
