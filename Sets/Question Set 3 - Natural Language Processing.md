# Question Set 3 - Natural Language Processing
### Question 1
How are attention scores calculated and applied?

#### Answer 1:
At each step of the decoder, we have a direct connection to the encoder to focus on a particular part of the source sequence
* We calculate attention scores for each encoder hidden state, apply a SoftMax and calculate a weighted sum. 
* We concatenate this with the decoder hidden state and produce an output.
* The attention score is calculated from the encoder hidden states $h_1,\cdots,h_n$ and decoder hidden state $s$ by one of:
    * dot-product 	$score_i=s^Th_i$
    * multiplication with learned weights	$score_i=s^TWh_i$
    * addition with learned hidden state and combination weights
$$score_i=v^Ttanh{\left(W_1h_i+W_2s\right)}$$

#### *[This question was from Transformers]*
<hr>

### Question 2
What can we use to model the underlying sequence of hidden states that produced our observations?

#### Answer 2:
Hidden Markov Models (HMMs).

#### *[This question was from Sequence Modelling]*
<hr>

### Question 3
What is recall given by?

#### Answer 3:
$$
\text{recall}=\frac{\text{true positives}}{\text{actual positives}}
$$

#### *[This question was from Classification Metrics]*
<hr>

### Question 4
What is distributional semantics and how can this be used for representation?

#### Answer 4:
Distributional semantics is a method of representing words in a way that captures their meaning based on the contexts in which they appear.

A word can be represented by a point vector in a multi-dimensional semantic space, where the word’s meaning is distributed amongst its neighbours according to their co-occurrence within a specified context window.

#### *[This question was from Word Embeddings]*
<hr>

### Question 5
What is a query?

#### Answer 5:
A user's search request expressed as a set of terms.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 6
What is supervised learning?

#### Answer 6:
Machine learning with labelled data.

#### *[This question was from Introduction]*
<hr>

### Question 7
What is the purpose of the `tf-idf` weighting scheme?

#### Answer 7:
TF-IDF downweighs overly frequent terms in a collection and increases the weights of rarer terms with higher discriminatory power.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 8
Name the character that matches one or more repetitions of the preceding regular expression.

#### Answer 8:
The character is `+`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 9
What are three advantages of dense word embeddings over sparse word embeddings?

#### Answer 9:
* Shorter vectors are easier to work with and learn weights for
* Smaller parameter space helps improve generalisation
* Dense vectors are better at capturing synonymy

#### *[This question was from Word Embeddings]*
<hr>

### Question 10
What is Retrieval Augmented Generation (RAG)?

#### Answer 10:
Retrieval Augmented Generation (RAG) is a method of generating text by retrieving relevant information from a knowledge base, splitting them into chunks, encoding as vectors, retrieving the top k chunks based on semantic similarity and using this additional context to generate the output.

#### *[This question was from Variants of LLMs]*
<hr>

