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
