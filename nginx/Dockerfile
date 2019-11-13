FROM nginx:latest

MAINTAINER hugofer93 hugofer93@gmail.com

WORKDIR /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf

COPY ./sites-available/site.conf /etc/nginx/conf.d/
