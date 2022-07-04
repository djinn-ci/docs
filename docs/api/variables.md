<div class="doc-section" markdown>

# Variables

<div class="doc-content panel" markdown>{{ table("Variable entity", "tables/api/variables/variable-entity") }}</div>

{{ code_toc("ENTITIES", ["Variable entity"], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/variables", "list-variables"),
		("POST", "/variables", "create-variable"),
		("GET", "/variables/:id", "get-variable"),
		("DELETE", "/variables/:id", "delete-variable"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## List variables

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [variables](#variable-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `variable:read` permission.
</div>

{{ table("Parameters", "tables/api/variables/list-variables", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [variable](#variable-entity). The list will be
paginated to 25 variables per page, and will be ordered lexically. If the crons
were paginated, then the pagination information will be in the response header
`Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/variables?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/variables?page=3>; rel="next"

</div>

{{ code_snippet("GET /variables", "examples/curl/list-variables", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create variable

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create a [variable](#variable-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `variable:write`
permission.
</div>

{{ table("Parameters", "tables/api/variables/create-variable", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [variable](#variable-entity). It returns an
[error](/api#errors) if any of the parameters are invalid, or if an internal
error occurs.
</div>
</div>

{{ code_snippet("POST /variables", "examples/curl/create-variable", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get variable

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [variable](#variable-entity) by the given `:id`. This
requires the `variable:read` permission.

### Returns

This will return the [variable](#variable-entity).
</div>
</div>

{{ code_snippet("GET /variables/:id", "examples/curl/get-variable", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete variable

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the [variable](#variable-entity) by the given `:id`. This
requires the `variable:delete` permission.

### Returns

This returns no content in the response body.
</div>

</div>

{{ code_snippet("DELETE /variable/:id", "examples/curl/delete-variable", class="doc-content") }}

</div>
