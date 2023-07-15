========
Consumer
========

The ``djinn-consumer`` is the component that handles the processing of
background jobs, such as remote image downloads. This will pull jobs from Redis
off the ``jobs`` queue for processing.

.. contents::
   :local:
   :backlinks: none

External dependencies
=====================

Detailed below are the software dependencies that the consumer needs in order
to start and run,

==========  ======
DEPENDENCY  REASON
==========  ======
PostgreSQL  Primary data store for the consumer.
Redis       Data store used as the job queue to consume from.
==========  ======

Configuration the consumer
==========================

**Parameters**

=====================  ==========  ===========
NAME                   TYPE        DESCRIPTION
=====================  ==========  ===========
``database``           ``object``  Provides connection information to the
                                   PostgreSQL database.
``database.addr``      ``string``  The address of the PostgreSQL server to
                                   connect to.
``database.name``      ``string``  The name of the database to use.
``database.username``  ``string``  The name of the database user.
``database.password``  ``string``  The password of the database user.
``database.tls``       ``object``  TLS configuration for connecting via TLS.
``database.tls.ca``    ``string``  Path to the CA root to use.
``database.tls.cert``  ``string``  Path to the certificate to use.
``database.tls.key``   ``string``  Path to the key to use.
``redis``              ``object``  Provides connection information to the Redis
                                   database.
``redis.addr``         ``string``  The address of the Redis server to connect
                                   to.
``redis.password``     ``string``  The password used, if the Redis server is
                                   password protected.
``store <label>``      ``object``  The location where the driver images are
                                   stored. The ``<label>`` must be ``images``.
``store.type``         ``string``  The type of store to use, must be ``file``.
``store.path``         ``string``  The location of the store.
=====================  ==========  ===========

Running the consumer
====================

To run the consumer, simply invoke the ``djinn-consumer`` binary.

**Flags**

===========  =======================  ===========
NAME         DEFAULT                  DESCRIPTION
===========  =======================  ===========
``-config``  ``djinn-consumer.conf``  The configuration file to use.
===========  =======================  ===========

Configuring the consumer daemon
===============================

The ``dist`` directory contains files for running the Djinn Consumer as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that used systemd, then be sure to run
``systemctl daemon-reload`` upon placement of the service file.
