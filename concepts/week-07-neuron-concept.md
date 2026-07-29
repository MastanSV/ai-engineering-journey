- If Logistic Regression already solves classification problems, why do we need Neural Networks?
  - Logistic regression will classify only if the decision boundary is linear. suppose if the decision boundary is non-linear then it fails. To solve this problem Neural Network came into picture.

Key take-aways:

- Logistic regression is linear decision boundary model
- But many real world problems are non - linear
- A nueral network is non-linear model
- neural network makes small decisions across layers and make final output decision.

A neuron is nothing but which holds the number.
The number ranges from 0-1, is called Activation.

Suppose if we have 28\*28 pixels, and represent some number ex: 7, these pixels will form the first layer, inorder to get the next layer, for each pixel which is nothing but neuron (contains activation) has to be multiplied with weight, then if we want bias that can be added, which will form the next layer like each new layer will form based on previous untill the final decision made. This network is called Neural Network.

![Overview diagrams for logistic regression and neural network formula](images/intro_neural_network.png)
