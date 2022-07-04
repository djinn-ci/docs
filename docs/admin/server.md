<div class="doc-section" markdown>

# Server

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `djinn-server` is the primary component through which users would interact
with the CI server. This handles serving the UI and API endpoints for the
server. All assets served by the server are compiled into the binary itself,
so there is no need to worry about where assets will exist on disk.

* [External Dependencies](#external-dependencies)
* [Configuring the Server](#configuring-the-server)
* [Environment Variables](#environment-variables)
* [Running the Server](#running-the-server)
* [Proxying behind NGINX](#proxying-behind-nginx)
* [Configuring the Server Daemon](#configuring-the-server-daemon)

</div>
</div>
</div>

<div class="doc-section" markdown>

## External Dependencies

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Detailed below are the software dependencies that the server needs in order to
start and run,

</div>

| DEPENDENCY  | REASON                                                            |
|-------------|-------------------------------------------------------------------|
| PostgreSQL  | Primary data store for the server.                                |
| Redis       | Data store used as the build queue, and for storing session data. |
| SMTP Server | Used for sending emails on build failures.                        |

</div>
</div>

<div class="doc-section" markdown>

## Configuring the Server

<div class="doc-content panel" markdown>

{{ table("Server parameters", "tables/admin/server-config") }}

</div>

{{ code_snippet("EXAMPLE", "examples/conf/server", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Environment Variables

<div class="doc-content panel" markdown>

{{ table("", "tables/admin/server-env") }}

</div>
</div>

<div class="doc-section" markdown>

## Running the Server

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

To run the server simply invoke the `djinn-server` binary. There are three flags
that can be given to the `djinn-server` binary.

* `-config` - This specifies the configuration file to use, by default
this will be `djinn-server.conf`.

* `-api` - This tells the server to only serve the [REST API](/api) endpoints.

* `-ui` - This tells the server to only serve the UI endpoints.

If you do not specify either the `-api`, or `-ui` flag then both groups of
endpoints will be served. The [REST API](/api) endpoints will be served under
the `/api` prefix,

**Serving both the UI and API**

</div>

    $ djinn-server -config /etc/djinn/server.conf

<div class="panel-body" markdown>

**Serving just the API**

</div>

    $ djinn-server -config /etc/djinn/server.conf -api

<div class="panel-body" markdown>

**Serving just the UI**

</div>

    $ djinn-server -config /etc/djinn/server.conf -ui

</div>
</div>

<div class="doc-section" markdown>

## Proxying behind NGINX

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

It is recommended that you deploy Djinn CI behind an NGINX proxy. This will
give you more fine grained control over any timeouts that may occur when
uploading/downloading build images. An example NGINX configuration can be
found in the `dist` directory.

In the future, this may no longer be necessary should `net/http` support
configuring read/write timeouts on a per handler basis, see
[go/golang/issues/16100][0].

[0]: https://github.com/golang/go/issues/16100

</div>
</div>
</div>

<div class="doc-section" markdown>

## Configuring the Server Daemon

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `dist` directory contains files for running the Djinn Server as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that uses systemd, then be sure to run
`systemctl daemon-reload` upon placement of the service file.

</div>
</div>
</div>
