# Step 0: Orient and harvest

*Not Claude? Your setup rules are in `references/chatgpt.md`: never reuse setup from memory or an earlier chat, and offer the one or two calendars they live by.*

**By the end of this step:** you have read the person's plans yourself, you know which calendar and task tool are real, your workers have written their indexes, you have read those indexes whole, and the working document holds it all. You have said almost nothing yet.

## A. The first message: the approved text, word for word

Before you write a word to the person, do the looking this message needs. Find every calendar connection and list every calendar you can see, by name; pick the main one yourself from the evidence (their name, the most real events). Find any task tool connection and list every workspace or account you can see in it. Get today's date from the system with a command, never from memory, and compute with code the week you'll review and the week you'll plan; the person sets the week boundary, and your best guess is a week that starts on Friday, reviewing the last seven days and planning the next seven. If `references/user-canon.md` has entries from a prior week, use them as the guesses.

Then send the message between the two markers below, without the markers. Everything outside the square brackets is said exactly as written: the words, the bold, the italics, the emoji, the numbering and the line breaks. Fill each bracket, short, and send nothing else in that first message.

⟦MESSAGE STARTS⟧

This is the Lifehack Method's Win the Week, built into your AI. It plans your week with you and for you in about thirty minutes of your time. Learn more at lifehackmethod.com.

*For the best experience, set your model to the **HIGHEST** model you have available (ex: Opus 5.5), on the **LOWEST** thinking level (Low or "Faster") before starting. If you don't, this still works, just much slower.*

## How this goes
1. **You:** A minute of setup — right now
2. **Me:** I work ~7 minutes reading your calendar and tasks ⏸
3. **You:** You answer 5 questions, one at a time
4. **Me:** I work ~8 minutes building your plan ⏸
5. **You** decide what happens next — revise or apply it to your calendar and to-do list

🔒 *Nothing gets changed until you say so.*

## Answer all these questions now
- **Calendars.** [the calendars found, with the main one named] **Any calendar you live by that's missing?**
- **Tasks.** [the task tool and workspace found] **Anywhere else?**
- **Life Map.** 📎 **Attach it now.** I can't promise a good plan without it.
- **Anything else** — context docs, a monthly plan, a quarterly plan. 📎 **Attach now.**
- **Please confirm:** Are we planning the week of **[computed dates]**? Right, or do you want to plan another 7 days?

⟦MESSAGE ENDS⟧

How to fill the brackets:

- **Calendars:** every calendar you found, by name, with the main one marked as main; any you will ignore gets a few words why (a shared, holiday or subscribed calendar). A plan built on one of two calendars is wrong about the week, which is why the bold question after it matters.
- **Tasks:** the tool and the one workspace this connection reads. Asana's connector reads one workspace per connection, chosen when they connected it. Ask the connector who they are (for Asana, `get_me`): if it lists more workspaces than the one you can read, name each of the others and say plainly that you can't see them, then ask them to open My Tasks in each, select all, copy and paste it here (a CSV export of My Tasks attached works too). If a second workspace is likely and you cannot tell, ask. If no task tool is connected, the bracket says so and asks where their tasks live; after they answer, help them connect it in plain steps. No task tool, no plan: say so kindly and stop.
- **Dates:** the planning week's first and last day with weekdays, computed, like "Fri Sep 25 to Thu Oct 1".

**The heading "Answer all these questions now" belongs to this first message only.** Every other time you need something from the person, it sits under its own bold heading, "What I need from you now," with the instruction underneath in plain sentences, never inside a paragraph. That applies to the holds question, every one of the five questions, the pause before the build, and the choice at the end. The lines marked "word for word" in the prompts are said exactly as written; they are the moments the person has to act, and they are too important to paraphrase.

**With a harvest fixture attached** (files with a MANIFEST): send the approved message down to and including the 🔒 line. In place of the "Answer all these questions now" block, write one line confirming what you will treat as today, the calendar, the task tool and the documents, from the manifest; if a packaged answers file is attached, say so in the same line, because you will use it in step 1. Write the setup facts to `references/user-canon.md` from the manifest, with your guess at the days they never work, marked as a guess. Then skip to D.

## B. When they answer

If they answer without attaching a Life Map, say once, plainly, that the plan will lean on the calendar, the tasks and the five questions, and that it will be thinner for it. Then go on. Pull nothing until the week is confirmed.

If they paste a task list or attach a My Tasks CSV for a workspace you cannot reach, save it as is to `raw/tasks-<workspace>.txt` (or `.csv`) and hand it to the live-tasks worker with the rest: open tasks and anything finished in the last seven days, labelled with the workspace it came from. A big export is fine; the worker keeps those rows with code and ignores the history. Their tasks there count as theirs, the same as the connected ones.

Once the setup is confirmed, write it to `references/user-canon.md` now, before the harvest, as a bullet list: the main calendar and the ones to ignore, the task tool and its workspaces, the week's start day, anything they said is always protected. Setup facts only; nothing about how their week went. The days they never work are added after the holds question in F. The report cannot be assembled while this file is empty, and next week's setup reads it instead of asking again.

## C. Orient yourself first

Before any worker launches, read whole: every context document they gave you, any prior weekly plan, any monthly or quarterly plan. If there are none, read the calendar and the task notes for the same things; people write their priorities into event titles and task descriptions. You are looking for what this stretch was supposed to be, the altitudes (year, quarter, month), stated rhythms and protected time, and the one tension in their own documents. Write a five-line orientation into the working document. This reading is why your first words later will be sharp.

## D. Harvest

**With a fixture: no workers, no connectors.** Slice and count the fixture files yourself, with whatever code runner this environment has, into the index shapes in `references/harvest-briefs.md`. If there is no code runner at all, count by hand, carefully, and say so once.

**Without a fixture:** say, word for word: "Go get a coffee. I'll do my work and I'll be back in under ten minutes. Set a timer if you need to." Keep working in the same turn: the person is not going to answer, and stopping here leaves them waiting on nothing. Then, in one message, launch the full roster in `references/harvest-briefs.md`. Every brief carries the exact slice, the exact output path, the format, and the check. Ten minutes is the budget; if something is still out at ten, proceed with what's back and name the gap.


## E. Read the indexes yourself, whole

When the indexes are in, read every one, end to end, in pieces small enough that the output is shown to you and not saved aside. Log a one-line result per worker in the working document's task table. Write your own day-by-day read of last week and of the plan week into the working document, as short notes, from the calendar indexes; a day you have no note for is a day you did not read. Flag any number that looks wrong and recompute it in code before you trust it (a day showing twenty booked hours is a counting error). Note what the task tool shows as open, as a question, not a verdict.

## F. Holds, and free time dressed as claimed time

Before capacity means anything, find out what the blocks really are. With code, over the plan week's calendar index, list every block that is likely open time: marked free rather than busy; titled like a hold, a block, focus, deep work, buffer, admin, tentative or a placeholder; with no attendees and no description; or a long block with real meetings sitting inside it. Compute free working hours two ways, with those blocks closed and with them open, and keep both.

Then ask once, under **What I need from you now**, with your best guess on each line so "yep" is an answer: which of these are really open for planning into, and which are claimed. In the same message, one more line with your guess from the calendar: "It looks like you don't work Wednesdays. Right?" A session booked on a day they never work is a wrong plan, and the calendar cannot tell you which days those are. Add their answer to `references/user-canon.md`. With a packaged answers file there is nobody to ask: take your best guess, write it into the working document as a guess, and say in the report's calendar section that you guessed.

## Close

Show `references/user-canon.md` with `cat` so its contents land in this conversation. Then open `prompts/00b-how-you-write.md`.
