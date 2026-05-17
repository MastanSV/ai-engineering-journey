### Twitter post link: https://x.com/mastan_ai/status/2055971907586105384?s=20

Fair enough — you've already done the learning (teach-back + notebook). Here's a ready-to-post thread based on **your own findings**:

---

**Tweet 1 (Hook)**

Built linear regression last week. This week, broke it on purpose with Ridge and Lasso. Here's what regularization actually does to your weights 🧵

**Tweet 2 (The problem)**

Plain linear regression finds the "best fit" by minimizing squared errors. But with noisy or limited data, it overfits — low bias, high variance. Your predictions swing wildly from dataset to dataset. Regularization trades a little bias for much less variance.

**Tweet 3 (Ridge / L2)**

Ridge adds λ·w² to the loss. Every weight gets shrunk toward zero, but never reaches it. On California housing (8 features), Ridge barely moved the needle — MSE improved by 0.0000367. Why? The model was already underfitting at R² ≈ 0.58. Regularization can't fix a model that isn't overfitting.

**Tweet 4 (Lasso / L1)**

Lasso adds λ·|w| instead. The absolute-value penalty can drive weights to exactly zero — automatic feature selection. My Lasso zeroed out 5 of 8 features: AveRooms, AveBedrms, Population, AveOccup, Longitude. Only MedInc, HouseAge, and Latitude survived.

**Tweet 5 (The plot)**

[ATTACH 3-way coefficient chart from notebook 05]

This says it all. Ridge bars ≈ Linear bars (barely any shrinkage). Lasso bars vanish for 5 features. One penalty shrinks. The other eliminates.

**Tweet 6 (Critical reflection)**

But wait — AveBedrms and AveRooms probably matter for house prices. Why'd Lasso kill them? They're collinear (bedrooms ≈ subset of rooms). Lasso picks one correlated feature and zeros the rest. Lesson: don't blindly trust automatic feature selection. Explore your data first.

**Tweet 7 (Wrap + CTA)**

Key takeaway: Ridge when all features matter, Lasso when you suspect noise features exist. Next up: cross-validation to see if my single 80/20 split was lying to me. Follow along if you're learning ML in public 🚀
