### StatQuest — Regularization Part 1: Ridge (L2) Regression, Clearly Explained!!!

1. What problem does Ridge solve that vanilla linear regression doesn't?
   > - when the data is small enough then linear regression may overfit testing data and on test data it may not give good predictions. So redge regression solve this problem by increasing the bias so the model works well on test data (variance).
2. What does the L2 penalty `λ·Σwⱼ²` do to the weight values during training?
   > - The L2 penalty makes the predictions less sensitive to the Data Training.
3. Why does Ridge shrink weights toward zero but never _exactly_ to zero?
   > - Ridge shrink weights to zero but never zero because if the ridge weight becomes zero the variance will be more and it might not give predictions well on test data.
4. Why must features be standardized before applying Ridge?
   > - features must be standardized before applying Ridge because each feature will represent in different units and when you are calaculating the penalty basically you are adding square of each parameter with lambda, and when you are adding if the each parameter is representing in different units and not standardized, the predictions might not be correct.
5. When would you reach for Ridge over Lasso?
   > - I can not answer right now this question because i dont know what is Lasso.

**L1 (intuition, 5 sentences):** On Tuesday

1. In your own words, what is regularization trying to prevent?
   > regulariztion is preventing to give less accurate predictions as there is increase in variance of datasets. This is espicially applicable small datasets which does not have enough data to predict the target. Regularization helps with this
2. Geometric picture: what does adding `λ·Σwⱼ²` to the loss surface look like?
   > `λ·Σwⱼ²` adding the penalty to the loss surface makes the prediction to have less slope, if the slope decreases the target variable which we need to predict becomes less sensitive the change in features. In geometrically, the slope of the predicted line will be less.
3. Why is the penalty applied to weights only, not to the bias `b`?
   > Penlaty applied only to weights because y is intercept from where the predict line starts. and when there are features are there in the dataset, bias just tells from where the fit line should starts and weights only will decides how the line should align
4. What happens at λ=0? At λ→∞?
   > -If the λ=0, then it just becomes the normal fit line i.e. linear regression line, at λ=∞, the fit line just becomes parallel the x-axis and slope of the fit line becomes very nearer to zero but not zero.
5. Why does Ridge work best when many features each contribute a little?
   > When the many features contribute to a little, the predictions becomes accurate because the ridge regression line will align in proper way to get the accurate predictions

### Ridge L2 — derivation

Ridge loss:

L = mean((y - ŷ)²) + λΣwⱼ²

For one prediction:

ŷᵢ = w·xᵢ + b

I used eᵢ = ŷᵢ - yᵢ to make the derivative cleaner.

MSE part:

∂MSE/∂wⱼ = (2/n)Σ(ŷᵢ - yᵢ)xᵢⱼ

Penalty part:

∂/∂wⱼ[λΣwⱼ²] = 2λwⱼ

So the full Ridge gradient is:

∂L/∂wⱼ = ∂MSE/∂wⱼ + 2λwⱼ

Gradient descent update:

wⱼ ← wⱼ - lr · (∂MSE/∂wⱼ + 2λwⱼ)

Sanity check: if λ = 0, the penalty disappears and this becomes normal linear regression gradient descent.

Bias note: b is not penalized, so ∂L/∂b is only the MSE derivative.

### Lasso Regression pre-reading video notes:

1. How does Lasso's penalty differ from Ridge's, mathematically?
   > Ridge penalty will square the weight `w` with λ, while Lasso's penalty will take absolute value `w`.
2. Why can Lasso drive weights _exactly_ to zero (the geometric/diamond intuition)?
   > In Lasso regression the weights for different features (or) variables can be cancelled out so it leaves only line where the slope can becomes zero
3. What does that property buy you in practice (think: feature selection)?
   > If im choosing the feature selected, then im deleting the feature i dont want which suits for Lasso Regression
4. When does Lasso outperform Ridge? When is it worse?
   > Lasso will outperform Ridge where we can remove lot of un-useful features weights, Lasso can perform worse where are lot of features but each feature has value added, when each feature value-added, if you delete Lasso can perform worse
5. What is "Elastic Net" in one sentence?
   > Elastic Net is nothing but it can do both Ridge regression as well as the Lasso Regression.
