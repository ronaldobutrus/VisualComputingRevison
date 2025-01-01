# Question Set 11 - Natural Language Processing
### Question 1
What is the difference between the `re.I` and `re.IGNORECASE` flags?

#### Answer 1:
The `re.I` flag is an alias for `re.IGNORECASE`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 2
What does the decoder output vector at a point in time represent? How do we use this to generate the output?

#### Answer 2:
The decoder output at a point is the representation of the input sentence (which is input as chunks) up to that point, as well as the source context. It is then fed through a linear layer and SoftMax to produce a probability distribution over the vocabulary to sample the output from.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 3
What is an advantage and disadvantage of bottom-up parsing?

#### Answer 3:
While we only need to consider constituents compatible with the input, we need to keep track of all possible rules and subtrees even if they don’t result in S.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 4
Why is the continuous skip-gram model self-supervised?

#### Answer 4:
The target word $t$ and context word $c$ are treated as a positive example

The model randomly samples non-context words as a negative example

#### *[This question was from Word Embeddings]*
<hr>

### Question 5
What is P@k?

#### Answer 5:
P@k is given by the proportion of relevant documents in the returned k results.

#### *[This question was from Performance Metrics]*
<hr>

### Question 6
Which `re` method is used to compile a regular expression pattern into a regular expression object?

#### Answer 6:
The method is `re.compile()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 7
What can we do to term-document vectors to ensure they are comparable?

#### Answer 7:
We can normalise them.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 8
What is Mean P@k?

#### Answer 8:
$$
\mathrm{Mean\ P@k}=\sum_{i}\frac{P_i@k}{\mathrm{number\ of\ queries}}
$$

#### *[This question was from Performance Metrics]*
<hr>

### Question 9
What is homonymy?

#### Answer 9:
Homonymy is the phenomenon where a single word has multiple meanings.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 10
Name the character that matches `m` repetitions of the preceding regular expression.

#### Answer 10:
The character is `{m}`.

#### *[This question was from Regular Expressions]*
<hr>

