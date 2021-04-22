from flask import Flask

from database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configurations from Config class
    db.init_app(app)
    return app

#
# @app.route('/')
# def index():
#     return 'Hello Worlds'


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['Debug'], host='0.0.0.0')
