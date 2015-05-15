"""Contains repetitive task definitions."""
from fabric.api import *


def _manage(task):
    """Invokes manage.py.

    Function uses django's manage script to execute specified task.

    Args:
        task (string): name of a task to execute.
    """
    local("python manage.py {}".format(task))


def clean():
    """Project directory cleanup."""
    local("rm -rf env")


def create_admin():
    """Creates admin account."""
    _manage("createsuperuser")


def migrate():
    """Performs database migrations."""
    _manage("makemigrations")
    _manage("migrate")


def docs():
    """Generates sphinx documentation."""
    local("sphinx-build -b html docs/ docs/_build/")


def test(app=None):
    """Runs unit tests.

    Args:
        app (string): App to run tests for.
    """
    if app:
        _manage("test {}".format(app))
    else:
        _manage("test")


def run():
    """Starts development server."""
    local_ip = "0.0.0.0:8000"
    _manage("runserver {}".format(local_ip))
