=======
Invites
=======

Entities
========

.. _invite-entity:

Invite entity
-------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the invite.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                                  the invite was sent for.
``invitee_id``     ``int``        ID of the :ref:`user <user-entity>` who received
                                  the invite.
``inviter_id``     ``int``        ID of the :ref:`user <user-entity>` who sent
                                  the invite.
``url``            ``string``     The API URL for the invite itself.
``invitee``        ``object``     The :ref:`user <user-entity>` who received the
                                  invite.
``inviter``        ``object``     The :ref:`user <user-entity>` who sent the
                                  invite.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  invite was for.
=================  =============  ===========

.. _accepted-invite-entity:

Accepted invite entity
----------------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``invitee``        ``object``     The :ref:`user <user-entity>` who received the
                                  invite.
``inviter``        ``object``     The :ref:`user <user-entity>` who sent the
                                  invite.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  invite was for.
=================  =============  ===========

List invites
============

.. code-block::

   GET /invites

List the :ref:`invite <invite-entity>` for the currently authenticated
:ref:`user <user-entity>`. This requires the ``invite:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/invites

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`invites <invite-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create invite
=============

.. code-block::

   POST /n/:username/:path/-/invites

This will create an :ref:`invite <invite-entity>` for the currently
authenticated :ref:`user <user-entity>`, for the :ref:`namespace <namespace-entity>`.
The following parameters need to be given as a JSON encoded payload in the request
body. This requires the ``invite:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``handle``         ``string``     Yes       The username or email fo the user to
                                            invite.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"handle": "you"}' \
       https://api.djinn-ci.com/n/me/djinn/-/invites
   
   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"handle": "you@example.com"}' \
       https://api.djinn-ci.com/n/me/djinn/-/invites

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`invite <invite-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Accept invite
=============

.. code-block::

   PATCH /invites/:id

This will accept the :ref:`invite <invite-entity>` of the given ``:id``. This
requires the ``invite:write`` permission.

.. code-block::

   $ curl -X PATCH -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/invites/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`invite <accepted-invite-entity>` will be
                               the response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Reject invite
=============

.. code-block::

   DELETE /invites/:id

This will reject the :ref:`invite <invite-entity>` of the given ``:id``. This
requires the ``invite:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/invites/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``             
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
