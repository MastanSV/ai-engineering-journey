The link for the explanation of backprop pitch:
https://www.loom.com/share/c93dce8ceffc4430abe19595cf7a3dae

Questions:
Q1. Why can't we just randomly change the weights?

> Answer should be interms of scale (how big the network is) and efficiency (If you modify manually it is not possible to reduce the error)

Q2. What happens if a ReLU neuron dies?

> Answer interms of ReLU mechanism z<=0 -> 0 else z, neuron can not fix itself it needs gradiant

Q3. Why is it called "back" propagation?

> Answer interms of direction and Why the order is necessary (The chain rule depends on downstream gradients.)

Q4. What is the difference between the forward pass and the backward pass?

Answer interms of following:

- **The dependency.** The backward pass needs the values that the forward pass saved. That is why training uses more memory than inference.
- **Clear separation.** Backprop computes gradients. Gradient descent updates the weights. Many candidates mix these two up.

Q5. Do we backprop through activation functions?

Answer interms of following:

- **"Yes" plus the reason:** you multiply by the local derivative.
- **Concrete numbers:** ReLU gives 1 or 0. Sigmoid gives at most 0.25.
- **A link to vanishing gradients.** This shows real understanding, not only memory.
