=======
Curator
=======

The ``djinn-curator`` is the component that handles cleaning up of old
artifacts that exceed a given limit. Every minute this will trigger and remove
the oldest artifacts that exceed the user's configured cleanup threshold.

.. contents::
   :local:
   :backlinks: none

External dependencies
=====================

Detailed below are the software dependencies that the curator needs in order
to start and run,

==========  ======
DEPENDENCY  REASON
==========  ======
PostgreSQL  Primary data store for the curator.
==========  ======

Configuration the curator
=========================

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
                                   stored. The ``<label>`` must be ``artifacts``.
``store.type``         ``string``  The type of store to use, must be ``file``.
``store.path``         ``string``  The location of the store.
=====================  ==========  ===========

Running the curator
===================

To run the curator, simply invoke the ``djinn-curator`` binary.

**Flags**

============  =======================  ===========
NAME          DEFAULT                  DESCRIPTION
============  =======================  ===========
``-config``   ``djinn-curator.conf``   The configuration file to use.
``-limit``    ``1073741824``           The limit in bytes to use for clearing up
(deprecated)                           artifacts. This has been deprecated and
                                       has no effect, since the user's
                                       configured limit is used instead.
============  =======================  ===========

Configuring the curator daemon
==============================

The ``dist`` directory contains files for running the Djinn Curator as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that used systemd, then be sure to run
``systemctl daemon-reload`` upon placement of the service file.
