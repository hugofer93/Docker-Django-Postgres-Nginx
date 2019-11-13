FROM python:3.5-slim-buster

MAINTAINER hugofer93 hugofer93@gmail.com

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# NOTE: 'PIPENV_VENV_IN_PROJECT' disabled on purpose
#ENV PIPENV_VENV_IN_PROJECT=0

WORKDIR /home/

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/python3 /bin/python
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install pip --upgrade
RUN pip install pipenv

COPY . .

RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt
RUN rm requirements.txt
RUN touch source.env && chmod +x source.env
RUN sed -E -n 's/[^#]+/export &/ p' .env >> source.env
SHELL ["/bin/bash", "-c", "source source.env"]
RUN rm -f source.env
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic
RUN ls
RUN apt-get autoremove -y gcc

EXPOSE 8000

CMD ["uwsgi", "--http-socket", "project/project.sock", "--chmod-socket=666", "--wsgi-file", "project/wsgi.py", "--vacuum"]
