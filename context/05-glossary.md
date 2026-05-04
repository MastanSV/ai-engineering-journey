# Glossary

> Append as you learn. Every term you Anki-card lives here too in fuller form.
> Format: term · 1-line definition · why-it-matters-to-you note (optional).

---

## Journey-specific

- **NN (Non-Negotiable)** — One of 5 weekly habits I cannot skip without triggering a red-flag retro.
- **Red-flag week** — Any week where I miss 2+ NNs. Triggers mandatory root-cause analysis.
- **Recruiter-stops-scrolling test** — 6-criterion bar every portfolio project must pass before I move on.
- **Capstone** — Project #6, Compliance Document QA, due Week 24, must combine RAG + agents + eval + deploy + monitor.
- **Teach-back** — Mentor-graded Feynman explanation of a concept, scored 0–10 weekly.

## Setup / tooling

- **CUDA driver vs runtime** — `nvidia-smi` shows max CUDA the _driver_ supports (e.g., 13.1). `torch.version.cuda` shows the _runtime_ bundled with the PyTorch wheel (12.4). Independent.
- **`--index-url`** — Overrides default PyPI; pip pulls only from the specified URL. Used for PyTorch CUDA channels, private mirrors.
- **uv** — Modern Rust-based Python package manager. Way faster than pip; handles venvs.
- **Ollama** — Local LLM runner. `ollama run llama3.2:3b "..."` to chat. Quantized models, runs on small GPUs.

## Hugging Face

- **HF Hub** — Git-LFS-backed model/dataset/space registry.
- **Model card** — README.md with YAML frontmatter (license, language, tags). Required metadata.
- **Spaces** — Free deployed demos (Gradio/Streamlit). Where my projects will live publicly.

## LLM tooling

- **Langfuse** — Observability for LLM apps: traces every prompt+response+latency+cost. Free tier 50k events/mo.
- **OpenRouter** — Unified gateway for 300+ LLMs (one API, one key, free models available). OpenAI-compatible endpoint.
- **Gateway pattern** — Abstract LLM provider behind one interface; enables fallback, A/B test, cost routing. Senior-level architectural move.

## ML basics

- **Train/val/test split** — Partition labeled data into 3 disjoint sets: train (fit params), val (tune hyperparams + early stop), test (final unbiased estimate of generalization). Test set touched once. Week 1: used 80/20 train/test on California housing.
- **Overfitting** — Model fits training data (including its noise) so closely that performance on unseen data drops. Symptom: train MSE ≪ test MSE. Week 1: not yet hit — linreg has too few params to overfit California housing.
- **Bias** — Error from wrong assumptions about the data shape (e.g., fitting a line to a curve). High bias = underfit. In my essay: "the model is too simple to see the pattern."
- **Variance** — Error from sensitivity to the specific training sample (model wiggles a lot if you swap data). High variance = overfit. In my essay: "the model memorized noise instead of the rule."
- **Bias-variance tradeoff** — Adding capacity reduces bias but raises variance. Sweet spot minimizes total expected error. Linreg sits firmly on the high-bias / low-variance end.
- **MSE (Mean Squared Error)** — `mean((y_pred − y_true)²)`. Squaring makes errors positive and penalizes big misses harder than small ones. Differentiable everywhere → friendly to gradient descent.
- **Residual** — `y_true − y_pred` for one row. Residual plot (predicted vs actual or residuals vs predicted) reveals when linreg's assumptions break (curvature, heteroskedasticity).
- **R² (coefficient of determination)** — `1 − SS_res/SS_tot`. Fraction of variance in `y` explained by the model. 1.0 = perfect, 0 = no better than predicting the mean, negative = worse than the mean.
- **Gradient** — Vector of partial derivatives `∂L/∂params`. Points in direction of steepest **increase** of the loss.
- **Learning rate (lr)** — Step size multiplier on the gradient update `w ← w − lr·∂L/∂w`. Too high → diverge (saw lr=0.1 produce NaN); too low → crawl (saw lr=0.0001 not converge in 1000 epochs).
- **Gradient descent** — Iteratively move params **opposite** the gradient to minimize loss. Convex losses (like MSE for linreg) reach the global minimum; neural-net losses don't.
- **Cross-validation (k-fold)** — _to fill Week 2._ Split train into k folds; rotate which fold is held out; average score across k runs. Reduces dependence on a single 80/20 split.
- **Standardization** — _to fill Week 2._ Subtract mean, divide by std per feature. Mandatory before Ridge/Lasso so the L1/L2 penalty treats features fairly.
- **Regularization** — _to fill Week 2._ Add a penalty on weight magnitudes to the loss; trades a small amount of train fit for big gains in generalization.
- **L2 regularization (Ridge)** — _to fill Week 2._ Adds `λ·Σwⱼ²` to the loss; shrinks all weights toward zero, never exactly zero.
- **L1 regularization (Lasso)** — _to fill Week 2._ Adds `λ·Σ|wⱼ|` to the loss; can drive weights _exactly_ to zero → built-in feature selection.
- **alpha / λ** — _to fill Week 2._ Strength of the regularization penalty. α=0 → vanilla regression; α→∞ → all weights = 0.
- **Logistic regression** — _to fill Week 2._ Linear model + sigmoid → probability for binary classification. Loss = log-loss (cross-entropy), not MSE.
- **Sigmoid** — _to fill Week 2._ `σ(z) = 1/(1+e^-z)`. Squashes any real number into (0, 1) so it can be read as a probability.
- **Log-loss / cross-entropy** — _to fill Week 2._ `-[y·log(p) + (1-y)·log(1-p)]`. Convex in logistic regression's parameters (so GD finds the global min).
- **Decision boundary** — _to fill Week 2._ Surface in feature space where `p = 0.5` — the line/curve that separates the two predicted classes.
- **ROC / AUC** — _to fill Week 2._ ROC plots TPR vs FPR across thresholds; AUC = area under it. AUC = 0.5 random, 1.0 perfect.

## DL / Transformers (Week 5+)

- _(to fill)_

## RAG / Agents (Week 9+)

- _(to fill)_

## Fine-tuning / LLMOps (Week 17+)

- _(to fill)_

---

## Rules for this file

1. Add a term within 24 hours of meeting it.
2. Definition in YOUR words (Feynman). If you can't, you don't know it yet.
3. If a term has an Anki card, link the deck/subdeck.
4. Don't delete entries — strike them through if wrong, leave the lesson visible.
