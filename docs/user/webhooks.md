<div class="doc-section" markdown>

# Webhooks

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Webhooks allow you to integrate with Djinn CI based on the events that happen
within Djinn CI. When one of these events is triggered, an HTTP POST request
is sent to the webhook's URL. What happens to these events when received is up
to the server that receives it. It could be used to notify people through
various communication channels, to update an issue tracker, or to kick off
another automated process.

* [Creating a webhook](#creating-a-webhook)
* [Signing webhooks](#signing-webhooks)
* [Event payloads](#event-payloads)

## Creating a webhook

Navigate to the [namespace](/user/namespaces) you want to configure the webhook
for. From the *Webhooks* tab, you will be able to create a new webhook via the
*Create webhook* button. Webhooks can also be created via the
[REST API](/api/namespaces#create-namespace-webhook).

## Signing webhooks

Secrets can be set on a webhook that is used for signing the payload of the
delivered event. Webhooks with secrets will include the signature in the
request headers,

</div>

    X-Djinn-CI-Signature sha256=6a7f769...

<div class="panel-body" markdown>

the secret should be used from your end to compute the hash using an HMAC
digest, then compare that with what's in the header.

</div>
</div>
{{ code_toc("EVENTS", ["build.submitted",
	"build.started",
	"build.finished",
	"build.tagged",
	"build.pinned",
	"build.unpinned",
	"invite.sent",
	"invite.accepted",
	"invite.rejected",
	"namespaces",
	"cron",
	"images",
	"objects",
	"variables",
	"ssh_keys"], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Event payloads

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### build.submitted

This event is emitted whenever a new build is submitted to the webhook's
namespace for running.

### build.started

This is event is emitted when a build begins being run, this shares the same
payload as the `build.submitted` event, only the `started_at` field will not be
null.

### build.finished

This is event is emitted when a build begins being run, this shares the same
payload as the `build.submitted` event, only the `finished_at` field will not be
null.

</div>

{{ table("Payload", "tables/api/builds/build-entity") }}

</div>

{{ code_snippet("build.submitted, build.started, build.finished event", "examples/api/build.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### build.tagged

This event is emitted whenever a new tag is added to a build. This will not be
emitted for tags that are added to a build at the time the build is submitted.

</div>

{{ table("Payload", "tables/webhooks/build.tagged") }}

</div>

{{ code_snippet("build.tagged event", "examples/webhooks/build.tagged.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### invite.sent

This event is emitted when an invite is sent to a user.

</div>

{{ table("Payload", "tables/webhooks/invite.sent") }}

</div>

{{ code_snippet("invite.sent event", "examples/webhooks/invite.sent.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### invite.accepted

This event is emitted when an invite is accepted by a user.

### invite.rejected

This event is emitted when an invite is rejected by a user.

</div>

{{ table("Payload", "tables/webhooks/invite") }}

</div>

{{ code_snippet("invite.accepted, invite.rejected event", "examples/webhooks/invite.accepted.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### namespaces

This event is emitted whenever a namespace is created, updated, or deleted.
Creation events for namespaces will only be emitted for child namespaces.
The `action` field will either be `created`, `updated`, or `deleted`.

</div>

{{ table("Payload", "tables/webhooks/namespaces") }}

</div>

{{ code_snippet("namespaces event", "examples/webhooks/namespaces.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### cron

This event is emitted whenever a cron job is created, updated, or deleted within
a namespace. The `action` field will either be `created`, `updated`, or
`deleted`.

</div>

{{ table("Payload", "tables/webhooks/cron") }}

</div>

{{ code_snippet("cron event", "examples/webhooks/cron.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### images

This event is emitted whenever an image is created, or deleted within a
namespace. The `action` field will either be `created`, `updated`, or
`deleted`.

</div>

{{ table("Payload", "tables/webhooks/images") }}

</div>

{{ code_snippet("images event", "examples/webhooks/images.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### objects

This event is emitted whenever an object is created, or deleted within a
namespace. The `action` field will either be `created`, `updated`, or
`deleted`.

</div>

{{ table("Payload", "tables/webhooks/objects") }}

</div>

{{ code_snippet("objects event", "examples/webhooks/objects.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### variables

This event is emitted whenever a variable is created, or deleted within a
namespace. The `action` field will either be `created`, `updated`, or
`deleted`.

</div>

{{ table("Payload", "tables/webhooks/variables") }}

</div>

{{ code_snippet("variables event", "examples/webhooks/variables.json", class="doc-content") }}

</div>

<div class="doc-section" markdown>
<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

### ssh_keys

This event is emitted whenever an SSH key is created, updated, or deleted
within a namespace. The `action` field will either be `created`, `updated`, or
`deleted`.

</div>

{{ table("Payload", "tables/webhooks/ssh_keys") }}

</div>

{{ code_snippet("ssh_keys event", "examples/webhooks/ssh_keys.json", class="doc-content") }}

</div>
