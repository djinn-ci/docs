=========
Variables
=========

Entities
========

.. _variable-entity:

Variable entity
----------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the variable.
``author_id``      ``int``        ID of the :ref:`user <user-entity>` who created
                                  the variable.
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who owns
                                  the variable.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                   ``nullable``   the variable belongs to, if any.
``key``            ``string``     The name of the variable.
``value``          ``string``     The value of the variable, will be ``xxxxxx``
                                  if masked.
``masked``         ``bool``       Whether the variable has been masked.
``created_at``     ``timestamp``  The RRC3339 formatted string at which the variable
                                  was created.
``url``            ``string``     The API URL for the variable itself.
                                  the variable was placed on.
``author``         ``variable``   The :ref:`user <user-entity>` who authored the
                                  variable.
``user``           ``variable``   The :ref:`user <user-entity>` the variable belongs to.
``namespace``      ``variable``   The :ref:`namespace <namespace-entity>` the
                                  variable belongs to.
=================  =============  ===========

List variables
==============

.. code-block::

   GET /variables

List the :ref:`variables <variable-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``variable:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the variables with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/variables

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`variables <variable-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create variable
================

.. code-block::

   POST /variables

This will create an :ref:`variable <variable-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters need to be given as a JSON encoded
payload in the request body.This requires the ``variable:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``namespace``      ``string``     No        The namespace to upload the variable to.
``key``            ``string``     Yes       The name of the variable.
``value``          ``string``     Yes       The value of the variable.
``mask``           ``bool``       No        Whether the variable should be masked.
                                            Masked variable values must be at least
                                            6 characters in length.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"key": "PGADDR", "value": "host=localhost port=5432"}' \
       https://api.djinn-ci.com/variables

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`variable <variable-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get variable
============

.. code-block::

   GET /variables/:id

This will get the :ref:`variable <variable-entity>` by the given ``:id``. This requires
the ``variable:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/variables/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     If the ``Accept`` header matches the MIME type of
                               the variable, then the file itself will be sent in the
                               response body.

                               Otherwise, the :ref:`variable <variable-entity>`
                               will be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/variables/10/builds

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`builds <build-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Delete variable
===============

.. code-block::

   DELETE /variables/:id

This will delete the :ref:`variable <variable-entity>` by the given ``:id``. This
requires the ``variable:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/variables/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
