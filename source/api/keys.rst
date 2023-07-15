====
Keys
====

Entities
========

.. _key-entity:

Key entity
----------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID of the key.
``author_id``      ``int``        ID of the :ref:`user <user-entity>` who created
                                  the key.
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who owns
                                  the key.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                   ``nullable``   the cron belongs to, if any.
``name``           ``string``     The name of the key.
``config``         ``string``     The key's configuration.
``created_at``     ``timestamp``  The RFC3339 formatted string at which they key
                                  was created.
``updated_at``     ``timestamp``  The RFC3339 formatted string at which they key
                                  was updated.
``url``            ``string``     The API URL to the key itself.
``author``         ``object``     The :ref:`user <user-entity>` who authored the key.
``user``           ``object``     The :ref:`user <user-entity>` who owns the key.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the key
                                  belongs to.
=================  =============  ===========

List keys
=========

.. code-block::

   GET /keys

List the :ref:`keys <key-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``key:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the keys with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/keys

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`keys <key-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create key
==========

.. code-block::

   POST /keys

This will create a :ref:`key <key-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters need to be given as a JSON
encoded payload in the request body. This requires the ``key:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``namespace``      ``string``     No        The namespace to store the key in.
``name``           ``string``     Yes       The name of the key.
``key``            ``string``     Yes       The private key.
``config``         ``string``     No        The SSH configuration for the key.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"name": "id_rsa", "key": "-----BEGIN..."}' \
       https://api.djinn-ci.com/keys

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`key <key-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get key
=======

.. code-block::

   GET /key/:id

This will get the :ref:`key <key-entity>` by the given ``:id``. This requires
the ``key:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/keys/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`key <key-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Update key
==========

.. code-block::

   PATCH /keys/:id

This will update the given :ref:`key <key-entity>` by the given ``:id``. This
requires the ``key:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``namespace``      ``string``     No        The namespace to store the key in.
``name``           ``string``     Yes       The name of the key.
``config``         ``string``     No        The SSH configuration for the key.
=================  =============  ========  ===========

.. code-block::

   $ curl -X PATCH \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"config": "UserKnownHostsFile /dev/null"}' \
       https://api.djinn-ci.com/keys/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`key <key-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Delete key
==========

.. code-block::

   DELETE /keys/:id

This will delete the :ref:`key <key-entity>` by the given ``:id``. This requires
the ``key:delete`` permission.

.. code-block::

   $ curl -X DELETE \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       https://api.djinn-ci.com/keys/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
