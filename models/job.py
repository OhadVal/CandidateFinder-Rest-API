from database import db, ma
from models.linking_tables_many_to_many_relationships import job_skills
from models.skill import skill_schema


class Job(db.Model):
    __tablename__ = 'job'
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    skills = db.relationship('Skill', secondary=job_skills, backref=db.backref('job', lazy='dynamic'))

    def __repr__(self):
        return '<Job %r %r>' % (self.title, self.skills)


class JobSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Job
        fields = ('job_id', 'title', 'skills')
        include_fk = True

    skills = ma.Nested(skill_schema, many=True)
    link = ma.Hyperlinks(ma.URLFor("job_api.job_detail_by_id", values=dict(id="<job_id>")))


# Init Schema
job_schema = JobSchema()
jobs_schema = JobSchema(many=True)
