Architecture
============
TBD

Description
-----------

- Technology stack:
    - Git
      Git really changed the way developers think of merging and branching. From the classic CVS/Subversion world,
      merging/branching has always been considered a bit scary and something you only do every once in a while.
      With Git, these actions are extremely cheap and simple, and they are considered one of the core parts of
      your daily workflow.

    - In our project we use git flow model branching

- Despite being simple, REST is fully-featured, there's basically nothing you can do in Web
  Services that can't be done with a RESTful architecture

Diagram
-------

Design of data model
++++++++++++++++++++

.. image:: ./_static/model.jpg
   :align: center


System overview
+++++++++++++++

.. image:: ./_static/arch.jpg
   :align: center


- *Server*
    - Exposes REST API
    - Exposes admin interface
    - Docker component
- *Client*
    - REST API consumer
    - Hosted at nginx
    - Docker component



