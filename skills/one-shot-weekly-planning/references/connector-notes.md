# Connector notes: known pull recipes and quirks

Learned on real runs in the claude.ai browser chat, last verified July 2026. The same services show up differently on different surfaces: in Cowork or Claude Code they may appear as a set of named tools rather than the browser connector described here, with different call names. The recipes below are about *shape*, not call names: find the one bulk call that lists everything with notes, page through it, and vault the result. If a call errors or doesn't exist, adapt and say so rather than retrying the same thing.

## Google Calendar (browser connector)

- Events come back fat and with recurring events already expanded. Good: nothing to reconstruct.
- Do not pass field filters or a single-events flag; they hard-error. Take the whole event and slice with code.
- Paginate with the next-page token, up to 250 per page.
- Pull time is a few seconds per calendar and runs serially, so it scales with the number of calendars, not with the window. Three calendars over three weeks is fine.
- All-day events carry a date, not a date-time. Parse both. Some all-day events carry the date as a full timestamp (`2026-09-21T00:00:00Z`) rather than a plain date; treat a midnight-UTC timestamp on an all-day event as that calendar date, and never let it crash the slice.

## Asana (browser connector)

- Use the bulk my-tasks call, not a search call; the search call does not exist in the browser connector.
- Ask for these fields in one go: name, due date, completed, number of subtasks, created, modified, notes, permalink. **Notes come free in the bulk call.** No per-task loop for notes.
- Two calls cover the harvest: one with "completed since now" for the open set, one for tasks completed in the last 7 days.
- Limit around 100 per page; paginate by offset while a next page exists.
- **Comments are expensive:** about twelve seconds each, one call per task. Never loop them in the harvest. Fetch for one task only when its status is contested.
- Hidden buckets: tasks with no project, no section, or in an inbox or "to be sorted" area. Worker 5 sweeps these explicitly.
- Due-date history (how many times a date moved) is not exposed; "modified" is. Treat "zombie task" as inferred, not measured.

## Other task tools (Todoist, Google Tasks, Microsoft To Do, Things, Notion, and the like)

Same shape: find the one bulk call that lists open tasks with notes, take everything it offers, page through, vault it, and let code do the rest. Look for the tool's equivalent of an inbox or uncategorized area and sweep it.

## Other calendars (Outlook, Apple, and the like)

Same shape: list the calendars, confirm the main one, pull the window per calendar, vault, slice with code. Expect all-day events and recurring expansion to differ; parse defensively.

## Context documents

Read whole, once. They are usually small. Worker 6 distills them; the originals stay available for a re-read.

## Task timestamps are UTC

Asana's `completed_at`, `created_at` and `modified_at` are UTC. Convert them to the person's timezone before you print a time or count by day. Printed raw, a 1:18 PM close reads as "5:18 PM" and an evening close lands on the next day, and both are wrong facts about their own week.
