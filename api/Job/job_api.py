from flasgger import swag_from
from flask import Blueprint, jsonify, request

from database import db
from models.job import Job, jobs_schema, job_schema
from models.skill import Skill

job_blueprint = Blueprint('job_blueprint', __name__)


@job_blueprint.route("/jobs/")
@swag_from('jobs.yaml')
def get_all_jobs():
    """
        Gets all jobs in DB
        Returns: JSON Object
    """
    all_jobs = Job.query.all()
    return jsonify(jobs_schema.dump(all_jobs))


@job_blueprint.route("/jobs/<int:id>")
@swag_from('job_detail_by_id.yaml')
def job_detail_by_id(id):
    """
        Gets a job from DB by id
        Args:
            id: desired job id
        Returns: JobSchema Object

    """
    _job = Job.query.get_or_404(id)
    return job_schema.dump(_job)


@job_blueprint.route('/jobs/<string:job_title>')
@swag_from('job_detail_by_title.yaml')
def job_detail_by_title(job_title):
    """
        Gets a job from DB by title
        Args:
            job_title: desired job title
        Returns: JobSchema Object

        """
    found_job = Job.query.filter_by(title=job_title).first_or_404(
        description=f'There is no data with - {job_title}')
    return job_schema.dump(found_job)


@job_blueprint.route('/jobs', methods=['POST'])
@swag_from('job.yaml')
def add_new_job():
    """
        Request Example:
        {
        "job_title": "Software Engineer",
        "job_skills": [ "Python", "Flask", "Django", "AWS" ]
        }

        CURL example:
        curl -i -H "Content-Type: application/json" -X POST -d '{"job_title": "Software Engineer",
        "job_skills": ["Python", "Flask", "Django", "AWS"]}' http://localhost:5000/api/jobs

        Returns: JobSchema Object

    """

    data = request.get_json(force=True)
    new_job = Job(title=data["job_title"])

    # Add skills to job
    for skill_name in data["job_skills"]:
        # Find skill in DB:
        skill = Skill.query.filter_by(name=skill_name).first()

        # check if skill already in DB:
        skill_exist_in_table = skill is not None
        if not skill_exist_in_table:
            # Create new skill row in DB
            skill = Skill(name=skill_name)
            db.session.add(skill)  # store in DB

        # add required skill to job opening
        new_job.skills.append(skill)

    db.session.add(new_job)
    db.session.commit()
    return job_schema.dump(new_job)
