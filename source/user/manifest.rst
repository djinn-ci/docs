========
Manifest
========

The build manifest is a YAML file that describes how a build should be executed.
Detailed below are the different fields for the manifest, what they do, and if
they are required.

namespace
=========

The :doc:`namespace </user/namespaces>` to submit the build to. If the given
namespace does not exist, then it will be created, and have the visibility set
to ``private``. The format ``<path>@<user>`` is used to submit builds to a
namespace that you are a collaborator in.

.. code::

   # Standalone namespace
   namespace: project

   # Child namespace
   namespace: project/child

   # Namespace with owner
   namespace: project@owner

   # Namespace with owner and child
   namespace: project/child@owner

driver
======

The driver to use for the :doc:`driver </user/drivers>` to use for the build.
All drivers require the ``driver.type`` property. Each individual driver may
have a different configuration for each subsequent property, more detail about
the driver configuration can be found in :doc:`/user/drivers`.

.. code::

   # QEMU driver
   driver:
     type: qemu
     image: debian/stable

   # Docker driver
   driver:
     type: docker
     image: golang:latest
     workspace: /go

env
===

The environment variables to set within the build environment, this should be a
list of strings formatted as ``<key>=<value>``.

.. code::

   env:
   - PGADDR=host=localhost port=5432 dbname=djinn user=djinn password=secret sslmode=disable
   - EDITOR=ed
   - LOCALE=en_GB.UTF-8

objects
=======

The list of object to be placed in the build environment. This should be a list
of strings, where each item is the name of the object. The ``=>`` notation can
be used to specify the full destination location in the build environment.

.. code::

   objects:
   - data => /var/lib/data
   - keys.jks

sources
=======

The list of git repositories to clone into the build environment. Any repository
URL reconigzed by ``git clone`` can be used.

.. code::

   sources:
   - https://github.com/andrewpillar/req
   - git@github.com:andrewpillar/mgrt.git

The destination to clone into can be set via ``=>`` notation.

.. code::

   sources:
   - https://github.com/andrewpillar/req.git => req

The ref to checkout once cloned can be specified at the end of the URL.

.. code::

   sources:
   - https://github.com/andrewpillar/req.git v1.0.0 => req

If any of the sources fail to clone, then the build itself will fail.

stages
======

The order in which the stages should be executed.

.. code::

   stages
   - test
   - build

allow_failures
===============

The stages that are allowed to fail. This will result in the stage being marked
as ``passed_with_failures``.

.. code::

   allow_failures:
   - test

jobs
====

The jobs for the build to run. Each jjob will be executed in the order in which
it is specified.

.. code::

   jobs:
   - stage: build
     commands:
     - go build -o a.out
     artifacts:
     - a.out

name
----

The name of the job, if no name is given, then the stage name will be used in
the format of ``stage.n``, where ``n`` is the number of that job in the stage.
For example, ``test.1``, or ``build.1``.

stage
-----

The name of the stage the job belongs to. If the given stage name does not exist
then the job will be ignored.

commands
--------

The list of commands to run during job executed. Each command should be it's own
separate item. A command can be any string that is valid by the shell that is
interpreting it, this can vary depending on the driver being used.

artifacts
---------

The list of files to collect from the build environment upon job completion.
This can use the ``=>`` notation to specify the name the artifact should be
collected as,

.. code::

   artifacts:
   - a.out => program

Example
=======

.. code::

   namespace: djinn
   driver:
     type: qemu
     image: djinn-dev
   sources:
   - https://djinn-ci.com.git => djinn
   env:
   - PGPASSWORD=secret
   - LDFLAGS=-s -w
   stages:
   - setup
   - integration
   - make
   jobs:
   - stage: setup
     commands:
     - psql -U djinn -h localhost -d djinn -f djinn/schema.sql
   - stage: integration
     commands:
     - cd djinn
     - go test -v -tags "integration" ./integration
   - stage: make
     commands:
     - cd djinn
     - ./make.sh
     artifacts:
     - djinn/bin/djinn
     - djinn/bin/djinn-curator
     - djinn/bin/djinn-scheduler
     - djinn/bin/djinn-server
     - djinn/bin/djinn-worker
     - djinn/bin/sum.manif
