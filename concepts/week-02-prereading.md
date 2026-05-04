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
