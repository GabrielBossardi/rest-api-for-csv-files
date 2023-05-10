# Use an official Postgres runtime as a parent image
FROM postgres:13

# Copy the SQL script to create schemas into the container at /docker-entrypoint-initdb.d/
COPY create_schemas.sql /docker-entrypoint-initdb.d/
