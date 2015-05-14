#
# This docker configuration is used to build production-ready
# notes API container.
#
FROM phusion/baseimage:0.9.16
MAINTAINER Dejan Mijic <dejan.mjc@gmail.com>

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Environment variables
ENV NOTES_HOME /opt/api

# Update package repositories
RUN apt-get update && apt-get upgrade -y

# Install dependencies
RUN apt-get install -y python-dev python-pip libpq-dev nginx
RUN pip install fabric uwsgi

# Copy the app sources
RUN mkdir -p /opt/api
ADD ./notes /opt/api/notes/
ADD ./fabfile.py /opt/api/fabfile.py
ADD ./requirements /opt/api/requirements/
ADD ./requirements.txt /opt/api/requirements.txt

# Initialize app
WORKDIR /opt/api
RUN pip install -r requirements.txt

# Database setup

# Server setup
RUN rm -f /etc/nginx/sites-enabled/default

# Expose ports
EXPOSE 80

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
