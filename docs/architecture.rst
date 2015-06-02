Architecture
============

REST API
++++++++

Benefits of using REST API:

- Use HTTP methods explicitly and lets us interact with Parse from anything that can send an Http request.
- In the REST API, the class-level operations operate on a resource based on just the class name.
- Client server - A uniform interface separates clients from servers. This means that, for example,clients are not concerned with data storage, which remains internal to each server,so that the portability of client code is improved. Servers are not concerned with the user interface or user state,so that servers can be simpler and more scalable.
- Stateless - the client–server communication is further constrained by no client context being stored on the server between requests. Each request from any client contains all the information necessary to service the request, and session state is held in the client.

REST components communicate by transferring a representation of a resource in a format matching one of an
evolving set of standard data types, selected dynamically based on the capabilities or desires of the recipient
and the nature of the resource. Whether the representation is in the same format as the raw source,
or is derived from the source, remains hidden behind the interface. REST therefore gains the separation of concerns
of the client-server style without the server scalability problem, allows information hiding through
a generic interface to enable encapsulation and evolution of services, and provides for a diverse
set of functionality through downloadable feature-engines.

System overview
+++++++++++++++

Initial project architecture look like this:

.. image:: ./_static/arch.jpg
   :align: center

Based on this we design our data model

.. image:: ./_static/model.jpg
   :align: center

- Every person can visit site and there are 3 types of users:
    - guest
    - user
    - administrator

- Guest can:
    - register(after registration he get authorization token)
    - login

- User can:
    - logout
    - change its profile data(only password ATM)
    - manage his own notes

Every user has one user profile which contains his personal data. He can have many notebooks and every notebook can
have many notes. Because of authorization every user have access only to his own notebooks and notes.

- Admin:
    - apply CRUD(create, read, update, delete) everywhere

For implementation we used Django REST framework and PostgreSQL database.

.. _REST: http://www.django-rest-framework.org/