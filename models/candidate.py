from database import db


class Candidate(db.Model):
    candidate_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    skills = db.relationship('Skill', secondary='candidate_skills', backref=db.backref('candidates', lazy='dynamic'))
