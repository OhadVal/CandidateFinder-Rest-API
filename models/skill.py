from database import db, ma


# Model
class Skill(db.Model):
    __tablename__ = 'skill'
    skill_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Skill %r>' % self.name


# Schema
class SkillSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Skill
        fields = ('skill_id', 'name')
        include_fk = True

    links = ma.Hyperlinks(
        {
            "self": ma.URLFor("skill_blueprint.skill_detail", values=dict(id="<skill_id>")),
            "collection": ma.URLFor("skill_blueprint.skills"),
        }
    )


# Init Schema
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)
