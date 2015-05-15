Development
===========

Environment
-----------

To ensure that all team members work on the same environment, Vagrant_ virtual
machine configuration has been provided. Developers must ensure that
Virtualbox_ and Vagrant are installed and configured at their development
machines.

The following code block shows most used vagrant commands, with their meaning.
Users are encouraged to read the official documentation for more information.

.. code-block:: bash

    # create/start VM instance
    vagrant up

    # stop the VM
    vagrant halt

    # SSH into the VM
    vagrant ssh

    # completely remove VM
    vagrant destroy

Repetitive task automation (i.e. running migrations, tests, etc.) are handled
by Fabric_. Fabric is a command-line that provides a basic set of operations
for executing local and remote shell commands, as well as the uploads and
downloads of files, and user interaction. Next section discusses the content of
the available fabric script.

Fabric API
~~~~~~~~~~

.. code-block:: bash

    # invokes manage.py
    fab _manage

    # project directory cleanup
    fab clean

    # creates admin account
    fab create_admin

    # performs database migrations
    fab migrate

    # generates sphinx documentation
    fab docs

    # runs unit test
    fab test

    # starts development server
    fab run


Swagger
-------

Swagger_ provides a useful representation of exposed REST API. It can be
accessed on the following address_.

.. _Fabric: http://www.fabfile.org/
.. _Virtualbox: https://www.virtualbox.org/
.. _Vagrant: https://www.vagrantup.com/
.. _Swagger: http://swagger.io/
.. _address: http://192.168.85.5:8000/swagger/
