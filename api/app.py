from csv_app import create_app, db
from flask_migrate import Migrate

app = create_app('development')
migrate = Migrate(app, db)

from csv_app.models.department import Department    # noqa: F401, E402
from csv_app.models.job import Job                  # noqa: F401, E402
from csv_app.models.employee import Employee        # noqa: F401, E402

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
