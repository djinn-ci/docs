<div class="doc-section" markdown>

# User

<div class="doc-content panel" markdown>{{ table("User entity", "tables/api/user-entity") }}</div>

{{ code_toc("ENTITIES", [
		"User entity",
	], class="doc-content") }}
{{ code_toc_endpoints("ENDPOINTS", [
		("GET", "/user", "get-user"),
	], class="doc-content") }}

</div>

<div class="doc-section" markdown>

## Get user

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>
This will return the currently authenticated [user](#user-entity).
</div>
</div>

{{ code_snippet("GET /user", "examples/curl/get-user", class="doc-content") }}

</div>
