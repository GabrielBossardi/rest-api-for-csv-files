### Prerequisites

- Python 3.11
- Docker version 20.10.24 or higher
- Poetry version 1.4.2 or higher (see below for installation instructions)

### Docker Installation

To install Docker, please follow the installation instructions at https://docs.docker.com/get-docker/.

### Poetry Installation

If you don't have Poetry installed on your system yet, please follow the installation instructions at https://python-poetry.org/docs/#installation.

With Poetry installed, you can install the project dependencies by running `poetry install`.

### Database

This project uses a PostgreSQL database to store data. The database is deployed as a Docker container.

The `docker-compose.yml` file defines a service named `db` that runs the PostgreSQL image. The container is configured with the following environment variables:

- POSTGRES_USER: the username for the default PostgreSQL user.
- POSTGRES_PASSWORD: the password for the default PostgreSQL user.
- POSTGRES_DB: the name of the default PostgreSQL database.

In addition, the `docker-compose.yml` file runs an initialization script that creates three separate schemas in the database: `bronze`, `silver`, and `gold`. These schemas are based on the [Medallion architecture](https://www.databricks.com/glossary/medallion-architecture) and can be used to organize data at different levels of quality and complexity.

### REST API

This project uses a Flask web application to serve HTTP requests. The web application is deployed as a Docker container using Gunicorn as a WSGI server.

The `docker-compose.yml` file defines a service named `api` that builds the Docker image using the Dockerfile in the current directory. It maps port 5001 on the host to port 5000 in the container and starts the Gunicorn server.

The `api` service depends on the `db` service, which means that the `db` service will be started before the `api` service.
