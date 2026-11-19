# Routing eval for one-shot-weekly-planning

Re-run whenever the `description:` changes. Each prompt three times; a single green is not evidence.

## Should fire
- plan my week
- let's win the week
- can you help me plan this week
- weekly planning
- I want to do my Sunday planning
- what happened last week and what should I focus on this week
- set up my week

## Should NOT fire (belongs elsewhere)
- plan my month  (monthly planning)
- plan the quarter  (quarterly planning)
- what's on my calendar today  (a lookup, not planning)
- triage my inbox  (email triage skill)
- clean up my Asana  (task triage skill)
- add a task to Asana  (task tool, single action)
- plan this project  (project planning)

## Results
| date | prompt | fired 3/3? | note |
|---|---|---|---|
