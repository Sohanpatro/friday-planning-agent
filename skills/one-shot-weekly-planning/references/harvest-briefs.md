# Harvest briefs: the vault, the workers, the index

Contents:
1. The principle
2. The vault and the scratchpad
3. The worker roster (launch all in ONE message)
4. What every worker does, in order
5. Index formats
6. Just-in-time detail
7. Quality bar
8. Write workers (Room 7)

## 1. The principle

**The model never reads or retypes the data.** Reading raw calendar or task JSON costs every later turn. Retyping it into a report costs slow, serial output. Measured on a real browser run: a document written by code took milliseconds; the same document typed by the model took over a minute; the whole harvest went from about eight minutes to about one when the model stopped touching the bytes.

So a worker's job is not to read and summarize. It is to **pull, vault, slice with code, count with code, and hand back a lean index** with an id on every line. The brain reads the index. When a decision needs the detail behind one line, it fetches that one item by id. Never front-load detail.

If this environment has no code sandbox, keep the same shape by hand: counts actually counted, one line per item, ids on everything, detail left out until asked for.

## 1b. The fixture rule

If a harvest fixture is attached (a MANIFEST file plus raw calendar and task JSON and context documents), the harvest is already done. Read the manifest first: it fixes "today," the windows, the calendar, the task tool and the documents. Do not launch workers, do not call any connector, do not search any drive. Slice and count the fixture files yourself with code into the same index shapes below, save the indexes, and continue from Step 0 part E. The fixture exists so a test run costs no pulls; treat its contents exactly as you would a worker's return.

## 2. The vault and the scratchpad

One working folder for the session, named for the first day of the week being planned (the same date the report file carries), `weekly-planning-YYYY-MM-DD/`:

```
raw/            every connector result, saved as-is, unwrapped once, never edited
index/          one lean index file per worker (see §5)
scratchpad.md   the brain's file: TOC · Setup · Corrections · Answers · Locked plan · Receipts
```

Large connector results in this kind of environment usually auto-save to a tool-results folder as JSON wrapped in a small envelope. Copy each into `raw/` and unwrap it once with code. From then on, code reads `raw/`; the model reads `index/`.

**Small results do not auto-save, and you never copy one out by hand.** Ask every call for the largest page the connector allows, so more results land as files. When a result still comes back as text in the conversation, do not type it into a file: that is the retyping this whole design exists to avoid, and it has cost workers a third of their time. Write the index rows for those items straight from what you can see, keep each item's id, and move on; detail can be fetched again by id. A retried call can leave stale duplicate files behind, so use the filename the tool's own message names, not the newest-looking one.

If files can't be written here, keep `index/` content as clearly headed sections in the conversation and keep them lean. The rule about not retyping data still holds: build the index with code and paste the result, don't compose it.

## 3. The worker roster (launch all in ONE message)

Seven workers is the usual ceiling. Use every one. **Spawn every worker with the model named `sonnet`; never leave the model out.** Each brief carries: the person's name and timezone, the confirmed calendar names or task tool, the exact slice, the pull recipe in `references/connector-notes.md`, and the index format in §5. Name buckets and tools loosely so the worker finds the equivalent in whatever tool this is.

| # | Worker | Slice | Index file |
|---|---|---|---|
| 1 | Calendar, past week | today minus 7 through yesterday | `index/cal-past.md` |
| 2 | Calendar, this week | today through today plus 7 | `index/cal-this.md` |
| 3 | Calendar, week after | today plus 8 through today plus 14. Fourteen, not seven. | `index/cal-next.md` |
| 4 | Tasks, live | every open task: overdue, due in the next 14 days, no due date; plus any pasted or attached task list in `raw/tasks-*` (kept to open and done-in-7-days rows with code, labelled by workspace) | `index/tasks-live.md` |
| 5 | Tasks, hidden and done | every bucket where tasks hide (uncategorized, inbox, "to be sorted", no project, no section), tasks completed in the last 7 days, stale candidates | `index/tasks-hidden.md` |
| 6 | Context documents | Life Map and any basic-facts document | `index/context.md` |
| 7 | Prior plan | last week's locked plan or any current monthly or quarterly plan. If none exists, take half of worker 4's projects instead. | `index/prior-plan.md` |

More workers allowed: split calendars by layer, tasks by project. Fewer: merge 2 and 3 first, then 6 and 7. Never one after another. Every worker has a budget of about ten minutes; a worker that can't finish in that time returns what it has with the tail summarized by project, and says so.

## 4. What every worker does, in order

One script per stage. Every sandbox round trip costs seconds, so batch the work: pull, vault, slice, count, write the index, in as few runs as possible. Two or three runs for the whole job is normal.

1. **Pull** using the recipe for this connector (`references/connector-notes.md`). Pull everything the bulk call offers. Don't leave fields out to save tokens; the index does the saving.
2. **Vault** the raw result to `raw/` as-is. Unwrap the envelope once.
3. **Slice** the window with code, not by reading events. Parse defensively: missing start times, all-day dates, empty due fields, odd recurrence. A crash-and-retry is the most common way a worker loses a minute.
4. **Count** with code: events per day, hours booked, free working hours, open, overdue, by project. Numbers are computed, never estimated. **Booked hours are the union of the day's intervals, not the sum:** two overlapping holds from 9 to 11 are two hours, not four. All-day events are listed separately and never counted as hours. Overlaps go in the conflicts flag. A day that reads as 20 booked hours is a counting error, not a fact.
5. **Write the index** by iterating over the data in code. The worker writes the script; the script writes the file. Never type the rows.
6. **Return** a short note to the brain: the index path, the counts block, and anything odd. Under twenty lines.

## 5. Index formats

These are a shape, not a form. If you can produce something leaner that still has every item, an id on every line, and counted numbers, do that. Headings are only so the brain can find things.

**Calendar index** (workers 1 to 3, one file each):

```
# Calendar index: <past week | this week | week after>
Source: <connection, calendars read> · Window: <exact dates> · Timezone: <tz> · Events: <n>

## Counts
Hours booked: <n> · By day: <Mon n, Tue n, …> · Free working hours by day (9–5 or the observed pattern): <…> · The same, with likely holds counted as open: <…>

## By day
<date, weekday> · <n events, n h>
- <start–end> · <title> · <calendar> · <free | busy, as the event itself is marked> · <attendees: n or names> · id:<event id>
… every day in the window, empty days marked "nothing booked"

## Flags (computed where possible, judged where not)
- Recurring: <title, cadence>
- Fixed or multi-day (travel, launches, deadlines): <…>
- Likely open time dressed as claimed (computed): every block marked free; every block titled like a hold, a block, focus, deep work, buffer, admin, tentative or a placeholder; no attendees and no description; a long block with real meetings inside it. One line each with its hours.
- Duplicates and mirrors (the same event on two calendars, or the same appointment entered twice): listed once, counted once
- Debris (dead recurring, cancelled but still showing): <…>
- Conflicts and double-bookings: <…>
- Odd or uncertain: <…>
```

Descriptions stay in the vault. If a description matters (a delivery, a talk, a prep note), the flag line says so and the id fetches it.

**Task index** (worker 4 live, worker 5 hidden and done):

```
# Task index: <live | hidden and done>
Source: <tool> · Read at: <timestamp> · Tasks: <n>

## Counts
(live)   Open: <n> · Overdue: <n> · Due next 7: <n> · Due 8–14: <n> · No due date: <n> · By project: <…>
(hidden) Hidden buckets: <bucket: n, …> · Completed last 7 days: <n> (and when: if most completions fall inside one short window, say so; that is a cleanup pass, not a week of work) · Stale candidates: <n>

## Rows  (one line per task, oldest overdue first)
- <title> · due <date or "none"> · <project or bucket> · [overdue N d | this-week | next-week | no-date | done <date> | stale?] · id:<native id>
…

## Flags
- Stale candidates and why (due 90+ days ago, references a past event, duplicate of a completed one): <…>
- Projects with many open and no movement: <…>
- Odd or uncertain: <…>
```

Notes stay in the vault; the id fetches them. Comments are not pulled at all in the harvest (see connector notes); they are fetched for a single task only when its status is contested.

**Context index** (worker 6): short, judged, not counted. Who this is in five lines; the altitudes (year, quarter, month, any stated weekly rhythm or protected time); active projects named in the docs; stated priorities in their own words; anything that contradicts the calendar or tasks.

**Prior-plan index** (worker 7): what last week was supposed to be (the Win, aims, planned blocks); what the month or quarter says this week is for; anything now clearly out of date.

## 6. Just-in-time detail

The brain works from the indexes. When a question, a correction, or a triage call needs the detail behind one line, fetch that one item by id from the vault or the connector: an event's description, a task's notes, a task's comments. One item, not a re-pull. Write what you learned beside the line in the scratchpad so it isn't fetched twice.

## 7. Quality bar

Before trusting an index, the brain checks:

- The counts block is present and the by-day or by-project lines add up to it.
- Every row has an id.
- Nothing invented: an unreachable source says so in the index rather than filling in.
- Odd items are listed, not smoothed over.

If an index is thin or something is missing, say what and get it fixed. If that doesn't work, do that one pull yourself the same way: vault, code, index.

## 8. Write workers (Room 7)

Only after the person says approve. Same rule as the harvest: launch every writer in one message, split by day or by project so none is idle.

- **Calendar writers:** create the approved blocks on the main calendar. Every event that has attendees is its own confirmation with the person before it is written; never batch those. Return a receipt per event: title, start, end, id, or the error.
- **Task writers:** add the tags on the approved list, nothing else. Closing, moving or creating a task happens only if the person asked for that exact change in so many words, and then it was on the approve list by name. Tasks from a pasted or attached list are never written to; there is no connection to write with. Return a receipt per action with the native id, or the error.

The brain reads the receipts, spot-checks a few against the plan, and reports exactly what was written and what failed. A partial failure is reported as partial. Nothing is reported as done without a receipt.
