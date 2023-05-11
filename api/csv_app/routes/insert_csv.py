from csv_app import db
from csv_app.routes import bp
from csv_app.utils.file_handler import get_file_paths
from csv_app.utils.csv_handler import generate_dict
from csv_app.models.department import Department


@bp.route('/insert_csv', methods=['GET'])
def insert_csv():
    valid_files = ['departments']
    file_paths = get_file_paths(valid_files)

    files_metadata = {
        'departments': {
            'table_name': 'departments',
            'header': ['id','department'],
        },
        'hired_employees': {
            'table_name': 'employees',
            'header': ['id','name','datetime','department_id','job_id'],
        },
        'jobs': {
            'table_name': 'jobs',
            'header': ['id','job'],
        }
    }

    for key, value in file_paths.items():
        table_name = files_metadata[key]['table_name']
        csv_data = generate_dict(value, files_metadata[key]['header'])

        try:
            db.session.bulk_insert_mappings(Department, csv_data)
            db.session.commit()
            return 'Success'
        except:
            return 'Error'
