# Question Set 9 - Natural Language Processing
### Question 1
What is an advantage of stemming over lemmatisation?

#### Answer 1:
Stemming can help establish links between words, e.g. "better" and "best".

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 2
What is the paraphrasing task?

#### Answer 2:
The paraphrasing task tests whether one word/phrase can replace another word/phrase in a given context.

#### *[This question was from Word Embeddings]*
<hr>

### Question 3
What does the continuous skip-gram model use to calculate the probability of a positive example?

#### Answer 3:
The classifier calculates the probability that $c$ is a context word for $w$ as:
$$
P\left(+\middle| w,c\right)=\sigma\left(c\cdot w\right)=\frac{1}{e^{-c\cdot w}}
$$
$$
P\left(-\middle| c,w\right)=1-\sigma\left(c\cdot w\right)
$$
The trained weights therefore provide a linear regression-style way to produce these probabilities.

#### *[This question was from Word Embeddings]*
<hr>

### Question 4
Name the character that matches an empty string not at the start or end of a word.

#### Answer 4:
The character is `\B`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 5
What are two common problems with language models?

#### Answer 5:
* Bias due to only the most frequent data being stored.
* Hallucination by generating data that is not present in the training data.

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 6
Name the character that matches any character except a Unicode decimal digit.

#### Answer 6:
The character is `\D`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 7
What is stemming?

#### Answer 7:
Removing the suffixes from a word to form its root form (stem).

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 8
What is the difference between sparse and dense vectors?

#### Answer 8:
Sparse vectors are based on the co-occurrence of words within a context window, whereas dense vectors are based on the distribution of words within a semantic space (i.e. embeddings).

#### *[This question was from Word Embeddings]*
<hr>

### Question 9
Which `re` method is used to search a regular expression pattern against a string?

#### Answer 9:
The method is `re.search()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 10
What are two schemes for NER, and what do they mark?

#### Answer 10:
* The BIO scheme marks the beginning (B), inside (I) and outside (O) tokens.
* The BIOES scheme also marks the end (E) tokens and single-token entities (S).

#### *[This question was from Recurrent Neural Networks]*
<hr>

