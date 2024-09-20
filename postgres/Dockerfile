FROM postgres:latest
ENV POSTGRES_PASSWORD=S4p3rP4SS
ENV POSTGRES_DB=DB_SERVICIO

COPY psql_dump.sql /docker-entrypoint-initdb.d/
