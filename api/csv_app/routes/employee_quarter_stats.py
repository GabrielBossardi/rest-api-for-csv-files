from flask import jsonify
from csv_app import db
from csv_app.routes import bp
from csv_app.models.department import Department
from csv_app.models.employee import Employee
from csv_app.models.job import Job
from sqlalchemy import func, cast
from sqlalchemy.types import Date


@bp.route("/employee_quarter_stats", methods=["GET"])
def employee_quarter_stats():
    try:
        values_by_quarter = (
            db.session.query(
                Department.department,
                Job.job,
                func.extract("quarter", cast(Employee.datetime, Date))
                    .label("quarter"),
                func.count().label("employees_hired"),
            )
            .join(Department, Employee.department_id == Department.id)
            .join(Job, Employee.job_id == Job.id)
            .filter(
                func.date_trunc(
                    "year",
                    cast(Employee.datetime, Date)
                ) == "2021-01-01"
            )
            .group_by(
                Department.department,
                Job.job,
                func.extract("quarter", cast(Employee.datetime, Date)),
            )
            .subquery()
        )

        final = (
            db.session.query(
                values_by_quarter.c.department,
                values_by_quarter.c.job,
                func.sum(values_by_quarter.c.employees_hired)
                .filter(values_by_quarter.c.quarter == 1)
                .label("q1"),
                func.sum(values_by_quarter.c.employees_hired)
                .filter(values_by_quarter.c.quarter == 2)
                .label("q2"),
                func.sum(values_by_quarter.c.employees_hired)
                .filter(values_by_quarter.c.quarter == 3)
                .label("q3"),
                func.sum(values_by_quarter.c.employees_hired)
                .filter(values_by_quarter.c.quarter == 4)
                .label("q4"),
            )
            .group_by(values_by_quarter.c.department, values_by_quarter.c.job)
            .subquery()
        )

        results = (
            db.session.query(
                final.c.department,
                final.c.job,
                func.coalesce(final.c.q1, 0).label("q1"),
                func.coalesce(final.c.q2, 0).label("q2"),
                func.coalesce(final.c.q3, 0).label("q3"),
                func.coalesce(final.c.q4, 0).label("q4"),
            )
            .order_by(final.c.department, final.c.job)
            .all()
        )

        output = []
        for row in results:
            department, job, q1, q2, q3, q4 = row
            output.append(
                {
                    "department": department,
                    "job": job,
                    "q1": q1,
                    "q2": q2,
                    "q3": q3,
                    "q4": q4,
                }
            )
    except Exception as e:
        return jsonify(
            {'message': f'{e}'}
        ), 400

    return jsonify(output), 200
