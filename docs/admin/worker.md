<div class="doc-section" markdown>

# Worker

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `djinn-worker` is the component that handles executing builds that are
submitted via the [server](/admin/server) or the [scheduler](/admin/scheduler).
You may need to install some additional dependencies on the worker machine
depending on the drivers you want to make available.

* [External Dependencies](#external-dependencies)
* [Driver Dependencies](#driver-dependencies)
* [Configuring the Worker](#configuring-the-worker)
* [Running the Worker](#running-the-worker)
* [Configuring the Worker Daemon](#configuring-the-worker-daemon)

</div>
</div>
</div>

<div class="doc-section" markdown>

## External Dependencies

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Detailed below are the software dependencies that the worker needs in order
to start and run,

</div>

| DEPENDENCY  | REASON                                     |
|-------------|--------------------------------------------|
| PostgreSQL  | Primary data store for the server.         |
| Redis       | Data store used as the build queue.        |
| SMTP Server | Used for sending emails on build failures. |

</div>
</div>

<div class="doc-section" markdown>

## Driver Dependencies

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Detailed below are the software dependencies that the worker needs in order
to execute a build via that driver.

</div>

| DRIVER   | SOFTWARE                                                   |
|----------|------------------------------------------------------------|
| `docker` | The `dockerd` process for managing containers.             |
| `qemu`   | The `qemu` software package for creating virtual machines. |

</div>
</div>

<div class="doc-section" markdown>

## Configuring the worker

<div class="doc-content panel" markdown>

{{ table("Worker parameters", "tables/admin/worker-config") }}

<div class="panel-body" markdown>
>**Note:** The worker does not need the `client_id` or `client_secret` details
of a provider. For example, `provider github {}` will suffice for GitHub
integration.
</div>
</div>

{{ code_snippet("EXAMPLE", "examples/conf/worker", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Running the Worker

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

To run the worker simply invoke the `djinn-worker` binary. There are two flags
that can be given to the `djinn-worker` binary.

* `-config` - This specifies the configuration file to use, by default
this will be `djinn-worker.conf`.

* `-driver` - This specifies the driver configuration file to use, for
configuring the drivers you want to support on your server, by default this
will be `djinn-driver.conf`.

</div>
</div>
</div>

<div class="doc-section" markdown>

## Configuring the Worker Daemon

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `dist` directory contains files for running the Djinn Worker as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that uses systemd, then be sure to run
`systemctl daemon-reload` upon placement of the service file.

</div>
</div>
