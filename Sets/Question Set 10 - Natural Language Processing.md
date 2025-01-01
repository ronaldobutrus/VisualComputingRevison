# Question Set 10 - Natural Language Processing
### Question 1
What is feature selection and feature weighting?

#### Answer 1:
Feature selection involves identifying the most informative among potential features (e.g. by removing stop words).
Feature weighting and normalisation involve weighting the most informative among remaining features heavier (e.g. using TF-IDF).

#### *[This question was from Classification]*
<hr>

### Question 2
What is attention and what is it used for?

#### Answer 2:
Since it is hard to compress a sentence into an encoding, and different information may be relevant at different steps in the decoder, attention allows the decoder to focus on different parts of the input sentence at different times.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 3
How can we represent a phrase using compositional semantics?

#### Answer 3:
Methods of compositional semantics allows us to derive the representation of a phrase by applying a function to the constituent word vectors, i.e. $p = f(u, v)$

#### *[This question was from Word Embeddings]*
<hr>

### Question 4
What is masked self-attention and how is it used in the transformer?

#### Answer 4:
In the encoder, each token gathers context from other tokens to update its representation.
In the decoder, we mask future tokens in the inference stage (but not during training).

#### *[This question was from Transformers]*
<hr>

### Question 5
What is Pointwise Mutual Information (PMI) and what is the equation for it?

#### Answer 5:
Pointwise Mutual Information (PMI) is a measure of how often two events x and y occur (given some relation), compared to what we would expect if they were independent.
$$
\text{PMI}(w, c) = \log \frac{P(w, c)}{P(w)P(c)}
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 6
How can an RNN be used for classification?

#### Answer 6:
In an RNN, the final hidden state accumulates history from the whole sequence. Often, a further FNN with a SoftMax is applied to output a probability distribution over the class labels.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 7
What do conditional language models maximise?

#### Answer 7:
Conditional language models maximise the probability of the output sentence given the source $x$.

$$
P\left(y\middle| x\right)=\prod_{i=1}^{n}P\left(y_i\middle| y_{<i},x\right)
$$

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 8
What is Precision@k?

#### Answer 8:
Precision@k is an algorithm which returns the precision of the top `k` results.

#### *[This question was from Performance Metrics]*
<hr>

### Question 9
What is a semantic field?

#### Answer 9:
A semantic field is a set of words that are related to each other by some semantic relation.

#### *[This question was from Classification]*
<hr>

### Question 10
Name the character that represents the start of a string.

#### Answer 10:
The character is `^`.

#### *[This question was from Regular Expressions]*
<hr>

