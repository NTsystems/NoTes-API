Administration
==============

Deployment
----------

The service is packed as a Docker_ container, and it is executed by starting
up an instance of a pre-built image. Container startup can be done in two
ways: manually, by executing a commands through the OS terminal window, or
via `Docker Compose`_, which is the preferred way. Please make sure to have
both tools installed on the target machine before proceeding with the
deployment.

Docker Compose
~~~~~~~~~~~~~~

Docker Compose is a tool for defining and running complex applications with
Docker. To spin the application using compose, you need to specify its
structure using YAML configuration file named ``docker-compose.yml``. The
following configuration template can be used for any type of deployment:

.. code-block:: yaml

    api:
      build: .
      ports:
        - "<local port>:80"
      links:
        - postgres:postgres
        - rabbit:rabbit

    postgres:
      image: postgres:9.3
      ports:
        - "<local postgres port>:5432"
      environment:
        - POSTGRES_USER=ntsystems
        - POSTGRES_PASSWORD=ntsystems

    rabbit:
      image: rabbitmq:3.5
      ports:
        - "<local rabbitmq port>:5672"

    celery:
      image: celery:3.1
      links:
        - rabbit:rabbit

Once the template is filled with concrete values, following command should be
executed in the OS terminal window:

.. code-block:: bash

    docker-compose up -d

To check whether the containers have been properly started up, the following
command should be issued:

.. code-block:: bash

    docker ps

If everything went well, result of this operation will contain list of four
instances with their respective names and identifiers. In case that startup
succeeded, an initial database migration has to be created by executing a
"one-shot" command in a following manner:

.. code-block:: bash

    docker-compose run api python manage.py migrate

Management
----------

As being said, each container is identified by its name and unique identifier.
These identifiers are useful for referencing the running container, i.e., to 
stop its execution. Each container can be stopped using the following command:

.. code-block:: bash

    docker stop <instance number>

It is quite enough to enter the first couple of characters of the instance
number. If that couple of characters uniquelly denote the instance, desired
action will be accepted. 

Beside individual container management, compose provides a way for managing
container "clusters". For example, to stop all containers started using the
configuration given above, one must issue:

.. code-block:: bash

    docker-compose stop

Once the container is stopped it can be either removed (again, both indivudual
and cluster removal are available), or started. Examples of these operations 
are given below:

.. code-block:: bash

    # individual startup
    docker start <instance number>

    # individual removal
    docker rm <instance number>

    # cluster start
    docker-compose start

    # cluster removal (this will fail if issued after start)
    docker-compose rm

Updating the Docker Containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to switch to a different version of NoTes API, the user should first
stop the currently running cluster. Afterward, a container cluster should be
rebuilt via:

.. code-block:: bash

    docker-compose build

Once rebuild is completed, cluster can be restarted.

.. _Docker: http://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/
