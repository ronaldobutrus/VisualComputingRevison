# Question Set 7 - Natural Language Processing
### Question 1
What are four things that make up a good prompt?

#### Answer 1:
* Premise (context)
* Hypothesis (question)
* Reasoning example (how to solve the problem)
* Answer options (the possible solutions)

#### *[This question was from Variants of LLMs]*
<hr>

### Question 2
Name the character that matches zero or more repetitions of the preceding regular expression.

#### Answer 2:
The character is `*`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 3
Which equation is the Naive Bayes algorithm based on for classification?

#### Answer 3:
$$
P\left(class\middle| c o n t e n t\right)=\frac{P\left(content\middle| c l a s s\right)P\left(class\right)}{P\left(content\right)}
$$
where
* $P\left(class\middle| c o n t e n t\right)$ is the posterior probability
* $P\left(class\right)$ is the prior probability
* $P\left(content\middle| c l a s s\right)$ is the likelihood
* $P\left(content\right)$ is the probability of the data

#### *[This question was from Classification]*
<hr>

### Question 4
Name the character that matches any Unicode decimal digit.

#### Answer 4:
The character is `\d`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 5
What is top-down parsing?

#### Answer 5:
Top-down parsing starts from root non-terminal S and expands the tree downwards until the terminal words are reached. 

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 6
What is the Markov Assumption?

#### Answer 6:
The assumption that the probability of a word depends only on the previous word.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 7
What is the equation for inverse document frequency?

#### Answer 7:
$$
\text{idf}(t) = \log \left( \frac{N}{df(t)} \right)
$$
where `N` is the number of documents in the collection and `df(t)` is the document frequency of term `t`.

#### *[This question was from Performance Metrics]*
<hr>

### Question 8
What is the object of a sentence?

#### Answer 8:
The participant to whicht the action is applied.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 9
How does the continuous skip-gram model learn word embeddings?

#### Answer 9:
A logistic regression classifier is trained to distinguish between them, generating a linear-regression-style way to produce probabilities calculated using the sigmoid of their dot product.

Learned weights are used as embeddings for target word $t$.

#### *[This question was from Word Embeddings]*
<hr>

### Question 10
What is a polysemy?

#### Answer 10:
A polysemy is a word that has multiple meanings.

#### *[This question was from Lexical Semantics]*
<hr>

