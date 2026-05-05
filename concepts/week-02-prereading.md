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
