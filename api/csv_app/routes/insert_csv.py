from csv_app import db
from csv_app.routes import bp


@bp.route('/insert_csv', methods=['GET'])
def insert_csv():
    return 'This is the insert CSV route'
