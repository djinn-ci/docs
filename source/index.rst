:nolocaltoc:

.. Djinn CI Docs documentation master file, created by
   sphinx-quickstart on Sun May 21 16:04:39 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========
Overview
========

.. toctree::
   :hidden:
   :maxdepth: 1

   tutorial

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: USER

   user/overview
   user/builds
   user/namespaces
   user/repos
   user/cron
   user/drivers
   user/manifest
   user/images
   user/objects
   user/keys
   user/variables
   user/webhooks
   user/offline-runner

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: API

   api/overview
   api/oauth
   api/builds
   api/cron
   api/images
   api/invites
   api/keys
   api/namespaces
   api/objects
   api/user
   api/variables

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: ADMIN

   admin/overview
   admin/building
   admin/configuration
   admin/consumer
   admin/curator
   admin/scheduler
   admin/server
   admin/worker

Djinn CI is a continous integration system for automating builds of a program's
source code, its features include:

* Running builds inside of Docker containers and Linux VMs
* Cron jobs for repeatable builds
* Namespaces for organizing builds, and their resources
* Custom Linux VM build images
* Integration with GitHub and GitLab for build triggers on pushes and pull
  requests
* Support for multi-repository builds
* Collect files from build environments via build artifacts
* Place files into build environments via build objects

Tutorial
========

Get started with Djinn CI, learn how to submit your first build, organize
resources into namespaces, and setup integration with external providers,
:doc:`read more... </tutorial>`

User documentation
==================

Learn about the build server at a high level, and how to use it to run your
builds. This will cover what a build is, how they're executed, and how you can
connect to an existing Git provider to have your builds trigger whilst you
develop, :doc:`read more... </user/overview>`

API documentation
=================

Learn how to interact with the build server via the JSON REST API. This will
cover everything from what resources the API server exposes, to how OAuth apps
can be created for interfacting wit hthe API,
:doc:`read more... </api/overview>`

Admin documentation
===================

Learn how to deploy and administer your own installation of the build server.
This will cover how to build the server from source, the recommended strategies
for deploying it, and how it should be administered,
:doc:`read more... </admin/overview>`
