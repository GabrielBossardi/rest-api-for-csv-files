from csv_app import db


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    datetime = db.Column(db.String)
    department_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Employee %r>' % self.name
