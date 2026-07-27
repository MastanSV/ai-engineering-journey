# Tracking & Accountability Rules

> The system that turns brutal accountability into honest data.

## Day-state symbols

| Symbol | Meaning  | Use when                                                    |
| ------ | -------- | ----------------------------------------------------------- |
| ✅     | Shipped  | Task fully done within planned day                          |
| 🔄     | Carried  | Partial; remainder rolls to next day. **MUST log reason.**  |
| ⏭️     | Deferred | Explicit skip. Logged with reason + when (or if) it returns |
| ❌     | Skipped  | Missed entirely, no recovery. Rare. Triggers re-plan.       |

## The slip-logging template

Whenever a task is 🔄 or ⏭️, add this in the day's entry:

## Carryover sizing rule (added 2026-05-03)

When a weekday slips and a task carries:

1. **Estimate the remainder in minutes.** Don't hand-wave.
2. **If ≤ 30 min:** add to the next weekday's plan as the FIRST item with `(carryover, ~Xmin)` tag.
3. **If > 30 min:** do NOT push to the next weekday. Move it straight to Saturday's block in `03-active-tasks.md`.
4. **Why:** prevents single-day cascades from eating 3 weekdays. Weekday slots stay 1.5hr-shaped; weekend absorbs heavier rework.

Source: `weekly-logs/retro-week-01-linreg.md` §5 → `04-decisions-log.md` 2026-05-03.

## Feynman learning checklist (added 2026-05-17)

Before marking any concept "learned":

1. Write a 3-sentence explanation using zero jargon.
2. If you can't, identify the gap and re-study that specific piece.
3. Only then add the Anki card.

Source: `weekly-logs/retro-week-03.md` §9 gap #2.

## Recognition ≠ Explanation rule (added 2026-07-27)

Anki recognition ("I know this card") is NOT mastery. Before flipping ANY card:

1. Say the full answer OUT LOUD, in detail — as if to an interviewer.
2. Only if the spoken answer matches → mark known. Silent "I know it" does not count.
3. If you can recognize but not explain → it's fuzzy → re-study, don't pass.

Source: `weekly-logs/retro-week-06-p1.md` Q2 + Q7 (recognition/recall/explanation gap).

## Anki own-words + LLM-rating loop (added 2026-07-27)

Every new card is authored by ME, not pasted from GPT:

1. Write the answer in my own words first.
2. Ask the LLM to RATE my understanding (not to write the answer).
3. Store the polished, interview-ready version.

Source: `weekly-logs/retro-week-06-p1.md` "What could be improved" #2.

## Break re-entry rule (added 2026-07-27)

Prevents a skipped-days slip from fading into a month-long gap.

1. TRIPWIRE: 2 days missed in a row → next day is a mandatory 15-min
   Anki-only re-entry session. No new material. Just restart the habit.
2. RE-ENTRY RAMP: Day 1 after ANY break = review only (no new notebook).
   Lower the bar to make restarting frictionless.

Source: `weekly-logs/retro-week-06-p1.md` Q1 + Q3 (trip → slow fade → 1-month gap).

## Weekend minimum-viable rule (added 2026-07-27)

Weekends fail for two different reasons — two different fixes:

1. AT HOME (family + energy): minimum = 15-min Anki only. Don't attempt a full block.
2. AT HOSTEL (no fixed slot): pick a FIXED clock time, same as weekdays.

Source: `weekly-logs/retro-week-06-p1.md` Q8 (recurring from retro-week-02 §4 Slip 3).

## Active rules

- **30-min carryover cap:** weekday carryover >30 min → push to Saturday, not next weekday.
- **20-min stuck rule:** stuck >20 min → switch resource. Never close laptop without trying 1 alternative.
- **Feynman learning checklist:** before marking a concept "learned," write a 3-sentence zero-jargon explanation. If you can't → re-study. Only then add the Anki card.
- **Recognition≠Explanation:** say every Anki answer OUT LOUD before flipping. Recognition ≠ known.
- **Anki own-words loop:** author cards in my words → LLM rates → store polished version.
- **Break tripwire:** 2 missed days in a row → mandatory 15-min Anki re-entry next day.
- **Post-break ramp:** Day 1 back = review only, no new notebook.
- **Weekend minimum:** home → 15-min Anki floor; hostel → fixed clock slot.
