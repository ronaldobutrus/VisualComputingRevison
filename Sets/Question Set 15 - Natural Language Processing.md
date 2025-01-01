# Question Set 15 - Natural Language Processing
### Question 1
Which methods can we use to reduce the dimensionality of our vector space model?

#### Answer 1:
Principle Component Analysis (PCA) can be used with Singular Value Decomposition (SVD) to identify dimensions with the most variance, and therefore reduce the dimensionality of word representations. This is computationally expensive.

#### *[This question was from Word Embeddings]*
<hr>

### Question 2
How can we apply Bayes' Theorem to a classification task
$
\hat{y}=\mathrm{argmax}_Y P\left(Y\middle| X\right)
$?

#### Answer 2:
$$
\hat{y}=\mathrm{argmax}_Y P\left(Y\middle| X\right)\\
=\mathrm{argmax}_Y\frac{P\left(X\middle| Y\right)P\left(Y\right)}{P\left(X\right)}\\
=\mathrm{argmax}_YP\left(X\middle| Y\right)P\left(Y\right)
$$
The maximum a posteriori (MAP) decision rule removes the denominator because the probability of the content is constant amongst the content

#### *[This question was from Classification]*
<hr>

### Question 3
At each step of the decoder, we need to take the `argmax` of the output distribution to get the next word. How do we do this efficiently, step-by-step?

#### Answer 3:
To take the `argmax` efficiently at each step of the decoder, we use a **beam search**:
* $k$ is the beam size (typically 5-10), which represents the ‘width’ of the search
* At each step, keep track of the $k$ most probable partial translations (hypotheses)
* Keep track of each hypothesis score, tracking the top $k$ scoring hypotheses
		$$score\left(y_1,\cdots,y_t\right)=log{P_{LM}}\left(y_1,\cdots,y_t\middle| x\right)=\sum_{i=1}^{t}{log{P_{LM}}\left(y_i\middle| y_{<i},x\right)}$$
* A hypothesis is complete when it produces <eos>.
* A beam search is complete when it reaches a predefined timestep $T$ or has a predefined $n$ completed hypotheses


#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 4
What is WordNet?

#### Answer 4:
WordNet is the largest, most comprehensive and most widely used database of lexical relations.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 5
What is the encoder-decoder architecture?

#### Answer 5:
The encoder-decoder architecture is a neural network that consists of an encoder and a decoder.

The encoder reads the input sentence and produces an encoding.

The decoder reads the encoding and generates the output sentence.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 6
Which `re` method is used to split a string into a list of substrings according to a regular expression pattern?

#### Answer 6:
The method is `re.split()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 7
Name the character that represents the end of a string.

#### Answer 7:
The character is `$`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 8
State Zipf's Law in simple terms.

#### Answer 8:
In a corpus, the frequency of a word is inversely proportional to its rank.

#### *[This question was from Zipf's Law]*
<hr>

### Question 9
How do the parameters in a Recurrent Neural Network (RNN) compare to those in a feedforward neural network?

#### Answer 9:
RNNs must learn an extra parameter, the matrix of weights for the previous hidden layer.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 10
What is Mean Reciprocal Rank (MRR) and what does it measure?

#### Answer 10:
$$
\mathrm{Mean\ Reciprocal\ Rank}=\sum_{i}\frac{RR_i}{\mathrm{number\ of\ queries}}
$$
MRR measures how high, on average, the algorithm places the first relevant document that it returns.

#### *[This question was from Sequence Modelling]*
<hr>

