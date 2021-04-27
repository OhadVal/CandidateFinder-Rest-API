from database import db, ma
from models.linking_tables_many_to_many_relationships import candidate_skills


# Model
class Candidate(db.Model):
    __tablename__ = 'candidate'
    candidate_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    skills = db.relationship('Skill', secondary=candidate_skills, backref=db.backref('candidate', lazy='dynamic'))

    def __repr__(self):
        return '<Candidate %r %r>' % (self.title, self.skills)


# Schema
class CandidateSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Candidate
        fields = ('candidate_id', 'title', 'skills')
        include_fk = True


# Init Schema
candidate_schema = CandidateSchema()
candidates_schema = CandidateSchema(many=True)
