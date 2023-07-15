=====
OAuth
=====

.. _authorizing-an-oauth-app:

Authorizing an OAuth app
========================

When authorizing an OAuth app, a ``GET`` request must be sent to the
``/login/oauth/authorize`` endpoint, with the following parameters.

.. code-block::

   GET https://djinn-ci.com/login/oauth/authorize

================  ===========
NAME              DESCRIPTION
================  ===========
``client_id``     The client ID you received from Djinn CI when you created a
                  new app.
``redirect_uri``  The URL in your app where users will be sent once
                  authenticated.
``scope``         A space delimited list of :ref:`scopes <token-scopes>`.
``state``         An optional random string used to protect from CSRF attacks.
================  ===========

Once the user has allowed your app access to their Djinn CI account, they will
be redirected to the ``redirect_uri`` of your app. A temporary ``code`` will
be passed in the ``redirect_uri``, this will expire in 10 minutes. If a
``state`` was given during authentication, then this will be sent back too, and
should be checked on your end. If this state code does not match then you should
abort immediately.

Extract the ``code`` from the ``redirect_uri`` and exchange it, with the
following parameters,

.. code-block::

   POST https://djinn-ci.com/login/oauth/token

=================  ===========
NAME               DESCRIPTION
=================  ===========
``client_id``      The client ID you received from Djinn CI when you created a
                   new app.
``client_secret``  The client secret you received from Djinn CI when you created
                   a new app.
``code``           The code you received during the redirect back to your app.
=================  ===========

The parameters sent back to the endpoint should be encoded as a URL string. By
default, the response will be URL encoded like so,

.. code-block::

   access_token=1a2b3c&token_type=bearer&scope=build:read,write

a JSON respnse can be received by setting the ``Accept`` header to
``application/json``,

.. code-block::

   {
       "access_token": "1a2b3c",
       "token_type": "bearer",
       "scope": "build:read,write"
   }

.. _token-scopes:

Token scopes
============

A scope dictates the sort of access you need to the API. A single scope is made
up of a resource, and the permissions for that resource. There are three
permissions that a resoure can have,

==========  ===========
PERMISSION  DESCRIPTION
==========  ===========
``read``    Allow a user to get a resource.
``write``   Allow a user to create or update a resource.
``delete``  Allow a user to delete a resource.
==========  ===========

each individual scope is represented as ``<resource>:<permission>,...```, for
example,

.. code-block::

   build:read,write,delete namespace:read,write

The above scope would grant the user the ability to view, create, and kill
builds, and view, create, and update namespaces.
