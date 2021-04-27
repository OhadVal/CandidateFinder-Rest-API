from database import db, ma


# Model
class Skill(db.Model):
    __tablename__ = 'skill'
    skill_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    # jobs = db.relationship('Job', secondary='job_skills', backref='job_skill', lazy='dynamic')
    # candidates = db.relationship('Candidate', secondary='candidate_skills', backref='candidate_skill', lazy='dynamic')

    def __repr__(self):
        return '<Skill %r>' % self.name


# Schema
class SkillSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Skill
        fields = ('skill_id', 'name')
        include_fk = True


# Init Schema
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)
