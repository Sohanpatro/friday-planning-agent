# Friday config (example)

Copy this file to `config/friday.config.md` and fill in your own values.
`friday.config.md` is gitignored, so your IDs and routine never get committed.

## Storage
- Board spreadsheet id: `<GOOGLE_SHEET_ID>`
- Friday calendar id (Friday writes only here): `<FRIDAY_CALENDAR_ID>@group.calendar.google.com`
- Supply calendars (read only):
  - Main: `<you@example.com>`
  - Travel (optional): `<TRAVEL_CALENDAR_ID>@group.calendar.google.com`
- Demand tracker (optional upstream agent): sheet `<SHEET_ID>`, tab `State`
- Handover doc (design reasoning): `<DOC_ID>`

## Tools and time
- Task tool: Asana (workspace: `<WORKSPACE>`)
- Time zone: `America/Los_Angeles`
- Planning week starts: Saturday
- Weekly slot: Fridays 4:35–5:15 PM

## Level 1 day template (example — replace with yours)
| Time | Block |
|---|---|
| 7:00 AM | Wake + morning routine (workout, meditation) |
| 9:15 AM | Launch: get ready, phone away |
| 9:45 AM | **Gate 1** — focus session 1 (50 min body-doubling, e.g. Focusmate) |
| 10:45 AM | Focus session 2 |
| 11:35 AM | Flex |
| 12:30 PM | Meal 1, 10-min urgent check, nap, walk |
| 2:30 PM | **Gate 2** — focus session 3 |
| 3:30 PM | Tasks block (45 min) |
| 7:00 PM | Meal 2, family calls |
| 8:00 PM | **Gate 3** — shutdown / Friday close |
| 8:30 PM | Email and messages |
| 9:00 PM | **Gate 4** — fixed evening commitment |
| 11:30 PM | Lights out |

## Calendar colors and reminders
- Colors: gates and sessions 11, tasks 5, flex 2, pinned copies 9
- Reminders: gates 10 and 1 min, others 5, flex none
