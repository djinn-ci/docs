=========
Scheduler
=========

The ``djinn-scheduler`` is the component that handles the scheduling of cron
jobs that have been created via the server. Every minute this will invoke the
cron jobs in batches of 1000 that are ready to be invoked.

.. contents::
   :local:
   :backlinks: none


External dependencies
=====================

Detailed below are the software dependencies that the scheduler needs in order
to start and run,

==========  ======
DEPENDENCY  REASON
==========  ======
PostgreSQL  Primary data store for the consumer.
Redis       Data store used as the job queue to consume from.
==========  ======

Configuring the scheduler
=========================

**Parameters**

=====================  ============  ===========
NAME                   TYPE          DESCRIPTION
=====================  ============  ===========
``drivers``            ``string[]``  List of drivers supported on the server.
                                     Must match what is in the server
                                     configuration.
``crypto``             ``object``    Configuration settings for generating names
                                     for artifacts.
``crypto.salt``        ``string``    Salt used to generate secrest. Must match
                                     what is in the server configuration.
``database``           ``object``    Provides connection information to the
                                     PostgreSQL database.
``database.addr``      ``string``    The address of the PostgreSQL server to
                                     connect to.
``database.name``      ``string``    The name of the database to use.
``database.username``  ``string``    The name of the database user.
``database.password``  ``string``    The password of the database user.
``database.tls``       ``object``    TLS configuration for connecting via TLS.
``database.tls.ca``    ``string``    Path to the CA root to use.
``database.tls.cert``  ``string``    Path to the certificate to use.
``database.tls.key``   ``string``    Path to the key to use.
``redis``              ``object``    Provides connection information to the Redis
                                     database.
``redis.addr``         ``string``    The address of the Redis server to connect
                                     to.
``redis.password``     ``string``    The password used, if the Redis server is
                                     password protected.
=====================  ============  ===========

Running the scheduler
=====================

To run the consumer, simply invoke the ``djinn-scheduler`` binary.

**Flags**

===========  ========================  ===========
NAME         DEFAULT                   DESCRIPTION
===========  ========================  ===========
``-config``  ``djinn-scheduler.conf``  The configuration file to use.
===========  ========================  ===========

Configuring the scheduler daemon
================================

The ``dist`` directory contains files for running the Djinn Scheduler as a
daemon on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that used systemd, then be sure to run
``systemctl daemon-reload`` upon placement of the service file.
