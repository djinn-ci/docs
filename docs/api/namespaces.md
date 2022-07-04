<div class="doc-section" markdown>

# Namespaces

<div class="doc-content" markdown>
<div class="panel" markdown>

{{ table("Namespace entity", "tables/api/namespaces/namespace-entity") }}

</div>
<div class="panel" markdown>

{{ table("Webhook entity", "tables/api/namespaces/webhook-entity") }}

</div>
<div class="panel" markdown>

{{ table("Collaborator entity", "tables/api/namespaces/collaborator-entity") }}

</div>
</div>
{{ code_toc("ENTITIES", [
		"Namespace entity",
		"Webhook entity",
		"Collaborator entity",
	], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/namespaces", "list-namespaces"),
		("POST", "/namespaces", "create-namespace"),
		("GET", "/n/:username/:path", "get-namespace"),
		("GET", "/n/:username/:path/-/badge.svg", "get-namespace-badge"),
		("GET", "/n/:username/:path/-/builds", "get-namespace-builds"),
		("GET", "/n/:username/:path/-/namespaces", "get-namespace-children"),
		("GET", "/n/:username/:path/-/images", "get-namespace-images"),
		("GET", "/n/:username/:path/-/objects", "get-namespace-objects"),
		("GET", "/n/:username/:path/-/variables", "get-namespace-variables"),
		("GET", "/n/:username/:path/-/keys", "get-namespace-keys"),
		("GET", "/n/:username/:path/-/invites", "get-namespace-invites"),
		("GET", "/n/:username/:path/-/collaborators", "get-namespace-collaborators"),
		("GET", "/n/:username/:path/-/webhooks", "get-namespace-webhooks"),
		("POST", "/n/:username/:path/-/webhooks", "create-namespace-webhook"),
		("PATCH", "/n/:username/:path/-/webhooks/:id", "update-namespace-webhook"),
		("DELETE", "/n/:username/:path/-/webhooks/:id", "delete-namespace-webhook"),
		("PATCH", "/n/:username/:path", "update-namespace"),
		("DELETE", "/n/:username/:path", "delete-namespace"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## List namespaces

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [namespaces](#namespace-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `namespace:read` permission for the
user.
</div>

{{ table("Parameters", "tables/api/namespaces/list-namespaces", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [namespaces](#namespace-entity). The list will be
paginated to 25 namespaces per page, and will be ordered lexically. If the
namespaces were paginated, then the pagination information will be in the
response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/namespaces?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/namespaces?page=3>; rel="next"

</div>

{{ code_snippet("GET /namespaces", "examples/curl/list-namespaces", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create namespace

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create a new [namespace](#namespace-entity) for the currently
authenticated [user](/api/user#user-entity). This requires the
`namespace:write` permission.
</div>

{{ table("Parameters", "tables/api/namespaces/create-namespace", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [namespace](#namespace-entity). It returns an
[error](/api#errors) if any of the parameters are invalid, or if an internal
error occurs.
</div>

</div>

{{ code_snippet("POST /namespaces", "examples/curl/create-namespace", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [namespace](#namespace-entity) by the given `:username`, with
the given `:path`. This requires the `namespace:read` permission.

### Returns

This will return the [namespace](#namespace-entity).
</div>
</div>

{{ code_snippet("GET /n/:username/:path", "examples/curl/get-namespace", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace badge

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the badge of the [namespace](#namespace-entity) by the given
`:username`, with the given `:path`. The badge will display the status of the
most recently submitted build. This does not require any permission, instead
the namespace visibility applies.

### Returns

This will return one of the following SVG badges.

</div>

{{ table("Badges", "tables/api/namespaces/badges", id=False) }}

</div>

{{ code_snippet("GET /n/:username/:path/-/badge.svg", "examples/curl/get-namespace-badge", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace builds

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [builds](/api/builds#build-entity) for the given
[namespace](#namespace-entity). The following parameters can be given as query
parameters to the URL. This requires the `namespace:read` permission for the
user.
</div>

{{ table("Parameters", "tables/api/builds/list-builds", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [builds](/api/builds#build-entity). The list will be
paginated to 25 builds per page, and will be ordered by the most recently
submitted builds first. If the builds were paginated, then the pagination
information will be in the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/builds?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/builds?page=3>; rel="next"

</div>

{{ code_snippet("GET /n/:username/:path/-/images", "examples/curl/get-namespace-builds", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace children

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the child [namespaces](#namespace-entity) in the given namespace.
This requires the `namespace:read` permission.

</div>

{{ table("Parameters", "tables/api/namespaces/list-namespaces") }}

<div class="panel-body" markdown>
### Returns

This will return a list of [namespaces](#namespace-entity). The list will be
paginated to 25 namespaces per page, and will be ordered lexically. If the
namespaces were paginated, then the pagination information will be in the
response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/namespaces?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/namespaces?page=3>; rel="next"

</div>

{{ code_snippet("GET /n/:username/:path/-/namespaces", "examples/curl/get-namespace-children", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace images

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [images](/api/images#image-entity) for the given
[namespace](#namespace-entity). The following parameters can be given as query
parameters to the URL. This requires the `namespace:read` permission for the
user.
</div>

{{ table("Parameters", "tables/api/images/list-images", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [images](/api/images#image-entity). The list will be
paginated to 25 images per page, and will be ordered by the most recently
created images first. If the images were paginated, then the pagination
information will be in the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/images?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/images?page=3>; rel="next"

</div>

{{ code_snippet("GET /n/:username/:path/-/images", "examples/curl/get-namespace-images", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace objects

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [objects](/api/objects#object-entity) for the given
[namespace](#namespace-entity). The following parameters can be given as query
parameters to the URL. This requires the `namespace:read` permission for the
user.
</div>

{{ table("Parameters", "tables/api/objects/list-objects", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [objects](#object-entity). The list will be paginated
to 25 objects per page, and will be ordered lexically. If the objects were
paginated, then the pagination information will be in the response header
`Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/objects?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/objects?page=3>; rel="next"

</div>

{{ code_snippet("GET /n/:username/:path/-/objects", "examples/curl/get-namespace-objects", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace variables

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [variables](/api/variables#variable-entity) for the given
[namespace](#namespace-entity). The following parameters can be given as query
parameters to the URL. This requires the `namespace:read` permission for the
user.
</div>

{{ table("Parameters", "tables/api/variables/list-variables", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [variable](#variable-entity). The list will be
paginated to 25 variables per page, and will be ordered lexically. If the crons
were paginated, then the pagination information will be in the response header
`Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/variables?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/variables?page=3>; rel="next"

</div>

{{ code_snippet("GET /n/:username/:path/-/variables", "examples/curl/get-namespace-variables", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace keys

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [keys](/api/keys#key-entity) for the given
[namespace](#namespace-entity). The following parameters can be given as query
parameters to the URL. This requires the `namespace:read` permission for the
user.
</div>

{{ table("Parameters", "tables/api/keys/list-keys", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [keys](#key-entity). The list will be paginated to
25 keys per page, and will be ordered lexically. If the crons were paginated,
then the pagination information will be in the response header `Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/keys?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/n/me/djinn/-/keys?page=3>; rel="next"

</div>

{{ code_snippet("GET /n/:username/:path/-/keys", "examples/curl/get-namespace-keys", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace invites

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [invites](/api/invites#invite-entity) for the given
[namespace](#namespace-entity). This requires the `namespace:read` permission
for the user.

### Returns

This will return a list of [invites](#invite-entity).
</div>
</div>

{{ code_snippet("GET /n/:username/:path/-/invites", "examples/curl/get-namespace-invites", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace collaborators

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [collaborators](#collaborator-entity) for the given
[namespace](#namespace-entity). This requires the `namespace:read` permission
for the user.

### Returns

This will return a list of [collaborators](#collaborator-entity).
</div>
</div>

{{ code_snippet("GET /n/:username/:path/-/collaborators", "examples/curl/get-namespace-collaborators", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get namespace webhooks

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [webhooks](#webhook-entity) for the given
[namespace](#namespace-entity). This requires the `namespace:read` permission
for the user.

### Returns

This will return a list of [webhooks](#webhook-entity).
</div>
</div>

{{ code_snippet("GET /n/:username/:path/-/webhooks", "examples/curl/get-namespace-webhooks", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create namespace webhook

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create a [webhook](#webhook-entity) for the given
[namespace](#namespace-entity). This requires the `namespace:write` permission
for the user.
</div>

{{ table("Parameters", "tables/api/namespaces/create-webhook", id=False) }}

<div class="panel-body" markdown>

### Returns

Returns the created [webhook](#webhook-entity). It returns an
[error](/api#errors) if any of the parameters are invalid, or if an internal
error occurs.
</div>
</div>

{{ code_snippet("POST /n/:username/:path/-/webhooks", "examples/curl/create-namespace-webhook", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Update namespace webhook

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will update the [webhook](#webhook-entity) by the given `:id`, for the
given [namespace](#namespace-entity). This requires the `namespace:write`
permission.
</div>

{{ table("Parameters", "tables/api/namespaces/create-webhook", id=False) }}

<div class="panel-body" markdown>

### Returns

Returns the created [webhook](#webhook-entity). It returns an
[error](/api#errors) if any of the parameters are invalid, or if an internal
error occurs.
</div>
</div>

{{ code_snippet("PATCH /n/:username/:path/-/webhooks/:id", "examples/curl/update-namespace-webhook", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete namespace webhook

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the [webhook](#webhook-entity) by the given `:id`, for the
given [namespace](#namespace-entity). This requires the `namespace:delete`
permission.

### Returns

This returns no content in the response body.
</div>
</div>

{{ code_snippet("DELETE /n/:username/:path/-/webhooks/:id", "examples/curl/delete-namespace-webhook", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Update namespace

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will update the given [namespace](#namespace-entity). This requires the
`namespace:write` permission.
</div>

{{ table("Parameters", "tables/api/namespaces/update-namespace", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the updated [namespace](#namespace-entity).
</div>

</div>

{{ code_snippet("PATCH /n/:username/:path", "examples/curl/update-namespace", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete namespace

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the given [namespace](#namespace-entity). This requires the
`namespace:delete` permission.
### Returns

This returns no content in the response body.
</div>

</div>

{{ code_snippet("DELETE /n/:username/:path", "examples/curl/delete-namespace", class="doc-content") }}

</div>
