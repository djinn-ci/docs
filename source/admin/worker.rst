======
Worker
======

The ``djinn-worker`` is the component that handles executing builds that are
submitted via the :doc:`server </admin/server>` or the
:doc:`scheduler </admin/scheduler>`. You may need to install some additional
dependencies on the worker machine depending on the drivers you want to make
available.

External dependencies
=====================

Detailed below are the software dependencies that the worker needs in order to
start and run,

===========  ======
DEPENDENCY   REASON
===========  ======
PostgreSQL   Primary data store for the consumer.
Redis        Data store used as the job queue to consume from.
SMTP Server  Used for sending emails.
===========  ======

Driver dependencies
===================

Detailed below are the software dependencies that the worker needs in order to
execute a build via that driver.

==========  ========
DRIVER      SOFTWARE
==========  ========
``docker``  The ``dockerd`` process for managing containers.
``qemu``    The ``qemu`` software package for creating virtual machines.
==========  ========

Configuring the worker
======================

==========================  ============  ===========
NAME                        TYPE          DESCRIPTION
==========================  ============  ===========
``parallelism``             ``int``       The parallelism to use when running
                                          multiple builds at once. Set to ``0``
                                          to use the number of CPU cores
                                          available.
``driver``                  ``string``    The driver that will be used for
                                          executing builds on the worker.
``crypto``                  ``object``    Keys and hashes used for cryptography.
``crypto.block``            ``string``    The block key used for encrypting data.
                                          Must be either, 16, 24, or 32 characters in
                                          length.
``crypto.salt``             ``string``    Salt used for generating random secrets.
``database``                ``object``    Provides connection information to the
                                          PostgreSQL database.
``database.addr``           ``string``    The address of the PostgreSQL server to
                                          connect to.
``database.name``           ``string``    The name of the database to use.
``database.username``       ``string``    The name of the database user.
``database.password``       ``string``    The password of the database user.
``database.tls``            ``object``    TLS configuration for connecting via TLS.
``database.tls.ca``         ``string``    Path to the CA root to use.
``database.tls.cert``       ``string``    Path to the certificate to use.
``database.tls.key``        ``string``    Path to the key to use.
``redis``                   ``object``    Provides connection information to the Redis
                                          database.
``redis.addr``              ``string``    The address of the Redis server to connect
                                          to.
``redis.password``          ``string``    The password used, if the Redis server is
                                          password protected.
``smtp``                    ``object``    Configuration details for the SMTP server
                                          to use for sending email.
``smtp.addr``               ``string``    The address of the SMTP server.
``smtp.ca``                 ``string``    The path to the root CA, if connecting via
                                          TLS.
``smtp.admin``              ``string``    The email address to be used in the ``From``
                                          field of emails that are sent.
``smtp.username``           ``string``    The username for authentication.
``smtp.password``           ``string``    The password for authentication.
``store <label>``           ``object``    Configuration parameters for each of
                                          the file stores the server uses. The
                                          ``<label>`` will be the store type, one
                                          of:

                                          * ``artifacts``
                                          * ``objects``

                                          there must be a store configuration block
                                          for each.
``store.type``              ``string``    The type of the store to use, must be
                                          ``file``.
``store.path``              ``string``    The location where the files are.
``store.limit``             ``int``       The maximum size of files being stored.
                                          Set to ``0`` for no limit. For artifacts
                                          this will only collect the first n bytes
                                          of a file.
``provider <label>``        ``object``    Configuration parameters for each third-party
                                          provider you want to integrate with, where
                                          the ``label`` is the name of the provider. As
                                          of now, only ``github``, and ``gitlab`` are
                                          supported. For the worker, the ``client_id``
                                          and ``client_secret`` do not need specifying.
==========================  ============  ===========

Running the worker
==================

To run the consumer, simply invoke the ``djinn-worker`` binary.

**Flags**

===========  ========================  ===========
NAME         DEFAULT                   DESCRIPTION
===========  ========================  ===========
``-config``  ``djinn-worker.conf``     The configuration file to use.
``-driver``  ``djinn-driver.conf``     The driver configuration file to use.
===========  ========================  ===========

Configuring the worker daemon
=============================

The ``dist`` directory contains files for running the Djinn Worker as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that used systemd, then be sure to run
``systemctl daemon-reload`` upon placement of the service file.
