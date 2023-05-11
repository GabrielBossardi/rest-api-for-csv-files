from csv_app import db
from csv_app.routes import bp
from csv_app.utils.file_handler import get_file_paths


@bp.route('/insert_csv', methods=['GET'])
def insert_csv():
    valid_files = ['departments', 'hired_employees', 'jobs']
    file_paths = get_file_paths(valid_files)

    return f'These are the files: {file_paths}'
