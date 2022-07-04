<div class="doc-section" markdown>

# Curator

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `djinn-curator` is the component that handles cleaning up of old artifacts
that exceed a given limit. Every minute this will trigger and remove the oldest
artifacts that exceed the configured limit of the curator.

* [External Dependencies](#external-dependencies)
* [Configuring the Curator](#configuring-the-curator)
* [Running the Curator](#running-the-curator)
* [Configuring the Curator Daemon](#configuring-the-curator-daemon)

</div>
</div>
</div>

<div class="doc-section" markdown>

## External Dependencies

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Detailed below are the software dependencies that the curator needs in order
to start and run,

</div>

| DEPENDENCY  | REASON                              |
|-------------|-------------------------------------|
| PostgreSQL  | Primary data store for the curator. |

</div>
</div>

<div class="doc-section" markdown>

## Configuring the Curator

<div class="doc-content panel" markdown>

{{ table("Curator parameters", "tables/admin/curator-config") }}

</div>

{{ code_snippet("EXAMPLE", "examples/conf/curator", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Running the Curator

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

To run the curator simply invoke the `djinn-curator` binary. There are only two
flags that can be given to the `djinn-curator` binary,

* `-config` - This specifies the configuration file to use, by default this
will be `djinn-curator.conf`.

* `-limit` - This specifies the limit in bytes to use for clearing up
artifacts, by default this will be set to `1073741824` (1GB).

</div>
</div>
</div>

<div class="doc-section" markdown>

## Configuring the Curator Daemon

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `dist` directory contains files for running the Djinn Curator as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that uses systemd, then be sure to run
`systemctl daemon-reload` upon placement of the service file.

</div>
</div>
</div>
