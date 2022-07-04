<div class="doc-section" markdown>

# Cron

<div class="doc-content panel" markdown>{{ table("Cron entity", "tables/api/cron/cron-entity") }}</div>

{{ code_toc("ENTITIES", ["Cron entity"], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/cron", "list-crons"),
		("POST", "/cron", "create-cron"),
		("GET", "/cron/:id", "get-cron"),
		("GET", "/cron/:id/builds", "get-cron-builds"),
		("PATCH", "/cron/:id", "update-cron"),
		("DELETE", "/cron/:id", "delete-cron"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## List crons

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [cron jobs](#cron-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `cron:read` permission.
</div>

{{ table("Parameters", "tables/api/cron/list-crons", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [cron jobs](#cron-entity). The list will be paginated
to 25 cron jobs per page, and will be ordered by the most recently created cron
jobs first. If the crons were paginated, then the pagination information will be
in the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/cron?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/cron?page=3>; rel="next"

</div>

{{ code_snippet("GET /cron", "examples/curl/list-cron", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create cron

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create a [cron job](#cron-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `cron:write`
permission.
</div>

{{ table("Parameters", "tables/api/cron/create-cron", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [cron job](#cron-entity). It returns an
[error](/api#errors) if any of the parameters are invalid, or if an internal
error occurs.
</div>
</div>

{{ code_snippet("POST /cron", "examples/curl/create-cron", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get cron

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [cron job](#cron-entity) by the given `:id`. This requires the
`cron:read` permission.

### Returns

This will return the [cron job](#cron-entity).
</div>
</div>

{{ code_snippet("GET /cron/:id", "examples/curl/get-cron", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get cron builds

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [builds](/api/builds#build-entity) on the given
[cron job](#cron-entity). The following parameters can be given as query
parameters to the URL. This requires the `cron:read` permission.
</div>

{{ table("Parameters", "tables/api/builds/list-builds") }}

<div class="panel-body" markdown>
### Returns

This will return a list of [builds](/api/builds#build-entity). The list will be
paginated to 25 builds per page, and will be ordered by the most recently
submitted builds first. If the builds were paginated, then the pagination
information will be in the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/cron/:id/builds?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/cron/:id/builds?page=3>; rel="next"

</div>

{{ code_snippet("GET /cron/:id/builds", "examples/curl/get-cron-builds", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Update cron

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will update the given [cron job](#cron-entity). This requies the
`cron:write` permission.

>**Note:** If no parameters are sent in the request body, then nothing happens
to the cron job.
</div>

{{ table("Parameters", "tables/api/cron/create-cron") }}

<div class="panel-body" markdown>
### Returns

This will return the updated [cron job](#cron-entity).
</div>

</div>

{{ code_snippet("PATCH /cron/:id", "examples/curl/update-cron", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete cron

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the [cron job](#cron-entity) by the given `:id`. This requires
the `cron:delete` permission.

### Returns

This returns no content in the response body.
</div>

</div>

{{ code_snippet("DELETE /cron/:id", "examples/curl/delete-cron", class="doc-content") }}

</div>
