=========
Variables
=========

Variables can not only be set in build manifest files, but also as "global"
variables to be used across multiple builds.

Creating a variable
===================

Variables a created from the Variables link the dashboard's sidebar, and by
clicking the Create button in the top right hand corner.

A variable's name can only contain letters, numbers, and underscores. A
variable's name cannot have a leading number. The value of the variable can be
anything.

Variables can be grouped into a namespace, doing this will mean all builds
submitted to that namespace will have the given variable set on it.

Masked variables
================

A variable can be masked by simply selecting the Mask checkbox during creation.
This will encrypt the variable's value in the backend, and will replace any
occurrence of the variable's value in build logs with ``xxxxxx``.

Only the author of a variable can unmask a masked variable via the UI so see
its original value.

Using a variable
================

Variables are set as environment variables in the build environment, just like
variables in the build manifest.
