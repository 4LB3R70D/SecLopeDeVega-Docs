.. index:: Alerting

.. _activities:

Activity Alerting & Storage
===========================
In this chapter we are going to talk about the result of the interactions: activities. These activities

.. index:: Activities

Activities
----------


.. index:: Memory Reporting

Memory Reporting
----------------



.. index:: Storage

Storage
-------
*Lope* comes with a database schema ready to be imported into `MariaDB <https://mariadb.org/>`_ or `MySQL <https://www.mysql.com/>`_, ready to save any activity or any captured data for any interaction.
Below you can find the `Entity Relationship (ER) Diagram <https://www.visual-paradigm.com/guide/data-modeling/what-is-entity-relationship-diagram/>` that allow to save all the data. 
In this diagram, an ``external_connector_session`` is any session that the **external connector** establishes with the **engine**. The ``external_connection`` is any session (or interaction) that the
**external connector** establishes with a third party. As you will see, in any activity you can save the status of the memory variables in use as we have already explained.

.. image:: ../_static/slv_engine_db.png
   :width: 800
   :align: center



.. index:: Syslog Alerting

Syslog Alerting
---------------



.. index:: Kafka Alerting

Kafka Alerting
--------------



.. index:: Email Alerting

Email Alerting
--------------



.. index:: HTTP Alerting

HTTP Alerting
-------------