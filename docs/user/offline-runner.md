<div class="doc-section" markdown>

# Offline Runner

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Djinn CI can be used to run your builds offline without having to submit them to
the build server. This does require having to configure the necessary drivers
on your machine however.

* [Installing the Offline Runner](#installing-the-offline-runner)
* [Configuration Locations](#configuration-locations)
* [Configuring Drivers](#configuring-drivers)
  * [Docker](#docker)
  * [QEMU](#qemu)

## Installing the Offline Runner

To install the offline runner you will first need to build it using Go,

</div>

    $ git clone https://github.com/djinn-ci/djinn

<div class="panel-body" markdown>

once cloned, change into the directory and run the `make.sh` script.

</div>

    $ ./make.sh runner

<div class="panel-body" markdown>

This will produce a binary called `bin/djinn`, simply move this binary into a
location that will make it accessible via your `PATH`.

## Configuration Locations

For the offline runner, driver configuration sits in the `driver.conf` file. By
default this is expected to be in the user config directory. Detailed below is
where the file will be found on the different operating systems,

**Unix**

If non-empty then `$XDG_CONFIG_HOME` is used, and the fullpath would be
`$XDG_CONFIG_HOME/djinn/driver.conf`. Otherwise it will use
`~/.config/djinn/driver.conf`.

**Darwin**

On Darwin the path used will be,
`$HOME/Library/Application Support/djinn/driver.conf`.

**Windows**

On Windows the path used will be, `%AppData%/djinn`.

## Configuring Drivers

>**Note:** The same driver configuration used for the offline runner is used
for the worker too.

Each driver supported by Djinn CI is configured in its own block directive in
the `driver.conf` file like so,

</div>

    driver <name> {
        ...
    }

<div class="panel-body" markdown>

where `<name>` is the name of the driver being configured, followed by a list
of value directives. For example to configure the QEMU driver you would do the
following,

</div>

    driver qemu {
        disks  "/home/me/.config/djinn/images/qemu"
        cpus   1
        memory 2048
    }

<div class="panel-body" markdown>

the above configuration would set the location of the QEMU disk images to use,
the number of CPUs, and the amount of memory for each machine that will be
created.

For a completed example of a `driver.conf` file see the `dist` directory of the
source repository.

### Docker

Detailed below are the value directives used by the Docker driver.

</div>

| NAME      | TYPE     | DESCRIPTION                                                            |
|-----------|----------|------------------------------------------------------------------------|
| `host`    | `string` | The host of the running Docker daemon, can be a path to a Unix socket. |
| `version` | `string` | The versio nof the Docker API to use.                                  |

<div class="panel-body" markdown>

### QEMU

Detailed below are the value directives used by the QEMU driver.

</div>

| NAME      | TYPE     | DESCRIPTION                                          |
|-----------|----------|------------------------------------------------------|
| `disks`   | `string` | Where the QEMU disk images are on the filesystem.    |
| `cpus`    | `int`    | The number of CPUs to use for the QEMU machines.     |
| `memory`  | `int`    | The amount of memory in bytes for the QEMU machines. |

<div class="panel-body" markdown>

The directory specified in `disks` must have a another sub-directory for each
architecture, in each of these exist the disk images to use. For example assume
a manifest declares the following,

</div>

    driver:
      type: qemu
      image: centos/8

<div class="panel-body" markdown>

then the offline runner will look for the following disk image,

</div>

    /home/me/.config/djinn/images/qemu/x86_64/centos/8

</div>
</div>
