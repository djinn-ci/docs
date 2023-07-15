====
User
====

Entities
========

.. _user-entity:

User entity
-----------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``email``          ``string``     The email of the user.
``username``       ``string``     The username of the user.
``created_at``     ``timestamp``  The RFC3339 formatted string for when the user
                                  created their account.
=================  =============  ===========

Get user
========

.. code-block::

   GET /user

This will return the currently authenticated :ref:`user <user-entity>`.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/user

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`user <user-entity>` will be the response
                               body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
