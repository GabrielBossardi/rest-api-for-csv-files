from flask import jsonify
from csv_app.routes import bp
from csv_app.utils.file_handler import get_file_paths
from csv_app.utils.csv_handler import generate_dict
from csv_app.utils.insert_handler import full_refresh_batch_insert
from csv_app.models.department import Department
from csv_app.models.employee import Employee
from csv_app.models.job import Job


@bp.route('/insert_csv', methods=['GET'])
def insert_csv():
    """
    Endpoint for inserting data from CSV files into corresponding
        database tables.

    Returns:
        A JSON response indicating the success of the data insertion.
        HTTP status code 200 if successful, 400 if there is an error.
    """
    valid_files = ['departments', 'hired_employees', 'jobs']
    file_paths = get_file_paths(valid_files)

    # Metadata for each file, specifying table name, headers,
    # and corresponding model class
    files_metadata = {
        'departments': {
            'table_name': 'departments',
            'header': ['id', 'department'],
            'class': Department
        },
        'jobs': {
            'table_name': 'jobs',
            'header': ['id', 'job'],
            'class': Job
        },
        'hired_employees': {
            'table_name': 'employees',
            'header': ['id', 'name', 'datetime', 'department_id', 'job_id'],
            'class': Employee
        }
    }

    # Process each file and insert data into the corresponding table
    for key, value in file_paths.items():
        csv_data = generate_dict(value, files_metadata[key]['header'])

        try:
            full_refresh_batch_insert(
                files_metadata[key]['class'],
                csv_data,
                1000
            )
        except Exception as e:
            return jsonify(
                {'message': f'{e}'}
            ), 400

    return jsonify(
        {'message': 'CSV file uploaded and data inserted successfully'}
    ), 200
