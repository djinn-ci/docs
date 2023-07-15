====
Cron
====

Entities
========

.. _cron-entity:

Cron entity
-----------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID of the cron job.
``author_id``      ``int``        ID of the :ref:`user <user-entity>` who created
                                  the cron job.
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who owns
                                  the cron job.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                   ``nullable``   the cron belongs to, if any.
``name``           ``string``     The name of the cron job.
``schedule``       ``enum``       The schedule of the cron job, will be one of:

                                  - ``daily``
                                  - ``weekly``
                                  - ``monthly``
``manifest``       ``string``     The build :doc:`manifest </user/manifest>` to
                                  submit.
``prev_run``       ``timestamp``  When the cron job was last invoked, it at all.
                   ``nullable``
``next_run``       ``timestamp``  When the cron job will next be invoked.
``created_at``     ``timestamp``  The RFC3339 formatted string at which the
                                  cron job was created.
``url``            ``string``     The API URL to the cron job itself.
``author``         ``object``     The :ref:`user <user-entity>` who created the
                                  cron job.
``user``           ``object``     The :ref:`user <user-entity>` who owns the
                                  cron job.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  cron job belongs to.
=================  =============  ===========

List crons
==========

.. code-block::

   GET /cron

List the :ref:`cron jobs <cron-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``cron:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the cron jobs with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/cron

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`cron jobs <cron-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create cron
===========

.. code-block::

   POST /cron

This will create a :ref:`cron job <cron-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters need to be given as a JSON
encoded payload in the request body. This requires the ``cron:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``name``           ``string``     Yes       The name of the cron job.
``schedule``       ``enum``       No        The cron job's schedule, will be one
                                            of:

                                            - ``daily``
                                            - ``weekly``
                                            - ``monthly``

                                            this will default to ``daily``, if
                                            not otherwise specified.
``manifest``       ``string``     Yes       The :doc:`manifest </user/manifest>`
                                            to submit from the cron job.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"name": "Daily", "manifest": "driver:\n  image: centos/7\n  type: qemu"}' \
       https://api.djinn-ci.com/cron

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`cron job <cron-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get cron
========

.. code-block::

   GET /cron/:id

Get the :ref:`cron job <cron-entity>` by the given ``:id``. This requires the
``cron:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/cron/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`cron job <cron-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get cron builds
===============

.. code-block::

   GET /cron/:id/builds

This will get the :ref:`builds <build-entity>` submitted via the given
:ref:`cron job <cron-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``cron:read`` permission.

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

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/cron/10/builds

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

Update cron
===========

.. code-block::

   PATCH /cron/:id

This will update the :ref:`cron job <cron-entity>` by the given ``:id``. Th
following parameters need to be given as a JSON encoded payload in the request
body. This requires the ``cron:write`` permission.

.. note::

   If no parameters are sent in the request body, then nothing happens to the
   cron job.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``name``           ``string``     Yes       The name of the cron job.
``schedule``       ``enum``       No        The cron job's schedule, will be one
                                            of:

                                            - ``daily``
                                            - ``weekly``
                                            - ``monthly``

                                            this will default to ``daily``, if
                                            not otherwise specified.
``manifest``       ``string``     Yes       The :doc:`manifest </user/manifest>`
                                            to submit from the cron job.
=================  =============  ========  ===========

.. code-block::

   $ curl -X PATCH \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"name": "Daily", "manifest": "driver:\n  image: centos/7\n  type: qemu"}' \
       https://api.djinn-ci.com/cron/10

**Responses**

Delete cron
===========

.. code-block::

   DELETE /cron/:id

This will delete the :ref:`cron job <cron-entity>` by the given ``:id``. This
requires the ``cron:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/cron/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
