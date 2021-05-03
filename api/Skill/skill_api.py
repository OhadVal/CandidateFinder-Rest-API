from flasgger import swag_from
from flask import jsonify, Blueprint

from database import db
from models.skill import skills_schema, Skill, skill_schema

skill_blueprint = Blueprint('skill_blueprint', __name__)


@skill_blueprint.route("/skills/")
@swag_from('skills.yaml')
def skills():
    all_skills = Skill.query.all()
    return jsonify(skills_schema.dump(all_skills))


@skill_blueprint.route("/skills/<int:id>")
@swag_from('skill_detail_by_id.yaml')
def skill_detail_by_id(id):
    skill = Skill.query.get_or_404(id)
    return skill_schema.dump(skill)


@skill_blueprint.route('/skills/<string:skill_name>')
@swag_from('skill_detail_by_name.yaml')
def skill_detail_by_name(skill_name):
    found_skill = Skill.query.filter_by(name=skill_name).first_or_404(
        description=f'There is no data with - {skill_name}')
    return skill_schema.dump(found_skill)


@skill_blueprint.route('/skills/<string:skill_id>', methods=['DELETE'])
@swag_from('delete_skill.yaml')
def delete_skill(skill_id):
    skill = Skill.query.get_or_404(skill_id)
    db.session.delete(skill)
    db.session.commit()
    return skill_schema.dump(skill)
