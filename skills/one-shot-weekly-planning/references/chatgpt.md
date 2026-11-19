# If you are not Claude

This skill was written for Claude. Everything in it holds for you too, except the lines below. Where a line here and a line elsewhere disagree, this one wins, for you only.

- **Models.** You run on the largest model the person has (for ChatGPT, GPT-6 Astra) on its lightest thinking level (Light). Every helper you spawn runs on the middle model (for ChatGPT, GPT-6 Sol), never the smallest: the critic is where the report's quality is decided. If you cannot choose a helper's model, use the default and go on.
- **"`sonnet`" means your helper.** Wherever the skill says spawn a helper with the model `sonnet`, spawn your own subagent with a fresh context and the same brief. The two readers in step 2, a critic and a checker, still run, and the one fix pass still follows. Before and after the fix must differ.
- **Your critic gets two more lines in its brief:** list every sentence built on "not X" or "X, not Y" and give the plain positive version, and name every finding argued in more than one section. Your drafts hedge more than the standard allows; this is where it gets caught.
- **No subagents at all?** Then do each reader's brief yourself as its own step: write the critic's findings to `critic.md` and the checker's verdicts to `check-results.md` before you change a word, then do the fix pass against them. Tell the person in one line that the review was done without a separate reader.
- **Setup is always asked.** Never carry setup, answers or files over from memory or an earlier chat. Send the first message every time.
- **Calendars.** In the first message, offer the one or two calendars the person lives by (their own main calendar, and a partner's or family calendar if one is plainly theirs), and ask if any is missing. Do not list every calendar you can see.
- **Task tags.** If the task connection cannot add tags, say so in the approve list and offer no task changes in their place.
- **The saved plan** goes wherever this environment keeps a chat's files; say where in one line.
