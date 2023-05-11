# CSV Data Processing API

This project implements a CSV Data Processing API that allows you to upload CSV files, process the data, and retrieve relevant statistics. The API is built using Flask, SQLAlchemy, and Docker.

## Prerequisites

- Python 3.11
- Docker version 20.10.24 or higher
- Poetry version 1.4.2 or higher (see below for installation instructions)

## Quick Execution

To quickly run the CSV Data Processing API, follow these steps:

1. Install Docker by following the instructions at https://docs.docker.com/get-docker/.

2. Install Poetry by following the instructions at https://python-poetry.org/docs/#installation.

3. Clone this repository to your local machine.

4. In the project directory, open a terminal and run the command `poetry install` to install the project dependencies.

5. Start the Docker containers by running the command `docker-compose up` in the project directory.

6. Once the containers are up and running, you can access the API endpoints described above using a tool like cURL or an API testing tool like Postman.

7. Make requests to the API endpoints to upload CSV files and retrieve data.

## Endpoints

The CSV Data Processing API provides the following endpoints:

Note: The first endpoint, `/insert_csv`, needs to be executed before using the other endpoints to populate the tables with CSV data.

### 1. Insert CSV Data

- Method: GET
- URL: http://localhost:5001/insert_csv
- Request body (JSON): N/A
- Response body (JSON):
  ```json
  {
      "message": "CSV file uploaded and data inserted successfully"
  }
  ```

### 2. Employee Quarter Statistics
- Method: GET
- URL: http://localhost:5001/employee_quarter_stats
- Request body (JSON): N/A
- Response body (JSON):

    ```json
    [
        {
            "department": "Department 1",
            "job": "Job 1",
            "q1": 10,
            "q2": 12,
            "q3": 8,
            "q4": 15
        },
        {
            "department": "Department 2",
            "job": "Job 2",
            "q1": 5,
            "q2": 7,
            "q3": 6,
            "q4": 10
        },
        ...
    ]
    ```

### 3. Departments Above Average Hiring
- Method: GET
- URL: http://localhost:5001/departments_above_average_hiring
- Request body (JSON): N/A
- Response body (JSON):

    ```json
    [
        {
            "id": 1,
            "department": "Department 1",
            "hired": 25
        },
        {
            "id": 2,
            "department": "Department 2",
            "hired": 18
        },
        ...
    ]
    ```

## Database

This project uses a PostgreSQL database to store data. The database is deployed as a Docker container.

The `docker-compose.yml` file defines a service named `db` that runs the PostgreSQL image. The container is configured with the following environment variables:

- `POSTGRES_USER`: the username for the default PostgreSQL user.
- `POSTGRES_PASSWORD`: the password for the default PostgreSQL user.
- `POSTGRES_DB`: the name of the default PostgreSQL database.

In addition, the `docker-compose.yml` file runs an initialization script that creates three separate schemas in the database: `bronze`, `silver`, and `gold`. These schemas are based on the [Medallion architecture](https://www.databricks.com/glossary/medallion-architecture) and can be used to organize data at different levels of quality and complexity.

## REST API

This project uses a Flask web application to serve HTTP requests. The web application is deployed as a Docker container using Gunicorn as a WSGI server.

The `docker-compose.yml` file defines a service named `api` that builds the Docker image using the Dockerfile in the current directory. It maps port 5001 on the host to port 5000 in the container and starts the Gunicorn server.

The `api` service depends on the `db` service, which means that the `db` service will be started before the `api` service.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).
