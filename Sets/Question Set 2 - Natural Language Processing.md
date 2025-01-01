# Question Set 2 - Natural Language Processing
### Question 1
How do we extend the probability function to a set of context words?

#### Answer 1:
$$P\left(+\middle| w,c_{1:L}\right)=\prod_{i=1}^{L}\sigma\left(-c_i\cdot w\right)$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 2
What is self-consistency?

#### Answer 2:
Self-consistency involves sampling a diverse range of reasoning paths and taking the most probable path to aggregate the final answer.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 3
What is problem decomposition?

#### Answer 3:
The same as least-to-most prompting.
Least-to-most prompting (problem decomposition) involves decomposing a question into sub-questions, solving the sub-questions (with access to the previous answer as context) and producing a final answer.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 4
State and describe briefly two common evaluation metrics for machine translation models.

#### Answer 4:
* BLEU (based on n-gram precision)
* BERTScore (based on cosine similarity with contextual embeddings from a pre-trained BERT model)

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 5
What is bottom-up parsing?

#### Answer 5:
Bottom-up parsing starts from terminal symbols, assigns PoS categories and combines them into further constituents. 

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 6
What is the difference between Large Language Models (LLMs) and Pre-Trained Language Models (PLMs)?

#### Answer 6:
Large Language Models (LLMs) are large, general-purpose models trained on diverse datasets.
Pre-Trained Language Models (PLMs) are smaller models which are trained on simple tasks to learn linguistic priors, then fine-tuned or trained for a specific task. Pre-training is self-supervised.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 7
What are Recurrent Neural Networks (RNNs)?

#### Answer 7:
In Recurrent Neural Networks (RNNs) the input to a hidden layer h_t at time t is expanded with the value of the hidden layer from the preceding time step, h_{t-1}. 

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 8
What does each word in WordNet have?

#### Answer 8:
A gloss (definition) and a synset (synonymy set).

#### *[This question was from Lexical Semantics]*
<hr>

### Question 9
What are encoder-only models used for?

#### Answer 9:
Encoder-only architectures are used for classification (e.g. Bidirectional Encoder Representations from Transformers – BERT, RoBERTa).

#### *[This question was from Variants of LLMs]*
<hr>

### Question 10
What is least-to-most prompting?

#### Answer 10:
Least-to-most prompting (problem decomposition) involves decomposing a question into sub-questions, solving the sub-questions (with access to the previous answer as context) and producing a final answer.

#### *[This question was from Variants of LLMs]*
<hr>

