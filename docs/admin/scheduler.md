<div class="doc-section" markdown>

# Scheduler

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `djinn-scheduler` is the component that handles the scheduling of cron jobs
that have been submitted via the server. Every minute this will invoke the
cron jobs in batches of 1000 that are ready to be invoked.

* [External Dependencies](#external-dependencies)
* [Configuring the Scheduler](#configuring-the-scheduler)
* [Running the Scheduler](#running-the-scheduler)
* [Configuring the Scheduler Daemon](#configuring-the-scheduler-daemon)

</div>
</div>
</div>

<div class="doc-section" markdown>

## External Dependencies

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Detailed below are the software dependencies that the scheduler needs in order
to start and run,

</div>

| DEPENDENCY  | REASON                                |
|-------------|---------------------------------------|
| PostgreSQL  | Primary data store for the scheduler. |
| Redis       | Data store used as the build queue.   |

</div>
</div>

<div class="doc-section" markdown>

## Configuring the Scheduler

<div class="doc-content panel" markdown>

{{ table("Scheduler parameters", "tables/admin/scheduler-config") }}

</div>

{{ code_snippet("EXAMPLE", "examples/conf/scheduler", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Running the Scheduler

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

To run the scheduler simply invoke the `djinn-scheduler` binary. There is only
one flag that can be given to the `djinn-scheduler` binary.

* `-config` - This specifies the configuration file to use, by default this
will be `djinn-scheduler.conf`.

</div>
</div>
</div>

<div class="doc-section" markdown>

## Configuring the Scheduler Daemon

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The `dist` directory contains files for running the Djinn Scheduler as a daemon
on Linux systems that use systemd and SysVinit for daemon management. Use
whichever suits your needs, and modify accordingly.

If deploying to a Linux system that uses systemd, then be sure to run
`systemctl daemon-reload` upon placement of the service file.

</div>
</div>
</div>
