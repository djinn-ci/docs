<div class="doc-section" markdown>

# Invites

<div class="doc-content panel" markdown>{{ table("Invite entity", "tables/api/invites/invite-entity") }}</div>

{{ code_toc("ENTITIES", ["Invite entity"], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/invites", "list-invites"),
		("POST", "/n/:username/:path/-/invites", "create-invite"),
		("PATCH", "/invites/:id", "accept-invite"),
		("DELETE", "/invites/:id", "reject-invite"),
	], class="doc-content") }} 

</div>

<div class="doc-section" markdown>

## List invites

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
List the [invites](#invite-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `invite:read` permission for
the user.

### Returns

This will return a list of [invites](#invite-entity).
</div>
</div>

{{ code_snippet("GET /invites", "examples/curl/list-invites", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Create invites

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will create an [invite](#invite-entity) for the currently authenticated
[user](/api/user#user-entity). This requires the `invite:write`
permission.
</div>

{{ table("Parameters", "tables/api/invites/create-invite") }}

<div class="panel-body" markdown>
### Returns

Returns the sent [invite](#invite-entity). It returns an [error](/api#errors)
if any of the parameters are invalid, or if an internal error occurs.
</div>
</div>

{{ code_snippet("POST /n/:username/:path/-/invites", "examples/curl/create-invite", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Accept invite

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will accept the [invite](#invite-entity) by the given `:id`. This requires
the `invite:write` permission.

### Returns

Returns the accepted [invite](#invite-entity), with only the `namespace`,
`inviter`, and `invitee` fields.
</div>
</div>

{{ code_snippet("PATCH /invites/:id", "examples/curl/accept-invite", class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Reject invite

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will reject the [invite](#invite-entity) by the given `:id`. This requires
the `invite:delete` permission. Either the invitee or inviter can
reject the invite.

### Returns

This returns no content in the response body.
</div>
</div>

{{ code_snippet("DELETE /invites/:id", "examples/curl/reject-invite", class="doc-content") }}

</div>
