======
Server
======

The ``djinn-server`` is the primary component through which users would interact
with the CI server. This handles serving the UI and API endpoints for the
server. All assets served by the server are compiled into the binary itself, so
there is no need to worry about where assets will exist on disk.

External dependencies
=====================

Detailed below are the software dependencies that the server needs in order to
start and run,

===========  ======
DEPENDENCY   REASON
===========  ======
PostgreSQL   Primary data store for the consumer.
Redis        Data store used as the job queue to consume from.
SMTP Server  Used for sending emails.
===========  ======

Configuring the server
======================

**Parameters**

==========================  ============  ===========
NAME                        TYPE          DESCRIPTION
==========================  ============  ===========
``host``                    ``string``    The host on which the server will be running.
                                          This is used for OAuth redirects and setting
                                          the endpoint to which webhooks are sent.
``drivers``                 ``string[]``  The list of drivers supported on the
                                          server. This should match what is in the
                                          worker configuration.
``net``                     ``object``    Configuration details about how the server
                                          should be served over the network.
``net.listen``              ``string``    The address to listen on.
``net.write_timeout``       ``duration``  Maximum duration before timing out writes
                                          of a response, set to ``0s`` for no
                                          timeout.
``net.read_timeout``        ``duration``  Maximum duration before timing out reads of
                                          a request, set to ``0s`` for no timeout.
``net.tls.crt``                           Certificate file to use for TLS.
``net.tls.key``                           Key file to use for TLS.
``crypto``                  ``object``    Keys and hashes used for cryptography.
``crypto.hash``             ``string``    The hash key used to authenticate values
                                          using HMAC. Must be either 32 or 64
                                          characters in length.
``crypto.block``            ``string``    The block key used for encrypting data.
                                          Must be either, 16, 24, or 32 characters in
                                          length.
``crypto.salt``             ``string``    Salt used for generating random secrets.
``crypto.auth``             ``string``    The key used to protect against CSRF attacks.
                                          This must be 32 characters in length.
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
                                          * ``images``
                                          * ``objects``

                                          there must be a store configuration block
                                          for each.
``store.type``              ``string``    The type of the store to use, must be
                                          ``file``.
``store.path``              ``string``    The location where the files are.
``store.limit``             ``int``       The maximum size of files being stored.
                                          Set to ``0`` for no limit.
``provider <label>``        ``object``    Configuration parameters for each
                                          third-party provider you want to
                                          integrate with, where ``<label>`` is
                                          the name of that provider. As of now,
                                          only ``github``, and ``gitlab`` are
                                          supported.
``provider.secret``         ``string``    The secret used to authenticate incoming
                                          webhooks from the provider.
``provider.client_id``      ``string``    The OAuth client ID of the provider.
``provider.client_secret``  ``string``    The OAuth client secret of the provider.
==========================  ============  ===========

Environment variables
=====================

====================  ===========
NAME                  DESCRIPTION
====================  ===========
``DJINN_API_DOCS``    URL to the API documentation, link is rendered in the
                      sidebar if set.
``DJINN_API_SERVER``  URL to the API server, used to ensure all API endpoints
                      in response objects are complete.
``DJINN_USER_DOCS``   URL to the user documentation, link is rendered in the
                      sidebar if set.
====================  ===========

Running the server
==================

To run the consumer, simply invoke the ``djinn-server`` binary.

**Flags**

===========  ========================  ===========
NAME         DEFAULT                   DESCRIPTION
===========  ========================  ===========
``-config``  ``djinn-servers.conf``    The configuration file to use.
``-api``     ``--``                    Serve only the API endpoints.
``-ui``      ``--``                    Serve only the UI endpoints.
===========  ========================  ===========

If neither the ``-api``, or ``-ui`` flag are given, then both groups of
endpoints will be served. The REST API endpopints will be served under the
``/api`` prefix.

Proxying behind NGINX
=====================

NGINX can be used to serve the Djinn Server behind an NGINX proxy. This will
give you more fine grained control over any timeouts that may occur when
uploading/downloading build images. An example NGINX configuration can be found
in the ``dist`` directory.

Configuring the server daemon
=============================

The ``dist`` directory contains files for running the Djinn Server as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that used systemd, then be sure to run
``systemctl daemon-reload`` upon placement of the service file.
