<div class="doc-section" markdown>

# Builds

<div class="doc-content" markdown>
<div class="panel" markdown>

{{ table("Build entity", "tables/api/builds/build-entity") }}

</div>
<div class="panel" markdown>

{{ table("Trigger entity", "tables/api/builds/trigger-entity") }}

</div>
<div class="panel" markdown>

{{ table("Job entity", "tables/api/builds/job-entity") }}

</div>
<div class="panel" markdown>

{{ table("Build object entity", "tables/api/builds/build-object-entity") }}

</div>
<div class="panel" markdown>

{{ table("Build variable entity", "tables/api/builds/build-variable-entity") }}

</div>
<div class="panel" markdown>

{{ table("Artifact entity", "tables/api/builds/artifact-entity") }}

</div>
<div class="panel" markdown>

{{ table("Tag entity", "tables/api/builds/tag-entity") }}

</div>
</div>

{{ code_toc("ENTITIES", [
		"Build entity",
		"Trigger entity",
		"Job entity",
		"Build object entity",
		"Build variable entity",
		"Artifact entity",
		"Tag entity",
	], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/builds", "list-builds"),
		("POST", "/builds", "create-build"),
		("GET", "/b/:user/:number", "get-build"),
		("GET", "/b/:user/:number/objects", "get-build-objects"),
		("GET", "/b/:user/:number/variables", "get-build-variables"),
		("GET", "/b/:user/:number/jobs", "get-build-jobs"),
		("GET", "/b/:user/:number/jobs/:name", "get-build-job"),
		("GET", "/b/:user/:number/artifacts", "get-build-artifacts"),
		("GET", "/b/:user/:number/artifacts/:name", "get-build-artifact"),
		("GET", "/b/:user/:number/tags", "get-build-tags"),
		("POST", "/b/:user/:number/tags", "create-build-tag"),
		("DELETE", "/b/:user/:number/tags/:name", "delete-build-tag"),
		("PATCH", "/b/:user/:number/pin", "pin-build"),
		("PATCH", "/b/:user/:number/unpin", "unpin-build"),
		("DELETE", "/b/:user/:number", "kill-build"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## List builds

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [builds](#build-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `build:read` permission.
</div>

{{ table("Parameters", "tables/api/builds/list-builds", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [builds](#build-entity). The list will be paginated
to 25 builds per page, and will be ordered by the most recently submitted builds
first. If the builds were paginated, then the pagination information will be in
the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/builds?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/builds?page=3>; rel="next"

</div>

{{ code_snippet("GET /builds", "examples/curl/list-builds", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create build

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will submit a new [build](#build-entity) to the server for the currently
authenticated [user](/api/user#user-entity). This requires the `build:write`
permission.
</div>

{{ table("Parameters", "tables/api/builds/create-build", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [build](#build-entity). It returns an [error](/api#errors)
if any of the parameters are invalid, or if an internal error occurs.
</div>

</div>

{{ code_snippet("POST /builds", "examples/curl/create-build", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [build](#build-entity) by the given `:user`, with the given
`:number`. This requires the `build:read` permission.

### Returns

This will return the [build](#build-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number", "examples/curl/get-build", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build objects

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [objects](#build-object-entity) on the given build. This
requires the `build:read` permission.

### Returns

This will return list of [build objects](#build-object-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/objects", "examples/curl/get-build-objects", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build variables

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [variables](#build-variable-entity) on the given build. This
requires the `build:read` permission.

### Returns

This will return a list of [variables](#build-variable-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/variables", "examples/curl/get-build-variables", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build jobs

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [jobs](#job-entity) on the given build. This requires the
`build:read` permission.

### Returns

This will return a list of [job](#job-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/jobs", "examples/curl/get-build-jobs", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build job

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [job](#job-entity) by the given `:name`, on the given build.
This requires the `build:read` permission.

### Returns

This will return the [job](#job-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/jobs", "examples/curl/get-build-jobs", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build artifacts

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [artifacts](#artifact-entity) on the given build. This
requires the `build:read` permission.

### Returns

This will return a list of [artifacts](#artifact-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/artifacts", "examples/curl/get-build-artifacts", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build artifact

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [artifact](#artifact-entity) by the given `:name`, on the
given build. This requires the `build:read` permission.

### Returns

This will return [artifact](#artifact-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/artifacts/:name", "examples/curl/get-build-artifact", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get build tags

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [tags](#tag-entity) on the given build. This requires the
`build:read` permission.

### Returns

This will return a list of [tags](#tag-entity).
</div>
</div>

{{ code_snippet("GET /b/:user/:number/tags", "examples/curl/get-build-tags", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create build tag

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will add a tag to the given build. This requires the `build:write`
permission.

</div>

{{ table("Parameters", "tables/api/builds/create-build-tag", id=False) }}

<div class="panel-body" markdown>

### Returns

Returns a list of created [tags](#tag-entity). It returns an
[error](/api#errors) if an internal error occurs.
</div>
</div>

{{ code_snippet("POST /b/:user/:number/tags", "examples/curl/create-build-tag", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete build tag

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will remove the [tag](#tag-entity) by the given `:name`, from the given
build. This requires the `build:delete` permission.

### Returns

This returns no content in the response body.
</div>
</div>

{{ code_snippet("POST /b/:user/:number/tags/:name", "examples/curl/delete-build-tag", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Pin build

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will pin the given build. This requires the `build:write` permission.

### Returns

This returns the [build](#build-entity).
</div>
</div>

{{ code_snippet("PATCH /b/:user/:number/pin", "examples/curl/pin-build", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Unpin build

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will unpin the given build. This requires the `build:write` permission.

### Returns

This returns the [build](#build-entity).

</div>
</div>

{{ code_snippet("PATCH /b/:user/:number/unpin", "examples/curl/unpin-build", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Kill build

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will kill a [build](#build-entity) that is running. This requires the
`build:delete` permission.

### Returns

This returns no content in the response body.
</div>
</div>

{{ code_snippet("DELETE /b/:user/:number", "examples/curl/kill-build", class="doc-content") }}

</div>
