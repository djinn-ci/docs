<div class="doc-section" markdown>

# Cron

<div class="doc-content panel" markdown>
<div class="panel-body" markdown>

Cron jobs allow you to submit build manifests at a scheduled interval. Cron
jobs can either be configured to run `daily`, `weekly`, or `monthly`. When a
cron job is scheduled it will always trigger at the start of it's schedule, so
a `daily` cron job will run at the start of the next day, `weekly` would be the
start of the next week, and `monthly` would be the start of the next month.

Crons can either be standalone, or grouped into a [namespace](/user/namespaces).
Crons are grouped into a namespace by specifying the `namespace` field in the
build manifest you want to use for that cron.

</div>
</div>
</div>
