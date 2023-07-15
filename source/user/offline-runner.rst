==============
Offline runner
==============

Djinn CI can be used to run your builds offline without having to submit them to
the build server. This does require having to configure the necessary drivers on
your machine however.

Installing the offline runner
=============================

To install the offline runner you will first need to build it using Go,

.. code::

   $ git clone https://github.com/djinn-ci/djinn

once cloned, change into the directory and run the ``make.sh`` script.

.. code::

   $ ./make.sh runner

This will produce a binary called ``bin/djinn``, simply move this binary into a
location that will make it accessible via your ``PATH``.

Configuring locations
=====================

For the offline runner, driver configuration sits in the ``driver.conf`` file.
By default, this is expected to be in the user config directory. Detailed below
is where the file will be found on the different operating systems,

**Unix**

If non-empty, then the ``XDG_CONFIG_HOME`` variable is used, and the full path
would be ``$XDG_CONFIG_HOME/djinn/driver.conf``. Otherwise, it will use
``~/.config/djinn/driver.conf``.

**Darwin**

On Darwin, the path used will be ``$HOME/Library/Application Support/djinn``.

**Windows**

On Windows, the path used will be, ``%AppData%/djinn``.

Configuring drivers
===================

.. note::
   The same driver configuration used for the offline runner is used for the
   worker too.

Each driver supported by Djinn CI, is configured in its own block directive
in the ``driver.conf`` file like so,

.. code::

   driver <name> {
       ...
   }

where ``<name>`` is the name of the driver being configured, followed by a
list of value directives. For example, to configure the QEMU driver you would
do,

.. code::

   driver qemu {
       disks  "/home/me/.config/djinn/images/qemu"
       cpus   1
       memory 2048
   }

the above configuration would set the location of the QEMU disk images to use,
the number of CPUs, and the amount of memory for each machine that will be
created.

For a completed example of a ``driver.conf`` file see the ``dist`` directory
of the source repository.

Docker
======

Detailed below are the value directives used by the Docker driver.

===========  ==========  ===========
NAME         TYPE        DESCRIPTION
===========  ==========  ===========
``host``     ``string``  The host of the running Docker daemon, can be a path to
                         a Unix socket.
``version``  ``string``  The version of the Docker API to use.
===========  ==========  ===========

QEMU
====

Detailed below are the value directives used by the QEMU driver.

===========  ===========  ===========
NAME         TYPE         DESCRIPTION
===========  ===========  ===========
``disks``    ``string``   Where the QEMU disk images are on the filesystem.
``cpus``     ``int``      The number of CPUs to use for the QEMU machines.
``memory``   ``int``      The amount of memory in bytes for the QEMU machines.
===========  ===========  ===========

The directory specified in ``disks`` must have a another sub-directory for each
architecture, in each of these exist the disk images to use. For example assume
a manifest declares the following,

.. code::

   driver:
     type: qemu
     image: debian/stable

then the offline runner will look for the following disk image,

.. code::

   /home/me/.config/djinn/images/qemu/x86_64/debian/stable
