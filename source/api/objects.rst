=======
Objects
=======

Entities
========

.. _object-entity:

Object entity
-------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the object.
``author_id``      ``int``        ID of the :ref:`user <user-entity>` who created
                                  the object.
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who owns
                                  the object.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                   ``nullable``   the object belongs to, if any.
``name``           ``string``     The name of the object.
``type``           ``string``     The MIME type of the object.
``size``           ``int``        The size of the object in bytes.
``md5``            ``string``     The MD5 sum hash of the object.
``sha256``         ``string``     The SHA256 sum hash of the object.
``created_at``     ``timestamp``  The RRC3339 formatted string at which the object
                                  was created.
``url``            ``string``     The API URL for the object itself.
``builds_url``     ``string``     The API URL to the :ref:`builds <build-entity>`
                                  the object was placed on.
``author``         ``object``     The :ref:`user <user-entity>` who authored the
                                  object.
``user``           ``object``     The :ref:`user <user-entity>` the object belongs to.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  object belongs to.
=================  =============  ===========

List objects
=============

.. code-block::

   GET /objects

List the :ref:`objects <object-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``object:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the objects with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/objects

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

Create object
=============

.. code-block::

   POST /objects

This will create an :ref:`object <object-entity>` for the currently authenticated
:ref:`user <user-entity>`. This requires the ``object:write`` permission.

The contents of the file should be sent in the body of the request. The header
``Content-Type`` should be the MIME type of the file being uploaded. The parameters
should be sent in the URL as query parameters.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``name``           ``string``     Yes       The name of the object.
``namespace``      ``string``     No        The namespace to upload the object to.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: image/jpeg" \
       -d "@picture.jpeg" \
       https://api.djinn-ci.com/objects?name=data&namespace=djinn

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`object <object-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get object
==========

.. code-block::

   GET /objects/:id

This will get the :ref:`object <object-entity>` by the given ``:id``. This requires
the ``object:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/objects/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     If the ``Accept`` header matches the MIME type of
                               the object, then the file itself will be sent in the
                               response body.

                               Otherwise, the :ref:`object <object-entity>`
                               will be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get object builds
=================

.. code-block::

   GET /objects/:id/builds

This will get the :ref:`builds <build-entity>` the object was placed on. The
following parameters can be given as query parameters to the URL. This requires
the ``object:read`` permission.

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

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/objects/10/builds

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

Delete object
=============

.. code-block::

   DELETE /objects/:id

This will delete the :ref:`object <object-entity>` by the given ``:id``. This
requires the ``object:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/objects/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``             
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
