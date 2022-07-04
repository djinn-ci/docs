<div class="doc-section" markdown>

# Images

<div class="doc-content panel" markdown>{{ table("Image entity", "tables/api/images/image-entity") }}</div>

{{ code_toc("ENTITIES", ["Image entity"], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/images", "list-images"),
		("POST", "/images", "create-image"),
		("GET", "/images/:id", "get-image"),
		("DELETE", "/images/:id", "delete-image"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## List images

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [images](#image-entity) for the currently authenticated
[user](/api/user#user-entity). The following parameters can be given as query
parameters to the URL. This requires the `image:read` permission.
</div>

{{ table("Parameters", "tables/api/images/list-images", id=False) }}

<div class="panel-body" markdown>
### Returns

This will return a list of [images](#image-entity). The list will be paginated
to 25 images per page, and will be ordered lexically. If the images were
paginated, then the pagination information will be in the response header
`Link`.
</div>

    Link: <{{ env.DJINN_API_SERVER }}/images?page=1>; rel="prev",
          <{{ env.DJINN_API_SERVER }}/images?page=3>; rel="next"

</div>

{{ code_snippet("GET /images", "examples/curl/list-images", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create image

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create an [image](#image-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `image:write`
permission.

Images can be created in two ways, either via a direct upload, or via a
download. If the image is being created via an upload, then the contents of the
image should be sent in the request body, and the parameters set as URL query
parameters. If the image is being created via a download, then a regular JSON
payload can be sent, specifying the download URL.
</div>

{{ table("Parameters", "tables/api/images/create-image", id=False) }}

<div class="panel-body" markdown>
### Returns

Returns the created [image](#image-entity). It returns an [error](/api#errors)
if any of the parameters are invalid, or if an internal error occurs.
</div>
</div>

{{ code_snippet("POST /images", "examples/curl/create-image", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get image

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will get the [image](#image-entity) by the given `:id`. This requires the
`image:read` permission.

If the `Accept` header is set to `application/x-qemu-disk`, then the response
body will be the contents of the image file.

### Returns

This will return the [image](#image-entity).
</div>
</div>

{{ code_snippet("GET /images/:id", "examples/curl/get-image", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Delete image

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will delete the [image](#image-entity) by the given `:id`. This requires
the `image:delete` permission.

### Returns

This returns no content in the response body.
</div>
</div>

{{ code_snippet("DELETE /images/:id", "examples/curl/delete-image", class="doc-content") }}

</div>
