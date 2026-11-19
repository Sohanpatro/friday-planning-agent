<p align="center"><img src="assets/banner.svg" alt="Friday — AI planning agent for Claude" width="100%"></p>

# Friday — AI Daily & Weekly Planning Agent for Claude (Agent Skills)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Agent Skills](https://img.shields.io/badge/Claude-Agent%20Skills-DA7857?logo=anthropic)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
[![Works with Google Calendar](https://img.shields.io/badge/Google%20Calendar-supported-4285F4?logo=googlecalendar&logoColor=white)](#getting-started)
[![Works with Asana](https://img.shields.io/badge/Asana-supported-F06A6A?logo=asana&logoColor=white)](#getting-started)
[![GitHub stars](https://img.shields.io/github/stars/Sohanpatro/friday-planning-agent?style=social)](https://github.com/Sohanpatro/friday-planning-agent/stargazers)

> An open-source **AI planning assistant** that matches your **time demand** (tasks, goals, an upstream agent's study blocks) with your **time supply** (your calendar). A human-in-the-loop **productivity agent** built on Claude Agent Skills, working with Google Calendar, Google Sheets and Asana.

## Why

Most people's plans are fine. Their days just don't follow them. We keep appointments with other people and skip the ones with ourselves. A quick phone check turns into hours. A late night causes an afternoon crash.

Friday hangs each day on **four gates**, each one an appointment with someone else. Every night, at the close, it plans tomorrow **with** you: you see the clashes and the options, and you make every call. If you fall off during the day, you don't rebuild the day. You rejoin at the next gate.

## How it works

### Every day: four gates and a nightly close

<p align="center"><img src="assets/daily-loop.svg" alt="A day on four gates, with the eight-step nightly close" width="100%"></p>

| You say | Friday runs |
|---|---|
| `close`, `shutdown`, `plan tomorrow` | **Close**: the 20-minute nightly planning session (above) |
| `replan`, `I fell off`, `what now` | **Replan**: one minute; points you to the next gate |
| `where am I` | **Status**: level, streak, the gates left today |
| `weekly` | **Weekly**: direction for the next 14 days (below) |

### Every week: the weekly planning run

<p align="center"><img src="assets/how-it-works.svg" alt="Weekly planning: orient and harvest, how you write, five questions, build the report, you choose" width="100%"></p>

The weekly run uses the bundled `one-shot-weekly-planning` skill. Then Friday adds its own steps: it scores the week from your log, confirms your level, and writes next week's standard blocks to a dedicated Friday calendar.

### What you get

<p align="center"><img src="assets/sample-plan-card.svg" alt="Sample weekly Plan Card" width="80%"></p>

<sub>A sample weekly Plan Card, with made-up data.</sub>

### Design principles

- **You list, I decide.** Friday lays out demand, supply and clashes. It never picks a task, a date or a priority for you.
- **Nothing written without approval.** You always see "What approve would write" first, then choose: fix it, approve it, or keep it as advice only.
- **Fresh reads.** Every plan starts from a calendar read made in the same session, never from a summary.
- **A level system, not willpower.** A ladder of levels with streaks unlocks more focus sessions only after you've proven you can deliver the current level.
- **Pre-reasoned clash handling.** A *Day Shapes* table holds the options for each kind of conflict, so a small model can run the system reliably.
- **Writes to its own calendar.** Your main calendar is read-only. Friday writes only to the Friday calendar.
- **Stateless, with memory in your own storage.** The Board (Google Sheet) holds your canon, log, rules and journal.

## Repository layout

```
skills/
├── friday/SKILL.md                  # daily co-pilot: close, replan, status, weekly
└── one-shot-weekly-planning/        # the weekly planning run (Stage 1)
    ├── SKILL.md, prompts/, references/, scripts/check.py
config/
└── friday.config.example.md         # your IDs, calendars, day template (copy → friday.config.md, gitignored)
assets/                              # README visuals
```

## Getting started

**Requirements:** Claude (claude.ai, the desktop app, or Claude Code) with Google Calendar, Google Sheets and Asana connected. Python 3 for `check.py`.

1. Clone the repo: `git clone https://github.com/Sohanpatro/friday-planning-agent.git`
2. Copy `config/friday.config.example.md` to `config/friday.config.md`. Fill in your Board sheet, your calendars and your day template. Create a separate "Friday" Google calendar for Friday to write to.
3. Install both folders under `skills/`. In **Claude Code**, copy them to `~/.claude/skills/`. On **claude.ai**, zip each folder and upload it under Settings → Capabilities → Skills.
4. At 8 PM, say **"Friday, close"**.

## Roadmap

- [x] **Stage 1**: the weekly pre-planning skill
- [x] **Stage 2**: Friday, the daily co-pilot (gates, nightly close, replan, ladder, weekly run)
- [ ] A Board template (Google Sheet) you can copy
- [ ] An integration guide for upstream demand agents (job prep, study plans)
- [ ] Routing-eval results

## Credits

The weekly run is inspired by the **Lifehack Method's Win the Week** ([lifehackmethod.com](https://lifehackmethod.com)).

## Contributing

Issues and PRs are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). If Friday helps you win your week, a ⭐ helps other people find it.

## Author

Built by **Sohan Patro**, a software engineer building agentic AI systems. [LinkedIn](https://www.linkedin.com/in/sohan-patro-14086a130/) · [GitHub](https://github.com/Sohanpatro)

## License

[MIT](LICENSE) for Friday and the repo's original material. See Credits for the weekly method's origin.
