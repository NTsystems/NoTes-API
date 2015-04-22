"""Contains repetitive task definitions."""
import contextlib

from fabric.api import *


@contextlib.contextmanager
def _virtualenv():
    """Activates virtualenv."""
    activator = "./env/bin/activate_this.py"
    execfile(activator, dict(__file__=activator))
    yield


def _manage(task):
    """Invokes manage.py.

    Function uses django's manage script to execute specified task.

    Args:
        task (string): name of a task to execute.
    """
    with _virtualenv():
        local("python manage.py {}".format(task))


def clean():
    """Project directory cleanup."""
    local("rm -rf env")


def make_env():
    """Makes development environment."""
    local("virtualenv -p /usr/bin/python --no-site-packages env")
    with _virtualenv():
        local("pip install -r ./requirements/dev.txt")


def create_admin():
    """Creates admin account."""
    _manage("createsuperuser")


def migrate():
    """Performs database migrations."""
    _manage("makemigrations")
    _manage("migrate")


def run():
    """Starts development server."""
    local_ip = "0.0.0.0:8000"
    _manage("runserver {}".format(local_ip))
