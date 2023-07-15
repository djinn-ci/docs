========
Tutorial
========

This document walks you through submitting your first successful build on Djinn
CI, after which you should have a high-level overview as to how Djinn CI works.

Prerequisites
=============

To start using Djinn CI, you will need ann account. You can either `create`_ an
account, or `login`_ using `GitHub`_, or `GitLab`_.

.. _create: https://djinn-ci.com/register
.. _login: https://djinn-ci.com/login
.. _GitHub: https://github.com
.. _GitLab: https://gitlab.com

Your first build
================

Once logged in, click the `Submit`_ button on the homepage. From here you will
be able to submit your first build to Djinn CI.

.. _Submit: https://djinn-ci.com/builds/create

Build's in Djinn CI are described using YAML :doc:`manifests </user/manifest>`
These manifests describe how the build is executed, from the driver to use, the
jobs to run, and the artifacts to collect. Below is a simple manifest to
demonstrate this,

.. code-block::

   driver:
     type: qemu
     image: debian/stable
   stages:
   - os
   jobs:
   - stage: os
     commands:
     - cat /etc/os-release
     artifacts:
     - /etc/os-release

From this same page we can also add a comment to the build, and some tags to
help search for it later on. Tags are simple a comma separated list of strings.

Submitting the manifest will redirect you to the newly submitted build. From
here you will be able to see the status of the build as it's processed by Djinn
CI.

Once the build has finished processing its status will be updated to reflect so.
If successful the build will be marked as passed. From the "Artifacts" tab of
the build page you will be able to see the /etc/os-release artifact we collected
from the build.

Building code
=============

Now that we've submitted a simple build manifest let's submit another one, only
this time let's actually build some source code, and collect the artifacts from
it.

.. code-block::

   driver:
     type: qemu
     image: debian/stable
   env:
   - GOVERSION=1.18
   sources:
   - https://github.com/djinn-ci/imgsrv.git
   - https://github.com/golang/tools
   - https://github.com/valyala/quicktemplate
   stages:
   - deps
   - make
   jobs:
   - stage: deps
     commands:
     - wget -q https://go.dev/dl/go${GOVERSION}.linux-amd64.tar.gz
     - tar -xzf go${GOVERSION}.linux-amd64.tar.gz
     - mv go /usr/local
     - ln -sf /usr/local/go/bin/go /usr/local/bin/go
     - ln -sf /usr/local/go/bin/gofmt /usr/local/bin/gofmt
     - cd ~/tools/cmd/stringer
     - go build
     - mv stringer /usr/local/bin
     - cd ~/quicktemplate/qtc
     - go build
     - mv qtc /usr/local/bin
   - stage: make
     commands:
     - cd ~/imgsrv
     - ./make.sh
     artifacts:
     - imgsrv/bin/djinn-imgsrv

The above manifest will download the source for the `Djinn CI Image Server`_,
including the dependencies necessary, build it, and collect the built
binary.

.. _Djinn CI Image Server: https://images.djinn-ci.com

Further reading
===============

:doc:`Builds </user/builds>` - Learn about what a build is, how they're defined
and how they're executed.

:doc:`Manifest </user/manifest>` - Learn about build manifests, and what each
property within a manifest is used for during build execution.

:doc:`Drivers </user/drivers>` - Learn about the different drivers that can be
used for executing builds.

:doc:`Namespaces </user/namespaces>` - Learn about how namespaces can be used
for grouping builds and their resources together.

:doc:`Repos </user/repos>` - Learn how to trigger builds from pushes to GitHub
or GitLab.
