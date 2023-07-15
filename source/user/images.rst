======
Images
======

An image is what is used by the Docker and QEMU drivers to setup the build
environment for build execution. A user can upload custom images to use for
their builds. Right now Djinn CI only supports the uploading of QEMU driver
images.

.. note::
   Since the Docker driver uses Docker Hub to download images, you can specify
   any image for this driver to use, and as long as the Djinn Server can talk to
   the Docker Hub, that image will be downloaded and used.

Default images
==============

Djinn CI comes with a set of default images for the QEMU driver that can be
used. The full list of these images can be found on the Djinn CI
`image server`_.

.. _image server: https://images.djinn-ci.com

Creating an image
=================

Images are created from the Images link the dashboard's sidebar, and by clicking
the Create button in the top right hand corner.

Images for the QEMU driver are expected to be QCOW2 (v3) image file. It is
expected for the ``root`` user to have no password and for SSH access to be
configured for the ``root`` user.

Images can be grouped in a namespace for use by other users who have access to
that same namespace. If the namespace being specified does not exist during
image creation then it will be created on the fly.

Preparing a QEMU image
----------------------

.. code::

    $ qemu-img create -f qcow2 my-image.qcow2 10G

With this image created you can now install an operating system of your choice,
and prepare it for use in Djinn CI as a custom image.

.. code::

   $ qemu-system-x86_64 -m 4096 \
       -cdrom ubuntu.iso \
       -net nic,model=virtio \
       -net user \
       -drive file=my-image.qcow2,media=disk,if=virtio

Once the operating has been installed we can go about configuring the image for
use. The QEMU driver in Djinn CI uses a passwordless ``root`` user to connect to
the machine to perform jobs, so we need to ensure that the ``root`` user has no
password.

.. code::

    $ passwd -d root

Next, we need to configure the SSH server to allow for a root login, and to
allow password authentication. Below is the typical SSH configuration used by
the base images provided by Djinn CI.

.. code::

   PermitRootLogin yes

   PasswordAuthentication yes
   PermitEmptyPasswords yes
   PubkeyAuthentication no

   ChallengeResponseAuthentication no
   GSSAPIAuthentication no

   UsePAM no
   UseDNS no

   AcceptEnv *

   PermitUserEnvironment yes

   Subsystem sftp internal-sftp

Using a custom image
====================

Once an image has been uploaded you can use it by simply specifying its name in
the build manifest,

.. code::

   driver:
     type: qemu
     image: my-image
