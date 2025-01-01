# Question Set 16 - Natural Language Processing
### Question 1
What type of attention is used in the transformer and what is its equation?

#### Answer 1:
Self attention (scaled dot-product) is used 
$$
\text{Attention}\left(Q,K,V\right)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

#### *[This question was from Transformers]*
<hr>

### Question 2
What is Part of Speech (PoS) tagging?

#### Answer 2:
The task of labelling each word in a sentence with its part of speech.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 3
What is lexical semantics?

#### Answer 3:
A branch of linguistics and NLP that deals with word senses.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 4
What is an encoding and how is it used in an RNN as input?

#### Answer 4:
An encoding is a representation of the input sentence as a sequence of vectors, that is a representation of an idea or thought that will contribute to generated output.

The encoding is used as the initial hidden state of the RNN.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 5
What are the core components of the Early Parsing Algorithm and how do they work?

#### Answer 5:
It keeps track of the step ID, the rule for the grammar, the covered span of the sentence by this rule, rule IDs for sub-constituents and the ID of the word being processed. 

It has three stages: 
* The predictor considers the rules and tries to expand non-terminals waiting to be expanded (with a • to their left).
* The scanner considers any non-terminals waiting to be expanded which are consistent with the input sentence.
* The completer propagates fully explored non-terminals.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 6
What is chain of thought prompting?

#### Answer 6:
Chain of thought prompting encourages models to generate a rationale, increasing the likelihood of a correct answer (this is in-context learning).

#### *[This question was from Variants of LLMs]*
<hr>

### Question 7
What is a reversed index?

#### Answer 7:
A mapping of tokens to their documents.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 8
What is the Early Parsing Algorithm?

#### Answer 8:
The Earley parsing algorithm tries to recursively apply rules until the root non-terminal is fully processed or there is no input remaining to process.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 9
What is the Naive assumption?

#### Answer 9:
The naïve (independence) assumption states that the occurrence of each feature given the class is independent of the occurrence of any other feature in the class.

#### *[This question was from Classification Metrics]*
<hr>

### Question 10
What is sequence modelling?

#### Answer 10:
Machine learning tasks involving labelling sequences of input, e.g. PoS tagging.

#### *[This question was from Introduction]*
<hr>

