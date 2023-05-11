from flask import Blueprint


bp = Blueprint('main', __name__)

from csv_app.routes import insert_csv               # noqa: F401, E402
from csv_app.routes import employee_quarter_stats   # noqa: F401, E402
