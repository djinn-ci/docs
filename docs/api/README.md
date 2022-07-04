<div class="doc-section" markdown>

# Overview

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Djinn CI provides a REST API through which you can interact with the platform.
The API accepts JSON encoded request bodies, and returns JSON encoded responses.

</div>
</div>
<p></p>
<div class="doc-content code-snippet">
<div class="code-snippet-header"><div class="title">BASE URL</div></div>
<pre>{{ env.DJINN_API_SERVER }}</pre>
</div>
</div>

<div class="doc-section" markdown>

## Resources

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Listed below are the resources exposed via the REST API that can be created,
modified, or deleted.

* [Builds](/api/builds)
* [Cron](/api/cron)
* [Images](/api/images)
* [Invites](/api/invites)
* [Keys](/api/keys)
* [Namespaces](/api/namespaces)
* [Objects](/api/objects)
* [Variables](/api/variables)

</div>
</div>
</div>

<div class="doc-section" markdown>

## Authentication

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Authentication to the API is handled via a bearer token that is sent in the
`Authorization` header on each request. This token can either be generated
by the server itself, or generated as part of the OAuth authorization flow
for an application.

For more details on the OAuth authorization flow see
[Authorizing an OAuth app](/api/oauth#authorizing-an-oauth-app).

The amount of access a user has to the API is dictate by the scopes of the
bearer token. For more information about token scopes see
[Token scopes](/api/oauth#token-scopes).

</div>
</div>
</div>

<div class="doc-section" markdown>

## Errors

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Errors returned from API endpoints will be JSON encoded payloads. Detailed
below are the different types of errors that can occur,

**Validation Errors**

Validation errors occur when incorrect data is POSTed to an API endpoint. A JSON
object will be returned, where each key in the object will be a field name, and
its value will be an array of strings detailing the errors that occurred. For
example assume we were to submit a build without a manifest then we would get
the following error,

</div>

    {
        "manifest": [
            "Build manifest is required",
            "Build manifest, invalid driver specified",
        ]
    }

<div class="panel-body" markdown>

on validation errors, the HTTP status code will be that of `400 Bad Request`.

**Unprocessable Entities**

These errors occur when trying to submit data to a namespace you do not have
permission to work in. These will look like,

</div>

    {
        "message": "..."
    }

<div class="panel-body" markdown>

and will be sent with the `422 Unprocessable Entity` status code.

**Internal Errors**

Should an internal error occur from the side of the API then the below JSON
object will be sent with an appropriate `4xx` or `5xx` HTTP response code,

</div>

    {
        "message": "..."
    }

</div>
</div>
