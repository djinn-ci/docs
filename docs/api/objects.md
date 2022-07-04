<div class="doc-section" markdown>

# Objects

<div class="doc-content panel" markdown>{{ table("Object entity", "tables/api/objects/object-entity") }}</div>

{{ code_toc("ENTITIES", ["Object entity"], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/objects", "list-objects"),
		("POST", "/objects", "create-object"),
		("GET", "/objects/:id", "get-object"),
		("DELETE", "/objects/:id", "delete-object"),
	], class="doc-content") }}
</div>

<div class="doc-section" markdown>

## List objects

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [objects](#object-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `object:read` permission.
</div>

{{ table("Parameters", "tables/api/objects/list-objects", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [objects](#object-entity). The list will be paginated
to 25 objects per page, and will be ordered lexically. If the objects were
paginated, then the pagination information will be in the response header
`Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/objects?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/objects?page=3>; rel="next"

</div>

{{ code_snippet("GET /objects", "examples/curl/list-objects", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create object

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create an [object](#object-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `object:write`
permission.

The contents of the file should be sent in the body of the request. The header
`Content-Type` should be the MIME type of the file being uploaded.
</div>

{{ table("Parameters", "tables/api/objects/create-object", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [object](#object-entity). It returns an [error](/api#errors)
if any of the parameters are invalid, or if an internal error occurs.
</div>
</div>

{{ code_snippet("POST /objects", "examples/curl/create-object", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get object

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [object](#object-entity) by the given `:id`. This requires the
`object:read` permission.

If the `Accept` header is set to the MIME type of the object, then the response
body will be the contents of the object file.

### Returns

This will return the [object](#object-entity).
</div>
</div>

{{ code_snippet("GET /objects/:id", "examples/curl/get-object", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete object

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the [object](#object-entity) by the given `:id`. This requires
the `object:delete` permission.

### Returns

This returns no content in the response body.
</div>
</div>

{{ code_snippet("DELETE /objects/:id", "examples/curl/delete-object", class="doc-content") }}

</div>
