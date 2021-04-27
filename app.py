from flask import Flask
from api.Candidate.candidate_api import candidate_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configurations from Config class

    from database import db, ma
    # Init SQLAlchemy and Marshmallow
    db.init_app(app)
    ma.init_app(app)

    # Register Flask Blueprints
    app.register_blueprint(candidate_blueprint, url_prefix='/api/')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
