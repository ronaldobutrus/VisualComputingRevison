# Question Set 4 - Natural Language Processing
### Question 1
Why can stop words be removed from a corpus?

#### Answer 1:
According to Zipf's Law, stop words have the highest frequency and can be removed without significantly affecting the corpus.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 2
What are the key (five) steps of an end-to-end IR application pipeline?

#### Answer 2:
1. Raw text processing
2. Morphology
3. Word level
4. Syntax
5. Semantics

#### *[This question was from Introduction]*
<hr>

### Question 3
What is the subject of a sentence?

#### Answer 3:
The main participant of the action.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 4
How many embeddings are there in the continuous skip-gram model, and how do we find the single embedding for a word?

#### Answer 4:
There are two embeddings per word, as a target and as a context, and the final embedding is the sum of the two, i.e. $t_i=w_i+c_i$.

#### *[This question was from Word Embeddings]*
<hr>

### Question 5
What is a term?

#### Answer 5:
A word or phrase which occurs in a collection and helps to locate relevant documents in a collection.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 6
Name the character that matches any Unicode non-word character.

#### Answer 6:
The character is `\W`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 7
Name the character that represents any character except a newline.

#### Answer 7:
The character is `.`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 8
Derive the equation for the output sequence $Y$ given the input sequence $X$ and the $K$ global features for a CRF.

Start with $Y=argmax_{Y\in\mathcal{Y}}P\left(Y\middle| X\right)$

#### Answer 8:
The model assigns each of the features $F_k$ with a weight $w_k$, so
$$
P\left(Y\middle| X\right)=\frac{\exp{\left(\sum_{k=1}^{K}{w_kF_k\left(X,Y\right)}\right)}}{\sum_{Y^\prime\in\mathcal{Y}} \exp{\left(\sum_{k=1}^{K}{w_kF_k\left(X,Y^\prime\right)}\right)}}
$$
Since the denominator is constant for a given $X$ for all $Y^\prime$, we have
$$
Y=\argmax_{y\in\mathcal{Y}}\exp{\left(\sum_{k=1}^{K}{w_kF_k\left(X,Y\right)}\right)}
$$
Splitting $F_k$ into a sum of $f_k$, we have
$$
Y=\argmax_{y\in\mathcal{Y}}exp{\left(\sum_{k=1}^{K}{w_k\sum_{i=1}^{n}{f_k\left(y_{i-1},y_i,X,i\right)}}\right)}
$$
Since exp does not affect the argmax, we have
$$
Y=\argmax_{y\in\mathcal{Y}}\sum_{k=1}^{K}{\sum_{i=1}^{n}w_kf_k\left(y_{i-1},y_i,X,i\right)}
$$

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 9
What is neural machine translation?

#### Answer 9:
Neural Machine Translation (NMT) is MT using neural networks, which are end-to-end differentiable.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 10
What is accuracy given by?

#### Answer 10:
$$
\text{accuracy}=\frac{\text{correct predictions}}{\text{total predictions}}
$$

#### *[This question was from Classification Metrics]*
<hr>

