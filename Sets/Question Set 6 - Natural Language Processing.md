# Question Set 6 - Natural Language Processing
### Question 1
What is a collection?

#### Answer 1:
A set of documents.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 2
What is the equation for the Viterbi algorithm at step `t` for previous state `i` and current state `j` given the observation `o_t` for the current state?

#### Answer 2:
$$
V_t\left(j\right)=\text{max}_{i=1}^N \; V_{t-1}\left(i\right)a_{ij}b_j\left(o_t\right)
$$

#### *[This question was from Sequence Modelling]*
<hr>

### Question 3
What are Noun Phrases (NPs)?

#### Answer 3:
A sequence of words that contain a noun and surrounding words, and can fulfil the function of a noun in a sentence.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 4
What can be used to learn a function to map global features of an input to a label?

#### Answer 4:
Linear Chain Conditional Random Fields (CRFs) learns a function $f$ that maps $K$ global features of an input $x$ to the output label $y$.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 5
What is dependency parsing and how does it relate to constituency parsing?

#### Answer 5:
The goal of dependency parsing is to establish directed binary grammatical relations that hold among words of the input:
* The root node explicitly marks the root of the construction
* The heads determine the nature of the expression
* Other words are dependents.
![alt text](image.png)

#### *[This question was from Lexical Semantics]*
<hr>

### Question 6
What are morphological forms?

#### Answer 6:
Different forms of a word, e.g. singular and plural.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 7
What are the three connotations carried by words and how can this be used for representation?

#### Answer 7:
* *Valence* is the pleasantness of the stimulus
* *Arousal* is the intensity of the emotion provoked by the stimulus
* *Dominance* is the degree of control exerted by the stimulus

This can be used for representation by using a three-dimensional vector to represent the word.

#### *[This question was from Word Embeddings]*
<hr>

### Question 8
What are LSTMs?

#### Answer 8:
Long Short Term Memory (LSTM) networks are a type of RNN that use a memory cell to store information from previous time steps.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 9
What is cosine similarity and what is it used for?

#### Answer 9:
$$
\text{cosine similarity} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
$$
It is used to measure the similarity between two vectors.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 10
What is a Context Free Grammar (CFG) and what is it defined by?

#### Answer 10:
A CFG is a mathematical system for modelling constituent structure in a language.
It is defined by a set of non-terminal symbols, a set of terminal symbols (words), a set of production rules, and a start symbol.

#### *[This question was from Sequence Modelling]*
<hr>

