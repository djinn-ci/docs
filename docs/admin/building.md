<div class="doc-section" markdown>

# Building

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

To build the Djinn CI components you will need to install the following
dependencies,

* `go`- https://golang.org/dl
* `yarn` - https://yarnpkg.com/getting-started/install
* `stringer` - https://github.com/golang/tools
* `qtc` - https://github.com/valyala/quicktemplate#quick-start

make sure each of the programs listed above are installed and in your `$PATH`.

Once the build dependencies are installed clone the repository,

</div>

    $ git clone https://github.com/djinn-ci/djinn

<div class="panel-body" markdown>

once cloned, change into the directory and run the `make.sh` script. This will
execute all of the tests, compile the LESS and templates, then build the
curator, scheduler, server, the worker, and the offline runner.

</div>

    $ ./make.sh

<div class="panel-body" markdown>

The compiled programs will be `bin/djinn`, `bin/djinn-curator`,
`bin/djinn-scheduler`, `bin/djinn-server`, and `bin/djinn-worker`. Each of
these will be a statically linked binary. You can change the target operating
system and architecture via the `GOOS` and `GOARCH` environment variables,
these will be passed through to the underlying `go build` command that is
invoked,

</div>

    $ GOOS=freebsd GOARCH=amd64 ./make.sh

<div class="panel-body" markdown>

the flags of the linker can be configured via the `LDFLAGS` variable. This will
accept any flags that can be normally configured via the `-ldflags` flag that
is passed to the `go build` command,

</div>

    $ LDFLAGS="-s -w" ./make.sh

<div class="panel-body" markdown>

for more information about `-ldflags` see `go tool link -help`

</div>
</div>
</div>
