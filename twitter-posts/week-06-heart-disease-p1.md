# Twitter Thread #5 — P1: Heart Disease Screening

# Free-tier limit: 280 chars/tweet. Counts shown in ( ).

---

## 1/7 — HOOK (~205 chars)

Most ML tutorials chase accuracy.

For a heart-disease model, that's dangerous.

I built a screening tool where missing ONE sick patient matters more than a false alarm — and it changed every decision I made 🧵

---

## 2/7 — PROBLEM (~250 chars)

The task: flag patients who may have heart disease.

The catch: a false NEGATIVE (telling a sick patient "you're fine") can cost a life.
A false positive just costs a follow-up test.

So accuracy is the wrong metric.
This is a RECALL problem.

---

## 3/7 — WHAT I BUILT (~255 chars)

What I built:

• sklearn Pipeline (impute → scale → encode)
• Baseline vs L1 vs L2 logistic regression
• 5-fold cross-validation
• MLflow experiment tracking
• Live Gradio app on Hugging Face

All preprocessing fit INSIDE CV — so no data leaks.

---

## 4/7 — KEY INSIGHT (~250 chars)

The insight that stuck:

The default 0.5 cutoff isn't "recall-first" — it's neutral.

To actually catch more sick patients I lowered the decision threshold to 0.3, trading some precision for higher recall.

That's a product decision, not a default.

---

## 5/7 — EVAL RESULTS (~245 chars)

Results (Disease class):

• Recall: [0.__] ← the number I optimize for
• Precision: [0.__]
• F1: [0.__]
• ROC-AUC: [0.__]

Out of every 100 patients who truly have disease, the model flags [__].
Fewer missed patients = the entire point.

---

## 6/7 — LIVE LINK (~195 chars)

Try it yourself — live, no login:

🔗 huggingface.co/spaces/mastanai/p1-tabular-ml

Enter patient values, get a real-time risk score from the exact model I trained and logged with MLflow.

---

## 7/7 — CTA (~235 chars)

I'm learning AI engineering in public — real projects, and the messy parts too
(like the duplicate-row data leak I caught before it faked my scores).

Follow for the next build 👇
What would you have done differently? Reply below.

---
