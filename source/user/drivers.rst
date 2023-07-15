=======
Drivers
=======

A driver is how a build is executed. In essence it is anything that can execute
a job that is specified in a build manifest. This can be anything from a Docker
container to a virtual machine or an SSH connection.

Configuring a driver
====================

Drivers to use for build execution are configured in the build manifest using
the ``driver`` property. Every driver is configured differently depending on the
type of driver being used, but each driver configuration does require the
``driver.type`` property, some examples are below,

**QEMU**

.. code::

   driver:
     type: qemu
     image: debian/stable

**Docker**

.. code::

   driver:
     type: docker
     image: golang
     workspace: /go

as a whole each driver is configured as a list of key value pairs, where each
value is a string.

Available drivers
=================

Detailed below are the different drivers that are available to use for builds.
Depending on how your Djinn Server is configured, will depend on the drivers
that are available for execution.

Docker
------

To configure Docker as the driver simply set the ``driver.type`` to ``docker``.
When a build is executed via the Docker driver then a new container is used to
execute each job in the build.

Detailed below are the properties required for the Docker driver,

.. csv-table::
   :header: "PROPERTY", "DESCRIPTION"
   :widths: auto

   "``driver.image``", "
    The Docker container image to use for the build. This will pull down the
    container image from Docker Hub."
    "``driver.workspace``", "
    The location in the Docker container where the container's volume will be
    mounted to. This volume is used to persist state across the containers that
    are used during build execution."

QEMU
----

To configure QEMU as the driver simply set the ``driver.type`` to ``qemu``. When
a build is executed via the QEMU driver, an SSH connection is opened up to the
local virtual machine, and all of the build jobs are executed as the root user.

Detailed below are the properties required for the QEMU driver,

.. csv-table::
   :header: "PROPERTY", "DESCRIPTION"
   :widths: auto

   "``driver.image``", "
   The QCOW2 image file to use when booting a new virtual machine for build
   execution. The base images available will vary depending on how your Djinn
   Server is configured."

SSH
---

To configure SSH as the driver simply set the ``driver.type`` to ``ssh``. When
a build is executed via the SSH driver, an SSH connection is opened up to the
configured address. This will try and connect to the specified server as the
root user.

.. csv-table::
   :header: "PROPERTY", "DESCRIPTION"
   :widths: auto

   "``driver.address``", "
   The address of the server that Djinn CI should connect to for build
   execution."
