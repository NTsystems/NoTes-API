"""Contains repetitive task definitions."""
from fabric.api import *


def _manage(task):
    """Invokes manage.py.

    Function uses django's manage script to execute specified task.

    Args:
        task (string): manage.py task.
    """
    with prefix("/bin/bash ./api-env/bin/activate"):
        local("python manage.py {}".format(task))


def clean():
    """Project directory cleanup."""
    local("rm -rf api-env")


def run():
    """Starts development server."""
    local_ip = "0.0.0.0:8000"
    _manage("runserver {}".format(local_ip))
