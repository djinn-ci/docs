==========
Namespaces
==========

Entities
========

.. _namespace-entity:

Namespace entity
----------------

=====================  =============  ===========
NAME                   TYPE           DESCRIPTION
=====================  =============  ===========
``id``                 ``int``        Unique ID for the namespace.
``user_id``            ``int``        ID of the :ref:`user <user-entity>` who
                                      owns the namespace.
``root_id``            ``int``        ID of the top-level namespace for the current
                                      namespace. This will match the ``id`` for
                                      the root namespace.
``parent_id``          ``int``        ID of the namespace's parent, if any.
                       ``nullable``
``name``               ``string``     The name of the current namespace.
``path``               ``string``     The full path of the namespace, this will
                                      include the parent namespace names.
``description``        ``string``     The description of the current namespace.
``visibility``         ``enum``       The :ref:`visibility <visibility>`
                                      level of the namespace, will be one of:

                                      - ``private``
                                      - ``internal``
                                      - ``public``
``created_at``         ``timestamp``  The RFC3339 formatted string at which the
                                      namespace was created.
``url``                ``string``     The API URL to the namespace itself.
``builds_url``         ``string``     The API URL to the namespace's builds.
``namespaces_url``     ``string``     The API URL to the namespace's namespaces.
``images_url``         ``string``     The API URL to the namespace's images.
``objects_url``        ``string``     The API URL to the namespace's objects.
``variables_url``      ``string``     The API URL to the namespace's variables.
``keys_url``           ``string``     The API URL to the namespace's keys.
``collaborators_url``  ``string``     The API URL to the namespace's collaborators.
``webhooks_url``       ``string``     The API URL to the namespace's webhooks.
``user``               ``object``     The :ref:`user <user-entity>` that owns
                                      the namespace.
``parent``             ``object``     The parent namespace, if any.
                       ``nullable``
``build``              ``object``     The last :ref:`build <build-entity>` submitted
                       ``nullable``   to the namespace, if any.
=====================  =============  ===========

.. _webhook-entity:

Webhook entity
--------------

============================  =============  ===========
NAME                          TYPE           DESCRIPTION
============================  =============  ===========
``id``                        ``int``        Unique ID for the namespace.
``author_id``                 ``int``        ID of the :ref:`user <user-entity>` who
                                             authored the webhook.
``user_id``                   ``int``        ID of the :ref:`user <user-entity>` who
                                             owns the webhook.
``namespace_id``              ``int``        ID of the :ref:`namespace <namespace-entity>`
                                             the webhook belongs to.
``payload_url``               ``string``     URL to send the event payload to.
``ssl``                       ``bool``       Whether or not the event will be sent over
                                             TLS.
``events``                    ``string[]``   The :ref:`events <event-payloads>` the
                                             webhook will activate on.
``namespace``                 ``object``     The :ref:`namespace <namespace-entity>` the
                                             webhook belongs to.
``last_response``             ``object``     The last response received from the
                              ``nullable``   webhook, if any.
``last_response.code``        ``int``        The HTTP status codde of the response.
``last_response.duration``    ``int``        The duration of the webhook request
                                             in nanoseconds.
``last_response.error``       ``string``     The error that occurred if the webhook
                              ``nullable``   failed to be delivered.
``last_response.created_at``  ``timestamp``  The RFC3339 formatted string at
                                             which the delivery was made.
============================  =============  ===========

.. _collaborator-entity:

Collaborator entity
-------------------

=====================  =============  ===========
NAME                   TYPE           DESCRIPTION
=====================  =============  ===========
``id``                 ``int``        Unique ID for the user.
``email``              ``string``     The email of the user.
``username``           ``string``     The username of the user.
``created_at``         ``timestamp``  The RFC3339 formatted string for when the
                                      user joined the namespace.
``url``                ``string``     The API URL to the collaborator itself.
=====================  =============  ===========

List namespaces
===============

.. code-block::

   GET /namespaces

List the :ref:`namespaces <namespace-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``namespace:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the namespaces with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/namespaces

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`namespaces <namespace-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create namespace
================

.. code-block::

   POST /namespaces

This will create a :ref:`namespace <namespace-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters need to be given as a JSON
encoded payload in the request body. This requires the ``namespace:write``
permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``parent``         ``string``     No        The name of the parent namespace to
                                            create the new namespace under.
``name``           ``string``     Yes       The name of the new namespace.
``description``    ``string``     No        The description of the namespace.
``visibility``     ``enum``       No        The :ref:`visiblity <visibility>` of
                                            the namespace, will be one of:

                                            - ``private``
                                            - ``internal``
                                            - ``public``

                                            This defaults to ``private``.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"name": "djinn", "visibility": "private"}'\
       https://api.djinn-ci.com/namespaces

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``201 Created``                The :ref:`namespace <namespace-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace
=============

.. code-block::

   GET /n/:username/:path

This will get the :ref:`namespace <namespace-entity>` by the given ``:username``,
with the given ``:path``. This requires the ``namespace:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`namespace <namespace-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace badge
===================

.. code-block::

   GET /n/:username/:path/-/badge.svg

This will return the SVG badge of the :ref:`namespace <namespace-entity>` by
the given ``:username``, with the given ``:path``. This SVG will show the status
of the most recently submitted build to the namespace. This requires no
permission for the user.

**Badges**

.. raw:: html
   :file: ../../badge-table.html

Get namespace builds
====================

.. code-block::

   GET /n/:username/:path/-/builds

List the :ref:`builds <build-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. The following parameters
can be given as query parameters to the URL. This requires the ``namespace:read``
permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``tag``            ``string``     No        Get the builds with the given tag.
``search``         ``string``     No        Get the builds with tags like the
                                            given value.
``status``         ``enum``       No        Get the builds with the given status,
                                            will be one of:

                                            - ``queued``
                                            - ``running``
                                            - ``passed``
                                            - ``passed_with_failures``
                                            - ``failed``
                                            - ``killed``
                                            - ``timed_out``
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/builds

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

Get namespace children
======================

.. code-block::

   GET /n/:username/:path/-/namespaces

List the child :ref:`namespaces <namespace-entity>` for the namespace by the
given ``:username``, with the given ``:path``. This requires the ``namespace:read``
permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/namespaces

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`namespaces <namespace-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace images
====================

.. code-block::

   GET /n/:username/:path/-/images

List the :ref:`images <image-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. The following parameters
can be given as query parameters to the URL. This requires the ``namespace:read``
permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the images with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/images

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`images <image-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace objects
=====================

.. code-block::

   GET /n/:username/:path/-/objects

List the :ref:`objects <object-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. The following parameters
can be given as query parameters to the URL. This requires the ``namespace:read``
permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the objects with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/objects

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`objects <object-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace variables
=======================

.. code-block::

   GET /n/:username/:path/-/variables

List the :ref:`variables <variable-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. The following parameters
can be given as query parameters to the URL. This requires the ``namespace:read``
permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the variables with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/variables

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

Get namespace keys
==================

.. code-block::

   GET /n/:username/:path/-/keys

List the :ref:`keys <key-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. The following parameters
can be given as query parameters to the URL. This requires the ``namespace:read``
permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the keys with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/keys

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

Get namespace invites
=====================

.. code-block::

   GET /n/:username/:path/-/invites

List the :ref:`invites <invite-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. This requires the
``namespace:read`` permission for the user.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/invites

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`invites <invite-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace collaborators
===========================

.. code-block::

   GET /n/:username/:path/-/collaborators

List the :ref:`invites <invite-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. This requires the
``namespace:read`` permission for the user.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/collaborators

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`collaborators <collaborator-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get namespace webhooks
======================

.. code-block::

   GET /n/:username/:path/-/webhooks

List the :ref:`webhooks <invite-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. This requires the
``webhook:read`` permission for the user.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/n/djinn-ci/djinn/-/webhooks

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`webhooks <webhook-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create namespace webhook
========================

.. code-block::

   POST /n/:username/:path/-/webhooks

This will create a :ref:`webhook <webhook-entity>` for the :ref:`namespace <namespace-entity>`
by the given ``:username``, with the given ``:path``. The following parameters
need to be given as a JSON encoded payload in the request body. This requires
the ``webhook:write`` permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``payload_url``    ``string``     Yes       The URL to send the event payload to.
``secret``         ``string``     No        The secret to sign the event payload
                                            with.
``ssl``            ``bool``       No        Whether or not to use TLS when sending
                                            the event. The ``https`` scheme needs
                                            to be specified when this option is
                                            enabled.
``active``         ``bool``       No        Whether or not the webhook should be
                                            active.
``events``         ``string[]``   No        The list of :ref:`events <event-payloads>`
                                            to activate onn. If no events are given,
                                            then the webhook will activate on all
                                            events.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"payload_url": "https://example.com/hook/djinn-ci", "ssl": true, "active": true}' \
       https://api.djinn-ci.com/n/djinn-ci/djinn/-/webhooks

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``201 Created``                The :ref:`webhook <webhook-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Update namespace webhook
========================

.. code-block::

   PATCH /n/:username/:path/-/webhooks/:id

This will update the :ref:`webhook <webhook-entity>` by the given ``:id``, for
the :ref:`namespace <namespace-entity>` by the given ``:username``, with the
given ``:path``. The following parameters need to be given as a JSON encoded
payload in the request body. This requires the ``webhook:write`` permission for
the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``payload_url``    ``string``     Yes       The URL to send the event payload to.
``secret``         ``string``     No        The secret to sign the event payload
                                            with.
``ssl``            ``bool``       No        Whether or not to use TLS when sending
                                            the event. The ``https`` scheme needs
                                            to be specified when this option is
                                            enabled.
``active``         ``bool``       No        Whether or not the webhook should be
                                            active.
``events``         ``string[]``   No        The list of :ref:`events <event-payloads>`
                                            to activate onn. If no events are given,
                                            then the webhook will activate on all
                                            events.
=================  =============  ========  ===========

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`webhook <webhook-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"secret": "some_secret_password"}' \
       https://api.djinn-ci.com/n/djinn-ci/djinn/-/webhooks/1

Delete namespace webhook
========================

.. code-block::

   DELETE /n/:username/:path/-/webhooks/:id

This will delete the :ref:`webhook <webhook-entity>` by the given ``:id``, for
the :ref:`namespace <namespace-entity>` by the given ``:username``, with the
given ``:path``. This requires the ``webhook:delete`` permission for the user.

.. code-block::

   $ curl -X DELETE \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       https://api.djinn-ci.com/n/djinn-ci/djinn/-/webhooks/1

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Update namespace
================

.. code-block::

   PATCH /n/:username/:path

This will update the :ref:`namespace <namespace-entity>` by the given
``:username``, with the given ``:path``. The following parameters need to be
given as a JSON encoded payload in the request body. This requires the
``namespace:write`` permission for the user.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``description``    ``string``     No        The description of the namespace.
``visibility``     ``enum``       No        The :ref:`visiblity <visibility>` of
                                            the namespace, will be one of:

                                            - ``private``
                                            - ``internal``
                                            - ``public``

                                            This defaults to ``private``.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"name": "djinn", "visibility": "public"}'\
       https://api.djinn-ci.com/n/djinn-ci/djinn

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`namespace <namespace-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Delete namespace
================

.. code-block::

   DELETE /n/:username/:path

This will delete the given :ref:`namespace <namespace-entity>` by the given
``:username``, with the given ``:path``. This requires the ``namespace:delete``
permission.

.. code-block::

   $ curl -X DELETE \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       https://api.djinn-ci.com/n/djinn-ci/djinn

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
