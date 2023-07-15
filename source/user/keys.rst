====
Keys
====

SSH keys can be uploaded to Djinn CI to be used in the build environment. These
will be added to the build environment after driver creation. Each SSH key that
is uploaded is encrypted, and can have custom SSH configuration along side it.
With this you will be able to clone from private repositories.

.. note::
   If you are concerned about the security of adding keys to the build
   environment, then it is recommended you create a separate key that is used
   for cloning repositories only.

Creating a key
==============

Keys are created from the SSH Keys link the dashboard's sidebar, and by clicking
the Create button in the top right hand corner.

A key needs to be a valid SSH private key. During creation you will have the
option to specify configuration for that key, for example,

.. code::

   Host github.com
       User git
       IdentityFile /root/.ssh/id_deploy

the given name of the SSH key will be normalized with ``_``, for example if you
give the key a name of ``my deploy key`` then it will be stored and referenced
as ``my_deploy_key``.

Keys can be grouped into a namespace just as any other resource.

Using a key
===========

You don't need to add anything to a build manifest for a key to be placed into
the build environment. All keys available to the build through a namespace will
be placed into the build environment, and all key configurations will be
collated into a single ``/root/.ssh/config`` file on the build environment.
