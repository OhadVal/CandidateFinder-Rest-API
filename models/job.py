from database import db


class Job(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    skills = db.relationship('Skill', secondary='job_skills', backref=db.backref('job', lazy='dynamic'))
