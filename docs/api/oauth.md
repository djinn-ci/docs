<div class="doc-section" markdown>

# OAuth

</div>

<div class="doc-section" markdown>

## Authorizing an OAuth app

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
When authorizing an OAuth app, a `GET` request must be sent to the
`/login/oauth/authorize` endpoint, with the following parameters.
</div>

    GET {{ env.DJINN_SERVER }}/login/oauth/authorize

{{ table("", "tables/api/oauth-auth-params") }}

<div class="panel-body" markdown>
Once the user has allowed your app access to their Djinn CI account, they will
be redirect to the `redirect_uri` of your app. A temporary `code` will be paseed
in the `redirect_uri`, this will expire after 10 minutes. If a `state` was given
during authentication, then this will be sent back too, and should be checked on
your end. If this state code does not match then you should abort immediately.

Extract the `code` from the `redirect_uri` and exchange it, with the following
parameters,
</div>

    POST {{ env.DJINN_SERVER }}/login/oauth/token

{{ table("", "tables/api/oauth-token-params") }}

<div class="panel-body" markdown>
The parameters sent back to the endpoint should be encoded as a URL string, by
default, the response will be URL encoded like so,
</div>

    access_token=1a2b3c&token_type=bearer&scope=build:read,write

<div class="panel-body" markdown>
a JSON response cab be received by setting the `Accept` header to
`application/json`,
</div>

    {
        "access_token": "1a2b3c",
        "token_type": "bearer",
        "scope": "build:read,write"
    }

</div>
</div>

<div class="doc-section" markdown>

## Token scopes

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
A scope dictates the sort of access you need to the API. A single scope is made
up of a resource, and the permissions for that resource. There are three
permissions that a resource can have,
</div>

| PERMISSION | DESCRIPTION                                |
|------------|--------------------------------------------|
| `read`     | Allow au ser to get a resource.            |
| `write`    | Allow a user to create or edit a resource. |
| `delete`   | Allow a user to delete a resource.         |

<div class="panel-body" markdown>
each individual scope is represented as `<resource>:<permission>,...`, for
example.
</div>

    buid:read,write,delete namespace:read,write

<div class="panel-body" markdown>
The above scope would grant the user the abillity to view, create, and kill
builds, and view, create, and edit namespaces.
</div>
</div>
