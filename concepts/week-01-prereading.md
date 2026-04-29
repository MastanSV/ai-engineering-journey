## EP 1: Vectors

What is a vector (in ML/data context)?

- vector in ML/data context is representation of ordered numbers of list.

What does it mean to "add" two vectors?

- adding two vectors will be like finding out the result vector how far it is from origin. when you have two vectors, both starting from origin, when you want do addition, then you move the second vector to the tip of the first vector, then addition of the two vectors will be, draw the vector from tail of the first vector to the tip of the second vector
  will be their sum.

What does scalar multiplication do geometrically?

- strectching or sqeezing out the vectory with given scalar

Where will I use this in AI engineering?

- In AI engineering, it will be used once the data is represented in linear co-ordinate system, then the pattern of the data will be identified to make the necessary decisions.

One question I still have

- How does vector addition and multiplications will be applied in real world analogy to make the decisions.
- Why do we think all the time addition and multiplication only. [as mentioned in the video.]

## Ep 2: Linear combinations, span, basis

What is a linear combination of two vectors?

- for internally choosen basis vectors, scaling them and adding them is called linear combination.

What does "span" mean?

- from the linear combination of vectors, all vectors which are accessed by this combination is called 'span'

What is a basis (and why are î and ĵ called basis vectors)?

- Basis of vectors is linear combination of vectors that spans full space., in xy co-ordinate system, if you take any vector it will be combination x and y co-ordinate system in which so î will be basic vector which moves along x-axis, ĵ will be basic vector along y-axis, any vector in xy co-ordinate system nothing but scaling the basis vectors and adding them.

Where will I use span/basis in AI engineering?

- Embeddings live in a vector space; every embedding is a linear combination of the basis dimensions. PCA picks a new basis.

One question I still have

- The application of using span/basis in AI engineering.

## Ep 3: Linear transformations & metrices

What is a linear transformation?

- movement of vectory from one position to another linearly i.e., by keeping the origin fixed and all lines remains lines

How does a 2x2 matrix represent one?

- once you transform the vector what are the co-ordinate points basis vector i-hat and j-hat, first column will co-ordiante points i-hat and second column will be co-ordinate point of j-hat

What does the determinant tell you geometrically?

-

Where will I use this in AI engineering? (Hint: every neural net layer is Wx + b)

- In nural networks, every layer can be transformed in multiple times to get the best result

One question I still have

- The thing which im missing out is how do you represent this in geometrically which i need to answer this question. and practical usage in real-world.
