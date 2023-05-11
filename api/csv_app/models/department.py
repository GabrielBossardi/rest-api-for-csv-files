from csv_app import db


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String)

    def __repr__(self):
        return '<Department %r>' % self.department
