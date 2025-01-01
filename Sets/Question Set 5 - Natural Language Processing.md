# Question Set 5 - Natural Language Processing
### Question 1
Which `re` method is used to match a regular expression pattern against a string?

#### Answer 1:
The method is `re.match()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 2
What is multi-head attention and how is it used in the transformer?

#### Answer 2:
Multiple (independent) heads concatenate their attention scores and a linear layer is applied to calculate the attention.

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 3
What are decoder-only models used for?

#### Answer 3:
Decoder-only architectures are used for generation (e.g. Generative Pre-Trained Transformer – GPT).

#### *[This question was from Variants of LLMs]*
<hr>

### Question 4
What is the word analogy task?

#### Answer 4:
The analogy task solves the question of $a$ is to $b$ what $a^\ast$ is to what?
$$
b\ast={argmax}_xdistance\left(x,a^\ast-a+b\right)
$$

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 5
What is a synset and how are they organised?

#### Answer 5:
A synset is a synonymy set. They are organised hierarchically (e.g. entity, physical entity, organism, animal, mammal, dog)

#### *[This question was from Lexical Semantics]*
<hr>

### Question 6
What is the Reciprocal Rank (RR)?

#### Answer 6:
$$
\frac{1}{\mathrm{rank\ of\ first\ relevant\ document\ in\ ordered\ list}}
$$

#### *[This question was from Performance Metrics]*
<hr>

### Question 7
What is an advantage and disadvantage of top-down parsing?

#### Answer 7:
While we only need to consider rules compatible with a well-formed sentence rooted in S, we may consider rules along the way that do not lead to the input.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 8
What is entailment?

#### Answer 8:
Entailment states that what happens to hypernyms, happens to hyponyms (but not necessarily the other way around).

#### *[This question was from Lexical Semantics]*
<hr>

### Question 9
What is F1 given by?

#### Answer 9:
The harmonic mean of precision and recall.
$$
\text{F1}=\frac{2\times\text{precision}\times\text{recall}}{\text{precision}+\text{recall}}
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 10
What is emergence and when does it occur?

#### Answer 10:
Emergence is when quantitative changes in a system result in qualitative changes in behaviour.
As the size of a model and training data size increase, the performance of the model increases at a phase transition. At about 10bn parameters, it becomes able to solve problems it could not solve before, e.g. modular arithmetic.

#### *[This question was from Variants of LLMs]*
<hr>

