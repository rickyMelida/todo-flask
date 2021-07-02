import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="mykey",
        DATABASE_HOST="localhost",  # os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD="",  # os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER="root",  # os.environ.get('FLASK_DATABASE_USER'),
        DATABASE="prueba",  # os.environ.get('FLASK_DATABASE'),
    )

    from . import db

    db.init_app(app)
    
    from . import auth
    from . import todo

    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route("/hola")
    def hola():
        return "Chanchito Feliz"

    return app
