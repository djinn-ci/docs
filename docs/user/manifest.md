<div class="doc-section" markdown>

# Manifest

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

The build manifest is a YAML file that describes how a build should be executed.
Detailed below are the different fields for the manifest, what they do, and if
they are required.

* [Namespace](#namespace)
* [Driver](#driver)
* [Env](#env)
* [Objects](#objects)
* [Sources](#sources)
* [Stages](#stages)
* [Allow Failures](#allow-failures)
* [Jobs](#jobs)
  * [Name](#name)
  * [Stage](#stage)
  * [Commands](#commands)
  * [Artifacts](#artifacts)
* [Example manifest](#example-manifest)

## Namespace

**Required:** No

Specify the [namespace](/user/namespace) to submit the build to. If the given
namespace does not exist then it will be created on the fly, and have the
visibility of it set to `private` by default. You can use the `<path>@<user>`
notation to submit a build to a namespace that you are a collaborator in.

</div>

    # Standalone namespace
    namespace: project

    # Child namespace
    namespace: project/child

    # Namespace with owner
    namespace: project@owner

    # Namespace with owner and child
    namespace: project@owner/child

<div class="panel-body" markdown>

## Driver

**Required:** Yes

Specify the driver to use for the build. All drivers require the `driver.type`
property. Each individual driver may have different requirements for each
subsequent property, more detail about the driver configuration can be found
in the [Drivers](/user/drivers) section of the user docs.

</div>

    # QEMU driver
    driver:
        type: qemu
        image: centos/7

    # Docker driver
    driver:
        type: docker
        image: golang
        workspace: /go

<div class="panel-body" markdown>

## Env

**Required:** No

Specify the environment variables to set during build execution, this expects
a list of strings formatted like so, `<key>=<value>`,

</div>

    env:
    - PGADDR=host=localhost port=5432 dbname=djinn user=djinn password=secret sslmode=disable
    - EDITOR=ed
    - LOCALE=en_GB.UTF-8

<div class="panel-body" markdown>

## Objects

**Required:** No

Specify the objects that you want placed into the build environment during
driver creation. This expects a list of strings, where each item is the name
of the uploaded object. The `=>` notation can be used to specify the full
destination location in the build environment the object should be placed in.

</div>

    objects:
    - data => /var/lib/data
    - keys.jks

<div class="panel-body" markdown>

>**Note:** Build times will increase depending on the number of objects being
placed into an environment and their size.

## Sources

**Required:** No

Specify the list of source code repositories to clone into the build
environment. Any repository URL recognized by `git clone` can be used here,

</div>

    sources:
    - https://github.com/andrewpillar/mdsrv
    - git@github.com:andrewpillar/mgrt.git

<div class="panel-body" markdown>

The destination name of the repository to clone can be set via the `=>`
notation,

</div>

    sources:
    - https://github.com/andrewpillar/mdsrv.git => mdsrv

<div class="panel-body" markdown>

the ref to checkout once cloned can be specified at the end of the URL.

</div>

    sources:
    - https://github.com/andrewpillar/mdsrv.git v1.0.0 => mdsrv

<div class="panel-body" markdown>

The sources in the manifest will be collated into a single job of the build
when the build is submitted. This means if any of the sources fail to clone then
the build itself will fail.

## Stages

**Required:** Yes

Specify the order in which stages should be executed.

</div>

    stages:
    - test
    - build

<div class="panel-body" markdown>

## Allow Failures

**Required:** No

Specify which stages are allowed to fail.

</div>

    allow_failures:
    - test

<div class="panel-body" markdown>

## Jobs

**Required:** Yes

Specify the jobs for the build to run. Each job will be executed in the order
in which it is specified.

</div>

    jobs:
    - stage: build
      commands:
      - go build -o a.out
      artifacts:
      - a.out

<div class="panel-body" markdown>

### Name

The name of the build, if no name is given then the default name will be in the
format of `<stage>.<n>` where `<n>` is the number of that job in the stage, for
example, `test.1`, or `build.1`.

### Stage

The name of the stage the job belongs to. If the given stage name does not exist
then the job will be ignored.

### Commands

The list of commands to run during job execution. Each command should be it's
own separate item. A command can be any string that is valid by the shell that
is interpreting it, this can vary depending on the driver being used.

### Artifacts

The list of files to collect from the build environment upon job completion.
This can use the `=>` notation to specify the name the artifact should be
collected as,

</div>

    artifacts:
    - a.out => program

<div class="panel-body" markdown>

## Example manifest

Below is an example manifest with all of the possible properties it could have
to demonstrate its structure,

</div>

    namespace: djinn
    driver:
      type: qemu
      image: djinn-dev
    sources:
    - https://djinn-ci.com.git => djinn
    env:
    - PGPASSWORD=secret
    - LDFLAGS=-s -w
    stages:
    - setup
    - integration
    - make
    jobs:
    - stage: setup
      commands:
      - psql -U djinn -h localhost -d djinn -f djinn/schema.sql
    - stage: integration
      commands:
      - cd djinn
      - go test -v -tags "integration" ./integration
    - stage: make
      commands:
      - cd djinn
      - ./make.sh
      artifacts:
      - djinn/bin/djinn
      - djinn/bin/djinn-curator
      - djinn/bin/djinn-scheduler
      - djinn/bin/djinn-server
      - djinn/bin/djinn-worker
      - djinn/bin/sum.manif

</div>
</div>
