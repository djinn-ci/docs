======
Builds
======

Entities
========

.. _build-entity:

Build entity
------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the build.
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who
                                  submitted the build.
``namespace_id``   ``int``        ID of the :ref:`namespace <namespace-entity>`
                   ``nullable``   the build belongs to, if any.
``number``         ``int``        Number of the build for the user it belongs to.
``manifest``       ``string``     The build :doc:`manifest </user/manifest>`.
``status``         ``enum``       The status of the build, will be one of:

                                  - ``queued``
                                  - ``running``
                                  - ``passed``
                                  - ``passed_with_failures``
                                  - ``failed``
                                  - ``killed``
                                  - ``timed_out``
``output``         ``string``     The output of the build, if any.

                   ``nullable``
``tags``           ``string[]``   The list of tags on the build.
``pinned``         ``bool``       Whether or not the build has been pinned.
``created_at``     ``timestamp``  The RFC3339 formatted string at which the build
                                  was created.
``started_at``     ``timestamp``  The RFC3339 formatted string at which the build
                                  started.
                   ``nullable``
``finished_at``    ``timestamp``  The RFC3339 formatted string at which the build
                                  finished.
                   ``nullable``
``url``            ``string``     The API URL to the build entity itself.
``objects_url``    ``string``     The API URL to the build's objects.
``variables_url``  ``string``     The API URL to the build's variables.
``jobs_url``       ``string``     The API URL to the build's jobs.
``artifacts_url``  ``string``     The API URL to the build's artifacts.
``tags_url``       ``string``     The API URL to the build's tags.
``user``           ``object``     The :ref:`user <user-entity>` the build belongs
                                  to.
                   ``nullable``
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  build belongs to.
                   ``nullable``
``trigger``        ``object``     The trigger of the build.
=================  =============  ===========

.. _trigger-entity:

Trigger entity
--------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``type``           ``enum``       The type of trigger for the build, will be one
                                  of:

                                  - ``manual``
                                  - ``push``
                                  - ``pull``
                                  - ``schedule``
``comment``        ``string``     The comment associated with the build.
``data``           ``object``     A ``string:string`` object of the data about
                                  the trigger, such as who authored it, and any
                                  commit information associated with it, if it
                                  was a ``push`` or ``pull`` trigger.
=================  =============  ===========

.. _build-job-entity:

Job entity
----------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the job.
``build_id``       ``int``        ID of the :ref:`build <build-entity>` the job
                                  belongs to.
``stage``          ``string``     The name of the stage the job belongs to.
``name``           ``string``     The name of the job.
``commands``       ``string``     The commands for the job.
``status``         ``enum``       The status of the job, will be one of:

                                  - ``queued``
                                  - ``running``
                                  - ``passed``
                                  - ``passed_with_failures``
                                  - ``failed``
                                  - ``killed``
                                  - ``timed_out``
``output``         ``string``     The output of the job, if any.
                   ``nullable``
``created_at``     ``timestamp``  The RFC3339 formatted string at which the job
                   ``nullable``   was created.
``started_at``     ``timestamp``  The RFC3339 formatted string at which the job
                   ``nullable``   started.
``finished_at``    ``timestamp``  The RFC3339 formatted string at which the job
                   ``nullable``   finished.
                   ``nullable``
``url``            ``string``     The URL to access the job.
``build``          ``object``     The :ref:`build <build-entity>` of the job.
=================  =============  ===========

.. _build-object-entity:

Build object entity
-------------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the build object.
``build_id``       ``int``        ID of the :ref:`build <build-entity>` the
                                  object was placed on.
``source``         ``string``     The original name of the object.
``name``           ``string``     The name of the object it was placed as.
``type``           ``string``     The MIME type of the object.
                   ``nullable``
``md5``            ``string``     The MD5 hash of the object.
                   ``nullable``
``sha256``         ``string``     The SHA256 hash of the object.
                   ``nullable``
``placed``         ``bool``       Whether or not the object was placed.
``object_url``     ``string``     The API URL to the original
                                  :ref:`object <object-entity>` itself.
``build``          ``object``     The :ref:`build <build-entity>` object.
=================  =============  ===========

.. _build-variable-entity:

Build variable entity
---------------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the build variable.
``build_id``       ``int``        ID of the :ref:`build <build-entity>` the
                                  variable belongs to.
``key``            ``string``     The name of the variable.
``value``          ``string``     The value of the variable, if masked will be
                                  ``xxxxxx``.
``masked``         ``bool``       Whether or not the variable was masked.
``variable_url``   ``string``     The API URL to the original
                                  :ref:`variable <variable-entity>` itself.
``build``          ``object``     The :ref:`build <build-entity>` object.
=================  =============  ===========

.. _build-artifact-entity:

Artifact entity
---------------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the artifact.
``build_id``       ``int``        ID of the :ref:`build <build-entity>` the
                                  variable belongs to.
``job_id``         ``int``        ID of the :ref:`job <build-job-entity>` the
                                  artifact belongs to.
``source``         ``string``     The original name of the artifact from the
                                  build environment.
``name``           ``string``     The name of the artifact it was collected as.
``size``           ``int``        The size of the artifactl. Will be ``null`` if
                   ``nullable``   not collected.
``md5``            ``string``     The MD5 hash of the artifact. Will be ``null``
                   ``nullable``   if not collected.
``sha256``         ``string``     The SHA256 hash of the artifact. Will be
                   ``nullable``   ``null`` if not collected.
``created_at``     ``timestamp``  The RFC3339 formatted time at which the
                                  artifact was created.
``url``            ``string``     The API URL to the artifact itself.
``user``           ``object``     The :ref:`user <user-entity>` of the artifact.
``build``          ``object``     The :ref:`build <build-entity>` the artifact
                                  was collected from.
``job``            ``object``     The :ref:`job <build-job-entity>` the artifact
                                  was collected from.
=================  =============  ===========

.. _build-tag-entity:

Tag entity
----------

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``user_id``        ``int``        ID of the :ref:`user <user-entity>` who created
                                  the tag.
``build_id``       ``int``        ID of the :ref:`build <build-entity>` the tag
                                  is on.
``name``           ``string``     The name of the tag.
``created_at``     ``timestamp``  The RFC3339 formatted time at which the tag
                                  was created.
``url``            ``string``     The API URL to the tag itself.
``user``           ``object``     The :ref:`user <user-entity>` of the tag.
``build``          ``object``     The :ref:`build <build-entity>` of the tag.
=================  =============  ===========

List builds
===========

.. code-block::

   GET /builds

List the :ref:`builds <build-entity>` for the currently authenticated
:ref:`user <user-entity>`. The following parameters can be given as query
parameters to the URL. This requires the ``build:read`` permission.

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

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/builds

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

Create build
============

.. code-block::

   POST /builds

This will submit a new :ref:`build <build-entity>` to the server for the
currently authenticated :ref:`user <user-entity>`. The following parameters
need to be given as a JSON encoded payload in the request body. This requires
the ``build:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``manifest``       ``string``     Yes       The YAML formatted build
                                            :doc:`manifest </user/manifest>`.
``comment``        ``string``     No        The build's comment. Use this to
                                            describe the purpose of the build.
``tags``           ``string[]``   No        The build's tags.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -H "Content-Type: application/json" \
       -d '{"manifest":"namespace: djinn\ndriver:\n  image: centos/7\n  type: qemu\nenv:\n- LOCALE=en_GB.UTF-8\nobjects:\n- data => data\nstages:\n- clean\njobs:\n- stage: clean\n  commands:\n  - tr -d '0-9' data > data.cleaned\n  artifacts:\n  - data.cleaned => data.cleaned"}' \
       https://api.djinn-ci.com/builds

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``201 Created``                The :ref:`build <build-entity>` will be the
                               response body.
``400 Bad Request``            :ref:`Validation error <validation-errors>` response.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build
=========

.. code-block::

   GET /b/:username/:number

This will get the :ref:`build <build-entity>` by the given ``:username``, with
the given ``:number``. This requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`build <build-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build objects
=================

.. code-block::

   GET /b/:username/:number/objects

This will get the :ref:`objects <build-object-entity>` on the given build. The
following parameters can be given as query parameters to the URL. This requires
the ``build:read`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``search``         ``string``     No        Get the objects with names like the
                                            given value.
=================  =============  ========  ===========

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/objects

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`objects <build-object-entity>` will be
                               the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build variables
===================

.. code-block::

   GET /b/:username/:number/variables

This will get the :ref:`variables <build-variable-entity>` on the given build.
This requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/variables

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`variables <build-variable-entity>` will
                               be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build jobs
==============

.. code-block::

   GET /b/:username/:number/jobs

This will get the :ref:`jobs <build-job-entity>` on the given build. This
requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/jobs

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`jobs <build-job-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build job
=============

.. code-block::

   GET /b/:username/:number/jobs/:name

This will get the :ref:`job <build-job-entity>` by the given ``:name``, on the
given build. This requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/jobs/setup.1

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`job <build-job-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build artifacts
===================

.. code-block::

   GET /b/:username/:number/artifacts

This will get the :ref:`artifacts <build-artifact-entity>` on the given build.
This requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/artifacts

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`artifacts <build-artifact-entity>` will
                               be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build artifact
==================

.. code-block::

   GET /b/:username/:number/artifacts/:name

This will get the :ref:`artifact <build-artifact-entity>` by the given ``:name``,
on the given build. This requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/artifacts/build.log

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     If the ``Accept`` header was set to ``application/octet-stream``
                               then the contents of the artifact will be sent in
                               the response body, with the ``Content-Type`` header
                               set to the detected MIME type of the artifact.

                               Otherwise, the :ref:`artifact <build-artifact-entity>`
                               will be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Get build tags
==============

.. code-block::

   GET /b/:username/:number/tags

This will get the :ref:`tags <build-tag-entity>` on the given build. This
requires the ``build:read`` permission.

.. code-block::

   $ curl -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/tags

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`tags <build-tag-entity>` will be the
                               response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Create build tag
================

.. code-block::

   POST /b/:username/:number/tags

This will add a :ref:`tag <build-tag-entity>` to the given build. The following
parameters need to be given as a JSON encoded payload in the request body. This
requires the ``build:write`` permission.

**Parameters**

=================  =============  ========  ===========
NAME               TYPE           REQUIRED  DESCRIPTION
=================  =============  ========  ===========
``--``             ``string[]``   Yes       An array of strings submitted as the
                                            request body.
=================  =============  ========  ===========

.. code-block::

   $ curl -X POST \
       -H "Authorization: Bearer 1a2b3c4d5f" \
       -d '["tag1", "tag2", "tag3"]' \
       https://api.djinn-ci.com/b/me/10/tags

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``201 Created``                The list of :ref:`tags <build-tag-entity>` will
                               be the response body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Delete build tag
================

.. code-block::

   DELETE /b/:username/:number/tags/:name

This will remove the :ref:`tag <build-tag-entity>` by the given ``:name``, from
the given build. This requires the ``build:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/tags/tag1

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Pin build
=========

.. code-block::

   PATCH /b/:username/:number/pin

This will pin the given build. This requires the ``build:write`` permission.

.. code-block::

   $ curl -X PATCH -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/pin

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`build <build-entity>` will be the response
                               body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Unpin build
===========

.. code-block::

   PATCH /b/:username/:number/unpin

This will unpin the given build. This requires the ``build:write`` permission.

.. code-block::

   $ curl -X PATCH -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10/unpin

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``200 OK``                     The :ref:`build <build-entity>` will be the response
                               body.
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========

Kill build
==========

.. code-block::

   DELETE /b/:username/:number

This will kill a :ref:`build <build-entity>` that is running. This requires
the ``build:delete`` permission.

.. code-block::

   $ curl -X DELETE -H "Authorization: Bearer 1a2b3c4d5f" https://api.djinn-ci.com/b/me/10

**Responses**

=============================  ===========
STATUS CODE                    BODY
=============================  ===========
``204 No Content``
``404 Not Found``              Will happen when unauthorized.
``500 Internal Server Error``  :ref:`Internal error <internal-errors>` response.
=============================  ===========
