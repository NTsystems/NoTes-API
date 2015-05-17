#
# This docker configuration is used to build production-ready
# notes API container.
#
FROM phusion/baseimage:0.9.16
MAINTAINER Dejan Mijic <dejan.mjc@gmail.com>

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Environment variables
ENV NOTES_HOME /opt/nt-notes

# Install dependencies
RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip \
    libpq-dev \
    libyaml-dev \
    nginx

RUN pip install uwsgi

# uWSGI
ADD ./config/uwsgi.ini /opt/nt-notes/config/uwsgi.ini
ADD ./config/uwsgi.params /opt/nt-notes/config/uwsgi.params

# nginx
RUN rm -f /etc/nginx/sites-enabled/default
ADD ./config/nginx.conf /etc/nginx/sites-enabled/notes.conf

# Add runits
RUN mkdir /etc/service/nginx
ADD ./config/nginx.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run
RUN mkdir /etc/service/notes
ADD ./config/uwsgi.sh /etc/service/notes/run
RUN chmod +x /etc/service/notes/run

# Copy the app sources
RUN mkdir -p /opt/nt-notes
ADD ./notes /opt/nt-notes/notes/
ADD ./manage.py /opt/nt-notes/manage.py
ADD ./requirements /opt/nt-notes/requirements/
ADD ./requirements.txt /opt/nt-notes/requirements.txt

# Initialize app
WORKDIR /opt/nt-notes
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

# Expose ports
EXPOSE 80

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
