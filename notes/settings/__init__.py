"""Settings initialization."""
import os

#
# NOTES_HOME variable will be set once the application
# is dockerized.
#
if os.getenv("NOTES_HOME", False):
    from notes.settings.prod import *
else:
    from notes.settings.dev import *
