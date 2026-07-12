TN - what did you understand by True Negative? explain with example?
Suppose im predicting from certain dataset is that whether the patient is sick or healthy.

If the patient is sick then it will be Positive.
If the patient is healthy then it will be Negative.

True Positive - The true value for patient is sick, model predicted sick as well.
True Negative - The true value for patient is healthy or not sick, model predicted healthy as well.

False Positive - The true value for patient is healthy, but model predicted as sick.
False Negative - The true value for patient is sick, but model predicted as healthy. (This is the most dangerous thing because missing out sick patient will cost the lives of patient)

# for more clarity look for the classification_matrix display
