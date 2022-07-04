<div class="doc-section" markdown>

# Configuration

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Each configuration file for Djinn CI uses its own structured configuration
language. This provides a quick overview of that language, and the common
parameters between files.

* [Overview](#overview)
* [Common configuration](#common-configuration)
* [Environment variables](#environment-variables)

</div>
</div>
</div>

<div class="doc-section" markdown>

## Overview

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The syntax of the configuration files is detailed below using Extended
Backus-Naur Form,

</div>

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

</div>
</div>

<div class="doc-section" markdown>

## Common configuration

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

All of the configuration files used, with the exception of `driver.conf`, share
the following configuration parameters,

</div>

{{ table("", "tables/admin/common-config") }}

<div class="panel-body" markdown>

The `include` keyword can be used to include other configuration files. This
can be useful when multiple configuration file share the same configuration
parameters, such as SMTP connections, for example,

</div>

    include "/etc/djinn/smtp.cfg"

<div class="panel-body" markdown>

this can also be given an array of paths to include,

</div>

    include [
        "/etc/djinn/crypto.cfg",
        "/etc/djinn/smtp.cfg",
    ]

</div>
</div>

<div class="doc-section" markdown>

## Environment variables

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
Environment variables can be accessed in configuration files by wrapping the
variable name with `${}`. For example,
</div>

    smtp {
        username "${SMTP_USERNAME}"
    }

<div class="panel-body" markdown>
The above configuration would replace `${SMTP_USERNAME}` with the value of the
`SMTP_USERNAME`  environment variable. If no variable is set, then the value
would be an empty string.
</div>

</div>
