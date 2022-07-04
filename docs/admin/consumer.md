<div class="doc-section" markdown>

# Consumer

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `djinn-consumer` is the component that handles the processing of background
jobs, such as remote image downloads. This will pull jobs from Redis off the
`jobs` queue for processing.

* [External Dependencies](#external-dependencies)
* [Configuring the Consumer](#configuring-the-consumer)
* [Running the Consumer](#running-the-consumer)
* [Configuring the Consumer](#configuring-the-consumer)

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

| DEPENDENCY  | REASON                                            |
|-------------|---------------------------------------------------|
| PostgreSQL  | Primary data store for the consumer.              |
| Redis       | Data store used as the job queue to consume from. |

</div>
</div>

<div class="doc-section" markdown>

## Configuring the Consumer

<div class="doc-content panel" markdown>

{{ table("Consumer parameters", "tables/admin/consumer-config") }}

</div>

{{ code_snippet("EXAMPLE", "examples/conf/consumer", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Running the Consumer

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

To run the consumer simply invoke the `djinn-consumer` binary. There is only
one flag that can be given to the `djinn-consumer` binary,

* `-config` - This specifies the configuration file to use, by default this
will be `djinn-consumer.conf`.

</div>
</div>
</div>

<div class="doc-section" markdown>

## Configuring the Consumer Daemon

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `dist` directory contains files for running the Djinn Consumer as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that uses systemd, then be sure to run
`systemctl daemon-reload` upon placement of the service file.

</div>
</div>
</div>
