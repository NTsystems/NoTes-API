"""Settings initialization."""
import os

#
# PRODUCTION variable will be set once the application
# is dockerized.
#
if os.getenv("PRODUCTION", False):
    from notes.settings.prod import *
else:
    from notes.settings.dev import *
