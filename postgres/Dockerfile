FROM postgres:9.6

MAINTAINER hugofer93 hugofer93@gmail.com

# SUPERUSER FOR POSTGRES
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

# GENERATE SCHEMA
COPY ./init/01-db_setup.sh /docker-entrypoint-initdb.d/01-db_setup.sh

EXPOSE 5432
