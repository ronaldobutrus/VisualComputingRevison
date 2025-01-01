# Question Set 13 - Natural Language Processing
### Question 1
What two things does a transformer do that an RNN does not?

#### Answer 1:
* Parallel processing of sentence (faster pre-training, leading to better downstream performance)
* Lower computational complexity per layer 

#### *[This question was from Transformers]*
<hr>

### Question 2
What does word analogy mean and how can it be used for representation?

#### Answer 2:
Word analogy is the task of finding the relationship between two words, e.g. king is to queen as man is to woman.

This can be used for representation by using a word analogy task to learn a vector space model of word meaning.

#### *[This question was from Word Embeddings]*
<hr>

### Question 3
What is precision given by?

#### Answer 3:
$$
\text{precision}=\frac{\text{true positives}}{\text{predicted positives}}
$$

#### *[This question was from Classification Metrics]*
<hr>

### Question 4
What is metonymy?

#### Answer 4:
Metonymy is the use of a word to refer to something else that is closely associated with it.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 5
What is program of thought prompting?

#### Answer 5:
Program of thought prompting involves generating a computer program to compute the answer to a complex problem.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 6
What are homophones?

#### Answer 6:
Homophones are words that sound the same but have different meanings.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 7
What is a web crawler?

#### Answer 7:
A program that recursively downloads web pages and stores them in a database.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 8
What is an indirect object?

#### Answer 8:
A participant of the action that is not the main participant.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 9
The goal of decoding is to find the most likely sequence of hidden states that produced a sequence of observations. Derive the equation for the most likely sequence of hidden states $\hat{t}_{1:n}$ given a sequence of observations $w_{1:n}$.

#### Answer 9:
$$
S=t_1,t_2,\cdots,t_T
$$
$$
{\hat{t}}_{1:n}={\mathrm{argmax}}_{t_1,\cdots,t_n}P\left(t_1\cdots t_n\middle| w_1\cdots w_n\right)
$$
By Bayes’ Theorem we have 
$$
{\hat{t}}_{1:n}={\mathrm{argmax}}_{t_1,\cdots,t_n}\frac{P\left(w_1,\cdots,w_n\middle| t_1,\cdots,t_n\right)P\left(t_1,\cdots,t_n\right)}{P\left(w_1,\cdots,w_n\right)}
$$
Since the denominator is equal across the observation
$$
{\hat{t}}_{1:n}={\mathrm{argmax}}_{t_1,\cdots,t_n}P\left(w_1,\cdots,w_n\middle| t_1,\cdots,t_n\right)P\left(t_1,\cdots,t_n\right)
$$
By the HMM assumptions, 
$$
P\left(w_1,\cdots,w_n\middle| t_1,\cdots,t_n\right)=\prod_{i=1}^{n}{P\left(w_i\middle| t_i\right)}
$$
and
$$
P\left(t_1,\cdots,t_n\right)=\prod_{i=1}^{n}{P\left(t_i\middle| t_{i-1}\right)}
$$
Therefore,
$$
{\hat{t}}_{1:n}={\mathrm{argmax}}_{t_1,\cdots,t_n}\prod_{i=1}^{n}{P\left(w_i\middle| t_i\right)P\left(t_i\middle| t_{i-1}\right)}
$$

#### *[This question was from Sequence Modelling]*
<hr>

### Question 10
What is parsing?

#### Answer 10:
The task of producing a tree structure that represents the syntactic structure of a sentence.

#### *[This question was from Syntactic Analysis]*
<hr>

