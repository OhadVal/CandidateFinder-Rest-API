from database import db

# Stores skills for candidates
candidate_skills = db.Table(
    'candidate_skills',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.skill_id')),
    db.Column('candidate_id', db.Integer, db.ForeignKey('candidate.candidate_id')),
)

# Stores skills for jobs
job_skills = db.Table(
    'job_skills',
    db.Column('job_id', db.Integer, db.ForeignKey('job.job_id')),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.skill_id'))
)
