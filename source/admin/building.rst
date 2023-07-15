========
Building
========

To build Djinn CI, you will need to install the following dependencies,

* ``go`` - https://go.dev/dl
* ``yarn`` - https://yarnpkg.org/getting-started/install
* ``stringer`` - https://github.com/golang/tools
* ``qtc`` - https://github.com/valyalal/quicktemplate#quick-start

make sure each of these programs are installed an in your ``PATH``.

Once installed, clone the repository,

.. code::

   $ git clone https://github.com/djinn-ci/djinn

once cloned, change into the directory and run the ``make.sh`` script. This will
execute all of the tests, transpile the LESS and templates, then build the
curator, consumer, scheduler, server, the worker, and the offline runner.

.. code::

   $ ./make.sh

The compiled programs will be,

* ``bin/djinn``
* ``bin/djinn-consumer``
* ``bin/djinn-curator``
* ``bin/djinn-scheduler``
* ``bin/djinn-server``
* ``bin/djinn-worker``

each of these will be a statically linked binary. The target operating system
and architecture can be changed via ``GOOS`` and ``GOARCH`` environment
variables.

.. code::

   $ GOOS=freebsd GOARCH=amd64 ./make.sh

the flags of the linker can be configured via the ``LDFLAGS`` variable. This
will accept any flags that can normally be configured via the ``-ldflags`` flag
that is passed to the ``go build`` command,

.. code::

   $ LDFLAGS="-s -w" ./make.sh
