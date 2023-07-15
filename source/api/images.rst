======
Images
======

Entities
========

.. _image-entity:

Image entity
------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the image.
``author_id``      ``int``        ID of the :ref:`user <user-entity>` who created
                                  the image.
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who owns
                                  the image.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                   ``nullable``   the image belongs to, if any.
``name``           ``string``     The name of the image.
``created_at``     ``timestamp``  The RRC3339 formatted string at which the image
                                  was created.
``url``            ``string``     The API URL for the image itself.
``author``         ``object``     The :ref:`user <user-entity>` who authored the
                                  image.
``user``           ``object``     The :ref:`user <user-entity>` the image belongs to.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  image belongs to.
=================  =============  ===========

List images
===========

.. code-block::

   GET /images

List the :ref:`images <image-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``image:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the images with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/images

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

Create image
============

.. code-block::

   POST /images

This will create an :ref:`image <image-entity>` for the currently authenticated
:ref:`user <user-entity>`. This requires the ``image:write`` permission.

Images can be created either via a direct upload, whereby the contents of the
image is sent in the request body, and the parameters are sent as URL query
parameters.

An image download can also be created by submitting the JSON encoded parameters
alongside the ``download_url`` parameter.

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``name``           ``string``     Yes       The name of the image.
``namespace``      ``string``     No        The namespace to upload the image to.
``download_url``   ``string``     Yes*      The URL to download the image from.
                                            Only required if the image is being
                                            downloaded.
=================  =============  ========  ===========

.. code-block::

   # Direct image upload
   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -d "@alpine.qcow2" \
       https://api.djinn-ci.com/images?name=alpine

   # Image download
   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"name": "alpine", "namespace": "djinn", "download_url": "https://example.com/alpine"}' \
       https://api.djinn-ci.com/images

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`image <image-entity>` will be the
                               response body, with a ``Link`` header set for
                               pagination.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get image
=========

.. code-block::

   GET /images/:id

This will get the :ref:`image <image-entity>` by the given ``:id``. This requires
the ``image:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/images/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     If the ``Accept`` header was set to ``application/x-qemu-disk``
                               then the image file itself will be sent in the
                               response body.

                               Otherwise, the :ref:`image <image-entity>` will
                               be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Delete image
============

.. code-block::

   DELETE /images/:id

This will delete the :ref:`image <image-entity>` by the given ``:id``. This
requires the ``image:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/images/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
