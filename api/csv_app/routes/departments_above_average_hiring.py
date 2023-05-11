from flask import jsonify
from csv_app import db
from csv_app.routes import bp
from csv_app.models.department import Department
from csv_app.models.employee import Employee
from sqlalchemy import func, cast
from sqlalchemy.types import Date


@bp.route("/departments_above_average_hiring", methods=["GET"])
def departments_above_average_hiring():
    """
    Retrieves the departments with hiring above the average.

    Returns:
        A JSON response containing the department IDs, names, and the number
            of employees hired above the average.
        HTTP status code 200 if successful, 400 if there is an error.
    """
    try:
        # Query to calculate the number of employees hired per department
        hiring_by_department = db.session.query(
            Department.id,
            Department.department,
            func.count().label('hired')
        ).join(Employee, Department.id == Employee.department_id).filter(
            func.date_trunc(
                'year', cast(Employee.datetime, Date)
            ) == '2021-01-01'
        ).group_by(Department.id, Department.department).subquery()

        # Query to calculate the average number of employees hired
        # across departments
        final = db.session.query(
            hiring_by_department.c.id,
            hiring_by_department.c.department,
            hiring_by_department.c.hired,
            func.avg(hiring_by_department.c.hired).over()
                .label('avg_employees_hired')
        ).select_from(hiring_by_department).subquery()

        # Query to retrieve the departments with hiring above the average,
        # sorted in descending order
        results = db.session.query(
            final.c.id,
            final.c.department,
            final.c.hired
        ).filter(final.c.hired > final.c.avg_employees_hired).order_by(
            final.c.hired.desc()
        ).all()

        output = []
        for row in results:
            id, department, hired = row
            output.append({
                'id': id,
                'department': department,
                'hired': hired
            })
    except Exception as e:
        return jsonify(
            {'message': f'{e}'}
        ), 400

    return jsonify(output), 200
