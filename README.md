# Friday — a weekly pre-planning agent

**Friday** is an agentic planning co-pilot built as a set of [Claude Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview). It reads your calendar and task tool, asks you a few sharp questions about last week, and hands back a plan for the week you can approve, tweak, or keep as advice — in about 30 minutes of your time.

> **Status:** Stage 1 of 2. This release ships the core skill, `one-shot-weekly-planning`. Stage 2 will add the full Friday skill suite (nightly close/shutdown, replanning, Asana ↔ calendar placement, and the Hashira job-prep integration).

## Why

Most planning tools ask you to do the sorting. Friday does the sorting and shows you the picture: the handful of things that matter this week, how much real capacity you have, and what to drop. You make the calls; nothing touches your calendar or tasks until you say **approve**.

## How it works

```
 Step 0  Orient & harvest   →  parallel worker agents pull calendar + tasks, save raw data, return lean indexes
 Step 0b How you write      →  agent internalizes the writing standard
 Step 1  Post-mortem        →  5 questions about last week, one at a time, each built on the last answer
 Step 2  Build the report   →  6-section report; two fresh reviewer agents (critic + fact-checker); scripts/check.py gates every number/date
 Step 3  Choose & write     →  you approve / refine / keep-as-advice; only then are calendar blocks and tasks written
```

### Design principles

- **Human-in-the-loop by default** — exact list of writes shown before approval; anything with attendees is confirmed one at a time.
- **Numbers are computed, never estimated** — dates, weekdays and counts come from a script-generated `facts.md`; `check.py` refuses to assemble a report with an unverified claim.
- **Fresh-context review** — the report is checked by agents that did not write it.
- **Progressive disclosure** — each step's prompt is opened only when that step begins, keeping guidance fresh and context lean.
- **Privacy-first** — never reads email; nothing written to memory unless asked.
- **Learns setup over time** — durable facts (main calendar, week start, protected hours) go into `references/user-canon.md`.

## Repository layout

```
skills/one-shot-weekly-planning/
├── SKILL.md                     # entry point: the job, the steps, the firm rules
├── prompts/                     # one prompt per step (00, 00b, 01, 02, 03)
├── references/
│   ├── writing-standard.md      # how the report reads
│   ├── section-guide.md         # what each of the 6 sections is for
│   ├── layout.md                # page layout
│   ├── harvest-briefs.md        # worker roster and index shapes
│   ├── connector-notes.md       # calendar / task-tool pull recipes
│   ├── user-canon.md            # per-user durable setup (empty template)
│   └── chatgpt.md               # adjustments for non-Claude models
├── scripts/check.py             # fact gate: list → verify → assemble
└── routing-eval.md              # should/shouldn't-fire prompts for the trigger
```

## Getting started

**Requirements:** Claude (claude.ai, Claude desktop, or Claude Code) with a connected calendar (e.g. Google Calendar) and a task tool (e.g. Asana). Python 3 for `scripts/check.py`.

1. Clone the repo:
   ```bash
   git clone https://github.com/Sohanpatro/friday-planning-agent.git
   ```
2. Install the skill:
   - **Claude Code:** copy `skills/one-shot-weekly-planning` into `~/.claude/skills/` (or your project's `.claude/skills/`).
   - **claude.ai / desktop:** zip the `one-shot-weekly-planning` folder and upload it under Settings → Capabilities → Skills.
3. Say **"plan my week"**.

## Roadmap

- [x] **Stage 1** — core weekly pre-planning skill
- [ ] **Stage 2** — full Friday suite: nightly close & tomorrow plan, "I fell off" replanning, Asana/Hashira blocks onto a dedicated Friday calendar, Google Drive plan archive
- [ ] Routing-eval results and sample (anonymized) weekly report

## License

[MIT](LICENSE)
