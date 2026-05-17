## Questions i have before starting to learn, what is ROC and AUC.

1. What does the ROC curve plot on its X and Y axes?

> - ROC curve will have on x-axis -> False Positive rate, y-axis -> True Positives rate, and ROC curve helps us to decide which is best threshold for classification

2. What does each point on the ROC curve represent?

   > - Each point on ROC curve represent threshold, will give us the idea which is better one to use. We can compare the threshold which will be better for the classification based on the number of false positives we consider as better threshold classification.

3. What does AUC = 0.5 mean? AUC = 1.0? AUC = 0?

   > When we are doing classification using different methods we get the different ROC curves and we will decide which classification method to consider using AUC. Usually we consider which has more AUC value. And AUC = 0.5 means if i pick one positive sample and one negative sample, sometimes it might score more positive and less for negative and besically AUC = 0.5 is not that much intelligence. If AUC = 1.0 means it always scores more always for the positive example and less for negative example. and AUC = 0 means it opposite of AUC 1.0 because it always scores more for negative example and less for positive example.

4. Why is AUC threshold-independent — and why is that useful?

   > AUC is threshold-independent, AUC will tell when take the sample of positive or negative it tells only how confident it is. and it will give this based on not considering the threshold because if you consider threshold what happens is that accuracy will change even though it is same model but only change in threshold which is not good. that is why AUC is useful.

5. When would you NOT use AUC (think: heavy class imbalance)?
   > I will not go AUC when the data is having more negative classification instead of positives, because in this case FPR, in denominator you will have TN which is big and your FPR will be very tiny which gives the wrong predictions.
