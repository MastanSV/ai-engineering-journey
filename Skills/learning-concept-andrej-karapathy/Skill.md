---
name: learn-concept
description: "Teach any AI / ML / LLM engineering concept with Andrej Karpathy's output ladder: clear ASD-STE100-style writing, then a diagram, then an interactive HTML page, then (optional) a 3Blue1Brown-style narrated explainer video. USE WHEN the user says: learn, explain, teach me, help me understand, visualize, make an explainer, ELI5, or names a concept (backprop, attention, softmax, embeddings, RAG, LoRA, etc.). Uses only free tools."
argument-hint: "<concept> [text|diagram|html|video] [what I know]  — or 'help'"
---

# Learn a Concept — Karpathy Output Ladder

Source idea (Andrej Karpathy, X post): we spend more time understanding model output, so pick an
output format that is easy to understand. Each rung is better than the one before:

1. **Writing** in ~80% ASD-STE100 (Simplified Technical English).
2. **Diagram** — easier to parse than text.
3. **HTML page** — a beautiful, interactive web page.
4. **Explainer video** — custom, 3b1b style, with narration.

Artifacts are **custom and discardable**. Build them freely; do not over-polish.

## Help mode

If the argument is empty, `help`, `?`, or `how to use`: do NOT build anything. Print this guide and stop:

```text
/learn-concept <concept> [level] [what I already know]

level (optional):
  text     -> rung 1 only (STE-style explanation)
  diagram  -> rungs 1-2
  html     -> rungs 1-3   (DEFAULT)
  video    -> rungs 1-4   (needs ffmpeg; slow)

Examples:
  /learn-concept softmax
  /learn-concept attention in transformers html
  /learn-concept backprop dW1 for X(4,2), hidden 4, output 1 - I know the forward pass
  /learn-concept LoRA video
  /learn-concept help

Follow-ups in the same chat:
  "go one rung up"         -> build the next format
  "rate my explanation: …" -> Feynman score 0-10 + gaps
  "rate my anki answers: …"-> score + polished version
  "simpler" / "deeper"     -> re-explain at another level

Output folder: %USERPROFILE%\learning-explainers\<concept-slug>\
```

## Hard rules

- **Do not create or edit files in the current workspace / git repo.** Write all artifacts to
  `%USERPROFILE%\learning-explainers\<concept-slug>\` (create the folder). Only write elsewhere if the
  user names a path.
- **Free tools only.** No paid API keys (no ElevenLabs, no OpenAI). Prefer local tools.
- **Do not assume knowledge.** Define every term the first time you use it.
- **Correctness first.** If a fact, shape, or formula is uncertain, say so. Check math with a small
  runnable example (numpy) when possible.

## Step 0 — Scope (no questions unless blocked)

Read the request. Get: the concept, the requested level, and the user's current understanding.
Defaults when not given:

- Level: **text + diagram + HTML** (rungs 1–3). Do rung 4 (video) only if the user asks for "video".
- Audience: a software engineer (SDE2) who is learning AI engineering. Knows Python. Math is rusty.

Then write these 4 lines at the top of the chat answer:

- **Concept:** …
- **You need first (prerequisites):** max 3 items, each with a one-line reminder.
- **Main question this answers:** one sentence.
- **Output folder:** full path.

## Rung 1 — Writing (~80% ASD-STE100)

Write the explanation in the chat **and** save it as `01-explanation.md`.

STE-style rules (soften ~20% when a rule makes the text unnatural):

- One topic per sentence. Max ~20 words per sentence. Max ~6 sentences per paragraph.
- Active voice. Present tense. Use "you" for the reader.
- One word = one meaning. Use the same term every time (no synonyms for variety).
- Use simple, common words. No idioms, no metaphors without a plain statement next to them.
- Do not drop articles ("the", "a"). Do not stack more than 3 nouns.
- Procedures: numbered steps, one action per step, command verb first.
- Put a warning or note **before** the step it applies to.

Structure of `01-explanation.md`:

1. **One-sentence essence.**
2. **The problem it solves** (what fails without it).
3. **How it works** — numbered steps.
4. **Tiny worked example with real numbers** (small sizes, e.g. 2×3 matrices). Show every
   intermediate value and every **shape**. Verify numbers with a numpy snippet before showing them.
5. **The math** — formula, then each symbol in plain words, then the intuition in one sentence.
6. **Where it is used in AI engineering** (LLMs, RAG, fine-tuning, production) — 2–4 bullets.
7. **Common mistakes** — table: mistake | why it happens | fix.
8. **Check yourself** — 5 questions (2 recall, 2 "why", 1 "what happens if…"). Put answers in a
   collapsed `<details>` block.
9. **Feynman test** — ask the user to write a 3-sentence, zero-jargon explanation. Offer to rate it 0–10.

## Rung 2 — Diagram

Create `02-diagram.mmd` (Mermaid) and also embed the same diagram in `01-explanation.md` in a
` ```mermaid ` block so it renders in VS Code / GitHub preview.

- One diagram = one idea. If the concept has a "data flow" and a "math flow", make two diagrams.
- Label arrows with **what moves** (value + shape), e.g. `Z1 (4×4)`.
- Max ~12 nodes. Use subgraphs for layers / stages. Use the same names as in Rung 1.
- Validate syntax: no parentheses or special characters in node text unless quoted.

## Rung 3 — Interactive HTML page

Create `03-interactive.html`: **one self-contained file** (inline CSS + JS, no build step, works
offline; a CDN is allowed only for Mermaid/KaTeX and must degrade gracefully).

Must include:

- **Top:** the one-sentence essence + a "you need first" box.
- **Interactive core:** sliders / inputs for the key numbers (e.g. weights, learning rate, temperature,
  input vector). All dependent values and a visual (canvas/SVG chart, matrix grid, flow animation)
  **update live**.
- **Step-through mode:** "Prev / Next" buttons that walk the computation one step at a time,
  highlighting the active part and showing the numbers + shapes for that step.
- **"What if" presets:** 2–4 buttons that set values to show edge cases (e.g. learning rate too high,
  vanishing gradient, temperature → 0).
- **Quiz:** the 5 check-yourself questions, click to reveal.
- Clean, readable design: dark/light friendly, large font, color = meaning (same color for the same
  quantity everywhere). No external images.

Compute values in JS with the same formulas as Rung 1, and make sure the default values reproduce the
Rung 1 worked example exactly. After writing the file, open it: `Start-Process "<path>"`.

## Rung 4 — Explainer video (only on request)

Goal: a 2–5 minute, 3Blue1Brown-style narrated video. Free stack:

- **Animation:** Manim Community Edition (`manim`). Use `Text`/`MarkupText`; use `MathTex` only if a
  LaTeX install is present (check with `latex --version`).
- **Narration (free):** Piper TTS (local, offline) first; fallback `edge-tts` (free, online, no key);
  last fallback `pyttsx3` (offline, robotic).
- **Muxing:** `ffmpeg`.

Procedure:

1. Write `04-video/script.md`: 5–8 scenes. Per scene: narration text (STE style, ≤ 60 words) +
   what is on screen.
2. Create an isolated env **inside the output folder**: `uv venv .venv` (or `python -m venv .venv`),
   then install `manim` and the TTS package there. Never install into the user's project env.
3. Check `ffmpeg -version`. If missing, tell the user the install command (`winget install ffmpeg`) and stop.
4. Generate one audio file per scene. Measure each duration. Make each Manim scene wait to match it.
5. Render at `-qm` (720p) first. Concatenate scenes and add audio with ffmpeg → `04-video/final.mp4`.
6. Open the result. Report the total length and any scene that looks wrong.

If a step fails twice, stop and report the exact error plus the simplest fix.

## Finish

End the chat answer with:

- A table of created files (path + one-line purpose).
- **3 Anki card prompts** (question only). The user writes the answers in their own words; offer to
  rate them.
- **One "do it yourself" task** (≤ 30 min, by hand or in code) that proves the concept is learned.
- Suggest the next rung up if it was not built.
