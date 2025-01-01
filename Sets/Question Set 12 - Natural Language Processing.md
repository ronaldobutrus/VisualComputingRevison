# Question Set 12 - Natural Language Processing
### Question 1
What is a synonym?

#### Answer 1:
A synonym is a word with the same or nearly the same meaning as another word.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 2
What is in-context learning?

#### Answer 2:
In-context learning is a method of learning from a small number of examples by providing the model with a set of examples and then asking it to predict the output for a new example.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 3
What are Named Entities?

#### Answer 3:
Named entities are groups of words that can be referred to with a proper noun.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 4
What is a document?

#### Answer 4:
Any unit of text indexed in a system and available for retrieval.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 5
Name the character that matches any Unicode word character (alphanumeric and underscore).

#### Answer 5:
The character is `\w`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 6
What is the loss function for the continuous skip-gram model?

#### Answer 6:
The goal of the model is to update the randomly initialised embeddings so that similarity in each $\left(w,c_{pos}\right)$ embedding is maximised and in $\left(w,c_{neg}\right)$ is minimised, using stochastic gradient descent.

The loss function $L_{CE}$ is used:
$$
L_{CE}=-\log{\left[P\left(+\middle| w,c_{pos}\right)+\prod_{i=1}^{k}{P\left(-\middle| w,c_{neg_i}\right)}\right]}
$$
$$
=\left[\sigma\left(c_{pos}\cdot w\right)+\sum_{i=1}^{k}log\left(1-P\left(+\middle| w,c_{neg_i}\right)\right)\right]
$$
$$
=\left[\sigma\left(c_{pos}\cdot w\right)+\sum_{i=1}^{k}log\left(\log{\sigma}\left(-c_{neg_i}\cdot w\right)\right)\right]
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 7
What is a constituent?

#### Answer 7:
A constituent is a sequence of words that can fulfil the function of a part of a sentence.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 8
What is Positive PMI (PPMI)?

#### Answer 8:
Positive PMI (PPMI) is a variant of PMI that only considers the co-occurrence of words that occur together more than expected by chance.
$$
\text{PPMI}(w, c) = \max\left(0, \text{PMI}(w, c)\right)
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 9
What is a hypernym?

#### Answer 9:
A hypernym is a word that is more general than another word.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 10
What is one advantage of sparse word embeddings over dense word embeddings?

#### Answer 10:
Sparse word embeddings are better at capturing polysemy.

#### *[This question was from Word Embeddings]*
<hr>

