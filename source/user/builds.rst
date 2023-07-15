======
Builds
======

Builds are described via a build :doc:`/user/manifest`. These detail the driver
to use for execution, the code sources to pull in, the objects to place, the
stages and their respective jobs to execute, and the artifacts to collect.

Statuses
========

Detailed below are the different statuses that a build can be marked as.

.. csv-table::
   :header: "STATUS", "DESCRIPTION"
   :widths: auto

    "Queued", "The build has been submitted, but not started execution."
    "Running", "The build is in the process of being executed."
    "Passed", "The build passed without failures."
    "Passed with failures", "The build passed but a stage that was allowed to fail failed."
    "Failed", "A stage in the build failed."
    "Killed", "The build was killed."
    "Timed out", "The build took too long to execute."

Builtin jobs
============

When a build is submitted, a handful of jobs will be added to that build. The
first job added would be the driver creation job, that simply exists to capture
the output of driver creation. A job is added to the build for each source that
is defined in the build manifest.

The order of build execution
============================

Driver creation
---------------

First the build's driver is created before the build itself is executed. If the
driver creation exceeds 5 minutes then the build will be cancelled and marked
as ``Timed out``.

Object placement
----------------

The objects specified in the Objects property of the manifest are placed in the
build environment. Failure to place an object will not cause the build to fail.

Source cloning
--------------

Each source repository specified in the Sources property of the manifest are
cloned. If any of the cloning fails then the build will fail.

Stage execution
---------------

Each stage is then executed in the order specified in the Stages property. After
each job in the stage has completed execution then the artifacts specified via
the Artifacts property will be collected. If a stage fails then this marks the
build as Failed. If a stage failed, but is allowed to fail then the build is
marked as Passed With Failures.

Driver destruction
------------------

Once the build has finished execution, either successfully or unsuccessfully,
then the driver is destroyed.

What a job looks like
=====================

For the QEMU and Docker drivers, each job in a build is treated as an individual
shell script. All of the commands in a job are concatenated together and put
into a single script, for example the following job,

.. code::

   jobs:
   - stage: test
     commands:
     - cd djinn
     - go test -cover ./...
     - go test -tags "integration" ./integration

would become the shell script,

.. code::

    #!/bin/sh
    exec 2>&1
    set -ex

    cd djinn
    go test -cover ./...
    go test -tags "integration" ./integration

each shell script is placed into the build environment and then executed.

Build artifacts
===============

Artifacts are collected from each build job after the job has completed. These
artifacts are deleted during curation when they exceed the user's configured
cleanup threshold, by default this is 1GB. If a build is pinned however, then
its artifacts will not be deleted.
