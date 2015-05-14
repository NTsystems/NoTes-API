#!/bin/sh

exec /usr/bin/nginx -c /etc/nginx/nginx.conf -g "daemon off;"
