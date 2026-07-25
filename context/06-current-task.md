### Sat Jul 25 (6hr) — Ship P1 + build interview narrative

> **End goal:** By EOD I can walk an interviewer through this project in 3 min,
> defend every metric/threshold/model choice, and answer follow-up "why" questions
> without notes. Every artifact below doubles as interview ammo.

#### Morning block (3hr)

- [ ] 15 min — Anki review (focus: classification metrics + when each fails)

- [ ] 90 min — README polish (`projects/05_P1_Tabular_ML/README.md`)
  - Problem statement: frame as a **business/clinical cost** (false negative = missed
    heart disease = costly) → this is the "why recall matters" story
  - Approach + dataset description (rows, features, class balance, leakage checks)
  - Results table: precision, recall, F1, ROC-AUC per model
  - Architecture diagram (Excalidraw: data → preprocessing → model → threshold → prediction)
  - Live HF demo link + local setup
  - **Interview outcome:** I can state the problem in one sentence and justify why
    accuracy is the _wrong_ headline metric here.

- [ ] 60 min — Loom walkthrough (≤3 min)
  - Script first: problem → approach → code highlights → results → live demo
  - Record (max 2 takes), upload, embed in README
  - **Interview outcome:** the script IS my "walk me through a project you're proud of"
    answer — rehearsed, timed, tight.

- [ ] 15 min — Buffer

#### Afternoon block (3hr)

- [ ] 30 min — **Interview Q&A drill** → append to README or `concepts/` note
      Write my own answers (1-2 sentences each) to the questions THIS project invites:
  - Why did you pick recall/F1 over accuracy for this dataset?
  - How did you choose the classification threshold, and what did you trade off?
  - Why did model X beat model Y here? What would change with more data?
  - How would you detect/handle data leakage or class imbalance?
  - What breaks in production, and how would you monitor it?
  - **Outcome:** a written, reviewable Q&A bank I can quiz myself on later.

- [ ] 30 min — Twitter thread #5 → `twitter-posts/week-05-thread-p1.md`
  - Hook → problem → what I built → key insight → eval results → live link → CTA
  - POST LIVE, save URL
  - **Interview outcome:** the "key insight" line forces me to name the ONE thing I
    learned — a reusable answer to "what surprised you / what did you learn?"

- [ ] 30 min — Phase 1 gate check (all 6 must pass)
  - ✅ Live demo on HF Space
  - ✅ 3-min Loom in README
  - ✅ Architecture diagram
  - ✅ Real eval numbers
  - ✅ Twitter thread
  - ✅ Solves a real problem (heart disease screening)

- [ ] 45 min — Week 5/6 retro → `weekly-logs/retro-week-05.md`
  - What shipped, what slipped, velocity, root cause, lessons
  - Add a **"concepts I can now explain vs. still fuzzy"** section → feeds next Anki batch
  - **Interview outcome:** honest map of my knowledge gaps before they surface in a real interview.

- [ ] 15 min — Log Phase 1 gate result in `context/04-decisions-log.md`

- [ ] 15 min — 🚀 Commits: `week-06: P1 shipped + Phase 1 gate passed`
  - `week-06: retro + interview Q&A bank`

**Exit criteria:** All 6 quality-bar items pass. Retro written. Twitter posted. Gate
logged. **AND** I can deliver the 3-min pitch + answer all 6 drill questions out loud
without reading.
