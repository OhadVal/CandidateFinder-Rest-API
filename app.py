from flask import Flask
from api.Skill.skill_api import *
from api.Job.job_api import *
from api.Candidate.candidate_api import *
from database import db, ma
from models.candidate import CandidateSchema
from models.job import JobSchema
# Swagger imports
from flasgger import APISpec, Swagger
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin


def create_app():
    # ---------- App Configuration ----------
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load configurations from Config class

    # Init SQLAlchemy and Marshmallow
    db.init_app(app)
    ma.init_app(app)

    # Register Flask Blueprints
    app.register_blueprint(candidate_blueprint, url_prefix='/api/')
    app.register_blueprint(job_blueprint, url_prefix='/api/')
    app.register_blueprint(skill_blueprint, url_prefix='/api/')

    # ---------- Swagger ----------

    # Create an APISpec
    spec = APISpec(
        title='CandidateFinder REST API',
        version='1.0',
        openapi_version='2.0',
        plugins=[FlaskPlugin(), MarshmallowPlugin()]
    )
    template = spec.to_flasgger(app, definitions=[CandidateSchema, JobSchema])

    # Set the UIVERSION to 3
    app.config['SWAGGER'] = {'uiversion': 3}

    # Start Flasgger using a template from APISpec
    swag = Swagger(app, template=template)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'])
