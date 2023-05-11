from csv_app import db


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String)

    def __repr__(self):
        return '<Job %r>' % self.job
