=============
Configuration
=============

Each configuration file for Djinn CI uses its own structured configuration
language. This provides a quick overview of that language, and the common
parameters between files.

.. contents::
   :local:
   :backlinks: none

Overview
========

The syntax of the configuration files is detailed belong using Extended
Backus-Naur Form,

.. code::

   digit  = "0" ... "9" .
   letter = "a" ... "z" | "A" ... "Z" | "_" | unicode_letter .

   identifier = letter { letter | digit } .

   float_literal  = digit "." { digit } .
   int_literal    = { digit } .
   number_literal = int_literal | float_literal .

   duration_unit    = "s" | "m" | "h" .
   duration_literal = number_literal { number_literal | duration_unit } .

   size_unit    = "B" | "KB" | "MB" | "GB" | "TB" .
   size_literal = int_literal size_unit .

   string_literal = `"` { letter } `"` .

   bool_literal = "true" | "false" .

   literal = bool_literal | string_literal | number_literal | duration_literal | size_literal .

   block   = "{" [ parameter ";" ] "}" .
   array   = "[" [ operand "," ] "]" .
   operand = literal | array | block .

   parameter = identifier [ identifier ] operand .

   file = { parameter ";" } .

Common configuration
====================

All of the configuration files used, with the exception of ``driver.conf``,
share the following configuration parameters,

===============  =============  ===========
NAME             TYPE           DESCRIPTION
===============  =============  ===========
``pidfile``       ``string``    The file to which the PID should be written when
                                the process starts.
``log <label>``   ``string``    Configure logging for the process, ``<label>``
                                should be one of:

                                * ``debug``
                                * ``info``
                                * ``warn``
                                * ``error``
``include``       ``string``    The file or files to include in the configuration
                  ``string[]``  file.
===============  =============  ===========

The ``include`` keyword can be used to include other configuration files. This
can be useful when multiple configuration files share the same configuration
parameters, such as SMTP connections, for example,

.. code::

   include "/etc/djinn/smtp.cfg"

this can also be given an array of paths to include,

.. code::

   include [
       "/etc/djinn/crypto.cfg",
       "/etc/djinn/smtp.cfg",
   ]

Environment variables
=====================

Environment variables can be accessed in configuration files by wrapping the
variable name with ``${}``. For example,

.. code::

   smtp {
       username "${SMTP_USERNAME}"
   }

The above configuration would replace ``${SMTP_USERNAME}`` with the value of the
``SMTP_USERNAME`` environment variable. If no variable is set, then the value
would be an emtpy string.
