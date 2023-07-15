========
Webhooks
========

Webhooks allow you to integrate with Djinn CI based on the events that happen
within Djinn CI. When one of these events is triggered, an HTTP POST request is
sent to the webhook's URL. What happens to these events when received is up to
the server that receives it. It could be used to notify people through various
communication channels, to update an issue tracker, or to kick off another
automated process.

Creating a webhook
==================

Navigate to the :doc:`namespace </user/namespaces>` you want to configure the
webhook for. From the Webhooks tab, you will be able to create a new webhook via
the Create webhook button. Webhooks can also be created via the REST API.

Signing webhooks
================

Secrets can be set on a webhook that is used for signing the payload of the
delivered event. Webhooks with secrets will include the signature in the request
headers,

.. code::

   X-Djinn-CI-Signature sha256=6a7f769...

the secret should be used from your end to compute the hash using an HMAC
digest, then compare that with what's in the header.

.. _event-payloads:

Event payloads
==============

build.submitted
---------------

This event is emitted whenever a new build is submitted to the webhook's
namespace for running.

build.started
-------------

This is event is emitted when a build begins being run, this shares the same
payload as the ``build.submitted`` event, only the ``started_at`` field will not
be ``null``.

build.finished
--------------

This is event is emitted when a build begins being run, this shares the same
payload as the ``build.submitted`` event, only the ``finished_at`` field will
not be ``null``.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``id``             ``int``        Unique ID for the build.
``user_id``        ``int``        ID of the user who submitted the build
``namespace_id``   ``int``        ID of the namespace the build belongs to, if
                   ``nullable``   any.
``number``         ``int``        Number of the build for the user it belongs to.
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

build.tagged
------------

This event is emitted whenever a new tag is added to a build. This will not be
emitted for tags that are added to a build at the time the build is submitted.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``build``          ``object``     The :ref:`build <build-entity>` that was tagged.
``tags``           ``object[]``   The array of :ref:`tags <build-tag-entity>` on the build.
``url``            ``string``     The API URL to the builds tags.
``user``           ``object``     The :ref:`user <user-entity>` that tagged the
                                  build.
=================  =============  ===========

invite.sent
-----------

This event is emitted when an invite is sent to a user.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``invitee``        ``object``     The :ref:`user <user-entity>` who received the
                                  invite.
``inviter``        ``object``     The :ref:`user <user-entity>` who sent the
                                  invite.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  invite was sent for.
=================  =============  ===========

invite.accepted
---------------

This event is emitted when an invite is accepted by a user.

invite.rejected
---------------

This event is emitted when an invite is rejected by a user.

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``invitee``        ``object``     The :ref:`user <user-entity>` who received the
                                  invite.
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  invite was sent for.
=================  =============  ===========

namespaces
----------

This event is emitted whenever a namespace is created, updated, or deleted.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``action``         ``enum``       The action performed on the namespace, will be
                                  one of:

                                  * ``created``
                                  * ``updated``
                                  * ``deleted``
``namespace``      ``object``     The :ref:`namespace <namespace-entity>` the
                                  action was performed on.
=================  =============  ===========

cron
----

This event is emitted whenever a cron job is created, updated, or deleted within
a namespace.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``action``         ``enum``       The action performed on the cron job, will be
                                  one of:

                                  * ``created``
                                  * ``updated``
                                  * ``deleted``
``cron``           ``object``     The :ref:`cron <cron-entity>` the action was
                                  performed on.
=================  =============  ===========

images
------

This event is emitted whenever an image is created, or deleted within a
namespace.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``action``         ``enum``       The action performed on the image, will be one
                                  of:

                                  * ``created``
                                  * ``updated``
                                  * ``deleted``
``image``          ``object``     The :ref:`image <image-entity>` the action was
                                  performed on.
=================  =============  ===========

objects
-------

This event is emitted whenever an object is created, or deleted within a
namespace.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``action``         ``enum``       The action performed on the object, will be
                                  one of:

                                  * ``created``
                                  * ``updated``
                                  * ``deleted``
``object``         ``object``     The :ref:`object <object-entity>` the action
                                  was performed on.
=================  =============  ===========

variables
---------

This event is emitted whenever a variable is created, or deleted within a
namespace.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``action``         ``enum``       The action performed on the variable, will be
                                  one of:

                                  * ``created``
                                  * ``updated``
                                  * ``deleted``
``variable``       ``object``     The :ref:`variable <variable-entity>` the action
                                  was performed on.
=================  =============  ===========

ssh_keys
--------

This event is emitted whenever an SSH key is created, udated, or deleted within
a namespace.

**Payload**

=================  =============  ===========
NAME               TYPE           DESCRIPTION
=================  =============  ===========
``action``         ``enum``       The action performed on the variable, will be
                                  one of:

                                  * ``created``
                                  * ``updated``
                                  * ``deleted``
``key``            ``object``     The :ref:`key <key-entity>` the action was
                                  performed on.
=================  =============  ===========
