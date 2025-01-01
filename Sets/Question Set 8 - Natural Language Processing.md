# Question Set 8 - Natural Language Processing
### Question 1
What is a hyponym?

#### Answer 1:
A hyponym is a word that is more specific than another word.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 2
What are the five components of an HMM?

#### Answer 2:
$S=s_1,s_2,\cdots,s_n$ is a set of states (parts of speech)

$A=a_{11},a_{12},\cdots,a_{N1},\cdots,a_{NN}$ is a transition probability matrix (between states)

$\pi=\pi_1,\pi_2,\cdots,\pi_n$ is an initial probability distribution over states 

$O=o_1,o_2,\cdots,o_T$ is a sequence of $T$ observations (words)

$B=b_i\left(o_t\right)$ is a sequence of observation likelihoods (emission probabilities), expressing the probability of an observation $o_t$ being generated from state $s_i$

#### *[This question was from Sequence Modelling]*
<hr>

### Question 3
When does the vanishing gradient problem occur in RNNs?

#### Answer 3:
The vanishing gradient problem occurs when the model ignores the immediate context.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 4
Which `re` method is used to substitute all occurrences of a regular expression pattern with a replacement string?

#### Answer 4:
The method is `re.sub()`.

#### *[This question was from Zipf's Law]*
<hr>

### Question 5
State Zipf's Law in mathematical terms.

#### Answer 5:
In a corpus of `N` words, the normalised frequency of the `k`-th most frequent word is given by `f_k = 1 / k`.

#### *[This question was from Zipf's Law]*
<hr>

### Question 6
When does the exploding gradient problem occur in RNNs?

#### Answer 6:
The exploding gradient problem occurs when the model focuses too much on the immediate context.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 7
What is antonymy?

#### Answer 7:
Antonymy holds for words with opposite meaning. Though they might be close in meaning, they likely differ along a dimension.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 8
What is a term-document vector?

#### Answer 8:
A vector representation of a document using the frequency of terms in the document.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 9
What is machine translation?

#### Answer 9:
Machine Translation (MT) consists of translating a sentence $x$ from a source language to a sentence $y$ in a target language.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 10
Is the continuous skip-gram model supervised or unsupervised?

#### Answer 10:
The continuous skip-gram model is unsupervised (effectively self-supervised).

#### *[This question was from Word Embeddings]*
<hr>

