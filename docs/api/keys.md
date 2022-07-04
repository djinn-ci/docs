<div class="doc-section" markdown>

# Keys

<div class="doc-content panel" markdown>{{ table("Key entity", "tables/api/keys/key-entity") }}</div>

{{ code_toc("ENTITIES", ["Key entity"], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/keys", "list-keys"),
		("POST", "/keys", "create-key"),
		("GET", "/keys/:id", "get-key"),
		("PATCH", "/keys/:id", "update-key"),
		("DELETE", "/keys/:id", "delete-key"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## List keys

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [keys](#key-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `key:read` permission.
</div>

{{ table("Parameters", "tables/api/keys/list-keys", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [keys](#key-entity). The list will be paginated to
25 keys per page, and will be ordered lexically. If the crons were paginated,
then the pagination information will be in the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/keys?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/keys?page=3>; rel="next"

</div>

{{ code_snippet("GET /keys", "examples/curl/list-keys", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create key

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create a [key](#key-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `key:write`
permission.
</div>

{{ table("Parameters", "tables/api/keys/create-key", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [key](#key-entity). It returns an
[error](/api#errors) if any of the parameters are invalid, or if an internal
error occurs.
</div>
</div>

{{ code_snippet("POST /keys", "examples/curl/create-key", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get key

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [key](#key-entity) by the given `:id`. This requires the
`key:read` permission.

### Returns

This will return the [key](#key-entity).
</div>
</div>

{{ code_snippet("GET /keys/:id", "examples/curl/get-key", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Update key

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will update the given [key](#key-entity). This requies the `key:write`
permission.
</div>

{{ table("Parameters", "tables/api/keys/update-key") }}

<div class="panel-body" markdown>
### Returns

This will return the updated [key](#key-entity).
</div>
</div>

{{ code_snippet("PATCH /keys/:id", "examples/curl/update-key", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete key

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the [key](#key-entity) by the given `:id`. This requires
the `key:delete` permission.

### Returns

This returns no content in the response body.
</div>

</div>

{{ code_snippet("DELETE /key/:id", "examples/curl/delete-key", class="doc-content") }}

</div>
