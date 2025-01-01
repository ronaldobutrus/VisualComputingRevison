# Answers - Natural Language Processing
### Question 1
What is supervised learning?

#### Answer 1:
Machine learning with labelled data.

#### *[This question was from Introduction]*
<hr>

### Question 2
What is unsupervised learning?

#### Answer 2:
Machine learning with unlabelled data.

#### *[This question was from Introduction]*
<hr>

### Question 3
What is sequence modelling?

#### Answer 3:
Machine learning tasks involving labelling sequences of input, e.g. PoS tagging.

#### *[This question was from Introduction]*
<hr>

### Question 4
What are the key (five) steps of an end-to-end IR application pipeline?

#### Answer 4:
1. Raw text processing
2. Morphology
3. Word level
4. Syntax
5. Semantics

#### *[This question was from Introduction]*
<hr>

### Question 5
What is tokenisation?

#### Answer 5:
The task of separating a text into tokens.

#### *[This question was from Regular Expressions]*
<hr>

### Question 6
Name the character that represents any character except a newline.

#### Answer 6:
The character is `.`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 7
Name the character that represents the start of a string.

#### Answer 7:
The character is `^`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 8
Name the character that represents the end of a string.

#### Answer 8:
The character is `$`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 9
Name the character that matches zero or more repetitions of the preceding regular expression.

#### Answer 9:
The character is `*`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 10
Name the character that matches one or more repetitions of the preceding regular expression.

#### Answer 10:
The character is `+`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 11
Name the character that matches zero or one repetitions of the preceding regular expression.

#### Answer 11:
The character is `?`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 12
Name the character that matches `m` repetitions of the preceding regular expression.

#### Answer 12:
The character is `{m}`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 13
Name the character that matches an empty string at the start or end of a word.

#### Answer 13:
The character is `\b`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 14
Name the character that matches an empty string not at the start or end of a word.

#### Answer 14:
The character is `\B`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 15
Name the character that matches any Unicode decimal digit.

#### Answer 15:
The character is `\d`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 16
Name the character that matches any character except a Unicode decimal digit.

#### Answer 16:
The character is `\D`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 17
Name the character that matches any Unicode whitespace character.

#### Answer 17:
The character is `\s`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 18
Name the character that matches any Unicode word character (alphanumeric and underscore).

#### Answer 18:
The character is `\w`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 19
Name the character that matches any Unicode non-word character.

#### Answer 19:
The character is `\W`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 20
What is the difference between the `re.I` and `re.IGNORECASE` flags?

#### Answer 20:
The `re.I` flag is an alias for `re.IGNORECASE`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 21
Which `re` method is used to compile a regular expression pattern into a regular expression object?

#### Answer 21:
The method is `re.compile()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 22
Which `re` method is used to match a regular expression pattern against a string?

#### Answer 22:
The method is `re.match()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 23
Which `re` method is used to search a regular expression pattern against a string?

#### Answer 23:
The method is `re.search()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 24
Which `re` method is used to split a string into a list of substrings according to a regular expression pattern?

#### Answer 24:
The method is `re.split()`.

#### *[This question was from Regular Expressions]*
<hr>

### Question 25
Which `re` method is used to substitute all occurrences of a regular expression pattern with a replacement string?

#### Answer 25:
The method is `re.sub()`.

#### *[This question was from Zipf's Law]*
<hr>

### Question 26
State Zipf's Law in simple terms.

#### Answer 26:
In a corpus, the frequency of a word is inversely proportional to its rank.

#### *[This question was from Zipf's Law]*
<hr>

### Question 27
State Zipf's Law in mathematical terms.

#### Answer 27:
In a corpus of `N` words, the normalised frequency of the `k`-th most frequent word is given by `f_k = 1 / k`.

#### *[This question was from Zipf's Law]*
<hr>

### Question 28
What are words with the highest frequency called?

#### Answer 28:
Stop words.

#### *[This question was from Zipf's Law]*
<hr>

### Question 29
Why can stop words be removed from a corpus?

#### Answer 29:
According to Zipf's Law, stop words have the highest frequency and can be removed without significantly affecting the corpus.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 30
What is the difference between Large Language Models (LLMs) and Pre-Trained Language Models (PLMs)?

#### Answer 30:
Large Language Models (LLMs) are large, general-purpose models trained on diverse datasets.
Pre-Trained Language Models (PLMs) are smaller models which are trained on simple tasks to learn linguistic priors, then fine-tuned or trained for a specific task. Pre-training is self-supervised.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 31
What is a web crawler?

#### Answer 31:
A program that recursively downloads web pages and stores them in a database.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 32
What is a forward index?

#### Answer 32:
A mapping of documents to their tokens.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 33
What is a reversed index?

#### Answer 33:
A mapping of tokens to their documents.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 34
What is a document?

#### Answer 34:
Any unit of text indexed in a system and available for retrieval.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 35
What is a collection?

#### Answer 35:
A set of documents.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 36
What is a term?

#### Answer 36:
A word or phrase which occurs in a collection and helps to locate relevant documents in a collection.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 37
What is a query?

#### Answer 37:
A user's search request expressed as a set of terms.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 38
What are morphological forms?

#### Answer 38:
Different forms of a word, e.g. singular and plural.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 39
What is lemmatisation?

#### Answer 39:
Converting a word into its base form (lemma).

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 40
What is stemming?

#### Answer 40:
Removing the suffixes from a word to form its root form (stem).

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 41
What is an advantage of lemmatisation over stemming?

#### Answer 41:
Lemmatisation preserves the original word, whereas stemming may produce an incorrect word.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 42
What is an advantage of stemming over lemmatisation?

#### Answer 42:
Stemming can help establish links between words, e.g. "better" and "best".

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 43
What is a disadvantage of lemmatisation?

#### Answer 43:
It is computationally expensive and requires a lookup table for each language.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 44
What is a disadvantage of stemming?

#### Answer 44:
Stemmers may be too aggressive and produce incorrect words.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 45
What is a term-document vector?

#### Answer 45:
A vector representation of a document using the frequency of terms in the document.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 46
What is a term-document matrix?

#### Answer 46:
A matrix representation of a collection using the frequency of terms in the documents.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 47
What can we do to term-document vectors to ensure they are comparable?

#### Answer 47:
We can normalise them.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 48
What is cosine similarity and what is it used for?

#### Answer 48:
$$
\text{cosine similarity} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}
$$
It is used to measure the similarity between two vectors.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 49
What is the purpose of the `tf-idf` weighting scheme?

#### Answer 49:
TF-IDF downweighs overly frequent terms in a collection and increases the weights of rarer terms with higher discriminatory power.

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 50
What is the equation for TF-IDF?

#### Answer 50:
$$
\text{tf-idf}(t, d) = \text{tf}(t, d) \times \text{idf}(t)
$$
where `tf(t, d)` is the term frequency of term `t` in document `d` and `idf(t)` is the inverse document frequency of term `t`.  

#### *[This question was from Storing and Retrieving Information]*
<hr>

### Question 51
What is the equation for inverse document frequency?

#### Answer 51:
$$
\text{idf}(t) = \log \left( \frac{N}{df(t)} \right)
$$
where `N` is the number of documents in the collection and `df(t)` is the document frequency of term `t`.

#### *[This question was from Performance Metrics]*
<hr>

### Question 52
What is Precision@k?

#### Answer 52:
Precision@k is an algorithm which returns the precision of the top `k` results.

#### *[This question was from Performance Metrics]*
<hr>

### Question 53
What is P@k?

#### Answer 53:
P@k is given by the proportion of relevant documents in the returned k results.

#### *[This question was from Performance Metrics]*
<hr>

### Question 54
What is Mean P@k?

#### Answer 54:
$$
\mathrm{Mean\ P@k}=\sum_{i}\frac{P_i@k}{\mathrm{number\ of\ queries}}
$$

#### *[This question was from Performance Metrics]*
<hr>

### Question 55
What is the Reciprocal Rank (RR)?

#### Answer 55:
$$
\frac{1}{\mathrm{rank\ of\ first\ relevant\ document\ in\ ordered\ list}}
$$

#### *[This question was from Performance Metrics]*
<hr>

### Question 56
What is Mean Reciprocal Rank (MRR) and what does it measure?

#### Answer 56:
$$
\mathrm{Mean\ Reciprocal\ Rank}=\sum_{i}\frac{RR_i}{\mathrm{number\ of\ queries}}
$$
MRR measures how high, on average, the algorithm places the first relevant document that it returns.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 57
What is Part of Speech (PoS) tagging?

#### Answer 57:
The task of labelling each word in a sentence with its part of speech.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 58
What is the Markov Assumption?

#### Answer 58:
The assumption that the probability of a word depends only on the previous word.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 59
What can we use to model the underlying sequence of hidden states that produced our observations?

#### Answer 59:
Hidden Markov Models (HMMs).

#### *[This question was from Sequence Modelling]*
<hr>

### Question 60
What are the five components of an HMM?

#### Answer 60:
$S=s_1,s_2,\cdots,s_n$ is a set of states (parts of speech)

$A=a_{11},a_{12},\cdots,a_{N1},\cdots,a_{NN}$ is a transition probability matrix (between states)

$\pi=\pi_1,\pi_2,\cdots,\pi_n$ is an initial probability distribution over states 

$O=o_1,o_2,\cdots,o_T$ is a sequence of $T$ observations (words)

$B=b_i\left(o_t\right)$ is a sequence of observation likelihoods (emission probabilities), expressing the probability of an observation $o_t$ being generated from state $s_i$

#### *[This question was from Sequence Modelling]*
<hr>

### Question 61
What is Bayes' Theorem?

#### Answer 61:
$$
P\left(A\mid B\right) = \frac{P\left(B\mid A\right) P\left(A\right)}{P\left(B\right)}
$$

#### *[This question was from Sequence Modelling]*
<hr>

### Question 62
What is the output independence assumption?

#### Answer 62:
The assumption that the probability of an observation depends only on the state that produced it.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 63
The goal of decoding is to find the most likely sequence of hidden states that produced a sequence of observations. Derive the equation for the most likely sequence of hidden states $\hat{t}_{1:n}$ given a sequence of observations $w_{1:n}$.

#### Answer 63:
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

### Question 64
If we do not have a model for the transition probabilities and emission probabilities, what can we do to estimate these?

#### Answer 64:
By performing statistical analysis of our training data.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 65
What is the Viterbi algorithm?

#### Answer 65:
A dynamic programming algorithm for finding the most likely sequence of hidden states that produced a sequence of observations.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 66
What is the equation for the Viterbi algorithm at step `t` for previous state `i` and current state `j` given the observation `o_t` for the current state?

#### Answer 66:
$$
V_t\left(j\right)=\text{max}_{i=1}^N \; V_{t-1}\left(i\right)a_{ij}b_j\left(o_t\right)
$$

#### *[This question was from Sequence Modelling]*
<hr>

### Question 67
What are Noun Phrases (NPs)?

#### Answer 67:
A sequence of words that contain a noun and surrounding words, and can fulfil the function of a noun in a sentence.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 68
What is a constituent?

#### Answer 68:
A constituent is a sequence of words that can fulfil the function of a part of a sentence.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 69
In a constituent, what is the head and what are the dependents?

#### Answer 69:
The head is the main noun in the constituent, and the dependents are the surrounding words.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 70
What is syntactic constituency?

#### Answer 70:
The idea that groups of words can behave as single units or constituents.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 71
What is the subject of a sentence?

#### Answer 71:
The main participant of the action.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 72
What is the object of a sentence?

#### Answer 72:
The participant to whicht the action is applied.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 73
What is an indirect object?

#### Answer 73:
A participant of the action that is not the main participant.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 74
What is a Context Free Grammar (CFG) and what is it defined by?

#### Answer 74:
A CFG is a mathematical system for modelling constituent structure in a language.
It is defined by a set of non-terminal symbols, a set of terminal symbols (words), a set of production rules, and a start symbol.

#### *[This question was from Sequence Modelling]*
<hr>

### Question 75
What is parsing?

#### Answer 75:
The task of producing a tree structure that represents the syntactic structure of a sentence.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 76
What is chunking?

#### Answer 76:
The process of identifying and classifying non-overlapping segments of a sentence that constitute the basic non-recursive phrases corresponding to the major parts of speech (NPs, PPs, VPs, etc.)

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 77
What is bottom-up parsing?

#### Answer 77:
Bottom-up parsing starts from terminal symbols, assigns PoS categories and combines them into further constituents. 

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 78
What is an advantage and disadvantage of bottom-up parsing?

#### Answer 78:
While we only need to consider constituents compatible with the input, we need to keep track of all possible rules and subtrees even if they don’t result in S.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 79
What is top-down parsing?

#### Answer 79:
Top-down parsing starts from root non-terminal S and expands the tree downwards until the terminal words are reached. 

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 80
What is an advantage and disadvantage of top-down parsing?

#### Answer 80:
While we only need to consider rules compatible with a well-formed sentence rooted in S, we may consider rules along the way that do not lead to the input.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 81
What is the Early Parsing Algorithm?

#### Answer 81:
The Earley parsing algorithm tries to recursively apply rules until the root non-terminal is fully processed or there is no input remaining to process.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 82
What are the core components of the Early Parsing Algorithm and how do they work?

#### Answer 82:
It keeps track of the step ID, the rule for the grammar, the covered span of the sentence by this rule, rule IDs for sub-constituents and the ID of the word being processed. 

It has three stages: 
* The predictor considers the rules and tries to expand non-terminals waiting to be expanded (with a • to their left).
* The scanner considers any non-terminals waiting to be expanded which are consistent with the input sentence.
* The completer propagates fully explored non-terminals.

#### *[This question was from Syntactic Analysis]*
<hr>

### Question 83
What is dependency parsing and how does it relate to constituency parsing?

#### Answer 83:
The goal of dependency parsing is to establish directed binary grammatical relations that hold among words of the input:
* The root node explicitly marks the root of the construction
* The heads determine the nature of the expression
* Other words are dependents.
![alt text](image.png)

#### *[This question was from Lexical Semantics]*
<hr>

### Question 84
What is lexical semantics?

#### Answer 84:
A branch of linguistics and NLP that deals with word senses.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 85
What is WordNet?

#### Answer 85:
WordNet is the largest, most comprehensive and most widely used database of lexical relations.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 86
What does each word in WordNet have?

#### Answer 86:
A gloss (definition) and a synset (synonymy set).

#### *[This question was from Lexical Semantics]*
<hr>

### Question 87
What is a synset and how are they organised?

#### Answer 87:
A synset is a synonymy set. They are organised hierarchically (e.g. entity, physical entity, organism, animal, mammal, dog)

#### *[This question was from Lexical Semantics]*
<hr>

### Question 88
What is homonymy?

#### Answer 88:
Homonymy is the phenomenon where a single word has multiple meanings.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 89
What are homophones?

#### Answer 89:
Homophones are words that sound the same but have different meanings.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 90
What is a polysemy?

#### Answer 90:
A polysemy is a word that has multiple meanings.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 91
What is a synonym?

#### Answer 91:
A synonym is a word with the same or nearly the same meaning as another word.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 92
What is a hyponym?

#### Answer 92:
A hyponym is a word that is more specific than another word.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 93
What is a hypernym?

#### Answer 93:
A hypernym is a word that is more general than another word.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 94
What is metonymy?

#### Answer 94:
Metonymy is the use of a word to refer to something else that is closely associated with it.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 95
What is antonymy?

#### Answer 95:
Antonymy holds for words with opposite meaning. Though they might be close in meaning, they likely differ along a dimension.

#### *[This question was from Lexical Semantics]*
<hr>

### Question 96
What is entailment?

#### Answer 96:
Entailment states that what happens to hypernyms, happens to hyponyms (but not necessarily the other way around).

#### *[This question was from Lexical Semantics]*
<hr>

### Question 97
What is a semantic field?

#### Answer 97:
A semantic field is a set of words that are related to each other by some semantic relation.

#### *[This question was from Classification]*
<hr>

### Question 98
What is feature selection and feature weighting?

#### Answer 98:
Feature selection involves identifying the most informative among potential features (e.g. by removing stop words).
Feature weighting and normalisation involve weighting the most informative among remaining features heavier (e.g. using TF-IDF).

#### *[This question was from Classification]*
<hr>

### Question 99
Which equation is the Naive Bayes algorithm based on for classification?

#### Answer 99:
$$
P\left(class\middle| c o n t e n t\right)=\frac{P\left(content\middle| c l a s s\right)P\left(class\right)}{P\left(content\right)}
$$
where
* $P\left(class\middle| c o n t e n t\right)$ is the posterior probability
* $P\left(class\right)$ is the prior probability
* $P\left(content\middle| c l a s s\right)$ is the likelihood
* $P\left(content\right)$ is the probability of the data

#### *[This question was from Classification]*
<hr>

### Question 100
How can we apply Bayes' Theorem to a classification task
$
\hat{y}=\mathrm{argmax}_Y P\left(Y\middle| X\right)
$?

#### Answer 100:
$$
\hat{y}=\mathrm{argmax}_Y P\left(Y\middle| X\right)\\
=\mathrm{argmax}_Y\frac{P\left(X\middle| Y\right)P\left(Y\right)}{P\left(X\right)}\\
=\mathrm{argmax}_YP\left(X\middle| Y\right)P\left(Y\right)
$$
The maximum a posteriori (MAP) decision rule removes the denominator because the probability of the content is constant amongst the content

#### *[This question was from Classification]*
<hr>

### Question 101
What is the Naive assumption?

#### Answer 101:
The naïve (independence) assumption states that the occurrence of each feature given the class is independent of the occurrence of any other feature in the class.

#### *[This question was from Classification Metrics]*
<hr>

### Question 102
What is accuracy given by?

#### Answer 102:
$$
\text{accuracy}=\frac{\text{correct predictions}}{\text{total predictions}}
$$

#### *[This question was from Classification Metrics]*
<hr>

### Question 103
What is precision given by?

#### Answer 103:
$$
\text{precision}=\frac{\text{true positives}}{\text{predicted positives}}
$$

#### *[This question was from Classification Metrics]*
<hr>

### Question 104
What is recall given by?

#### Answer 104:
$$
\text{recall}=\frac{\text{true positives}}{\text{actual positives}}
$$

#### *[This question was from Classification Metrics]*
<hr>

### Question 105
What is F1 given by?

#### Answer 105:
The harmonic mean of precision and recall.
$$
\text{F1}=\frac{2\times\text{precision}\times\text{recall}}{\text{precision}+\text{recall}}
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 106
What are the three connotations carried by words and how can this be used for representation?

#### Answer 106:
* *Valence* is the pleasantness of the stimulus
* *Arousal* is the intensity of the emotion provoked by the stimulus
* *Dominance* is the degree of control exerted by the stimulus

This can be used for representation by using a three-dimensional vector to represent the word.

#### *[This question was from Word Embeddings]*
<hr>

### Question 107
What is distributional semantics and how can this be used for representation?

#### Answer 107:
Distributional semantics is a method of representing words in a way that captures their meaning based on the contexts in which they appear.

A word can be represented by a point vector in a multi-dimensional semantic space, where the word’s meaning is distributed amongst its neighbours according to their co-occurrence within a specified context window.

#### *[This question was from Word Embeddings]*
<hr>

### Question 108
What is the difference between sparse and dense vectors?

#### Answer 108:
Sparse vectors are based on the co-occurrence of words within a context window, whereas dense vectors are based on the distribution of words within a semantic space (i.e. embeddings).

#### *[This question was from Word Embeddings]*
<hr>

### Question 109
How can we represent a phrase using compositional semantics?

#### Answer 109:
Methods of compositional semantics allows us to derive the representation of a phrase by applying a function to the constituent word vectors, i.e. $p = f(u, v)$

#### *[This question was from Word Embeddings]*
<hr>

### Question 110
What is Pointwise Mutual Information (PMI) and what is the equation for it?

#### Answer 110:
Pointwise Mutual Information (PMI) is a measure of how often two events x and y occur (given some relation), compared to what we would expect if they were independent.
$$
\text{PMI}(w, c) = \log \frac{P(w, c)}{P(w)P(c)}
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 111
What is Positive PMI (PPMI)?

#### Answer 111:
Positive PMI (PPMI) is a variant of PMI that only considers the co-occurrence of words that occur together more than expected by chance.
$$
\text{PPMI}(w, c) = \max\left(0, \text{PMI}(w, c)\right)
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 112
What does word analogy mean and how can it be used for representation?

#### Answer 112:
Word analogy is the task of finding the relationship between two words, e.g. king is to queen as man is to woman.

This can be used for representation by using a word analogy task to learn a vector space model of word meaning.

#### *[This question was from Word Embeddings]*
<hr>

### Question 113
Which methods can we use to reduce the dimensionality of our vector space model?

#### Answer 113:
Principle Component Analysis (PCA) can be used with Singular Value Decomposition (SVD) to identify dimensions with the most variance, and therefore reduce the dimensionality of word representations. This is computationally expensive.

#### *[This question was from Word Embeddings]*
<hr>

### Question 114
What is the continuous skip-gram model?

#### Answer 114:
The continuous skip-gram model is a neural network model that learns word embeddings by predicting the context of a word in a sentence.

#### *[This question was from Word Embeddings]*
<hr>

### Question 115
Is the continuous skip-gram model supervised or unsupervised?

#### Answer 115:
The continuous skip-gram model is unsupervised (effectively self-supervised).

#### *[This question was from Word Embeddings]*
<hr>

### Question 116
Why is the continuous skip-gram model self-supervised?

#### Answer 116:
The target word $t$ and context word $c$ are treated as a positive example

The model randomly samples non-context words as a negative example

#### *[This question was from Word Embeddings]*
<hr>

### Question 117
How does the continuous skip-gram model learn word embeddings?

#### Answer 117:
A logistic regression classifier is trained to distinguish between them, generating a linear-regression-style way to produce probabilities calculated using the sigmoid of their dot product.

Learned weights are used as embeddings for target word $t$.

#### *[This question was from Word Embeddings]*
<hr>

### Question 118
How many embeddings are there in the continuous skip-gram model, and how do we find the single embedding for a word?

#### Answer 118:
There are two embeddings per word, as a target and as a context, and the final embedding is the sum of the two, i.e. $t_i=w_i+c_i$.

#### *[This question was from Word Embeddings]*
<hr>

### Question 119
What does the continuous skip-gram model use to calculate the probability of a positive example?

#### Answer 119:
The classifier calculates the probability that $c$ is a context word for $w$ as:
$$
P\left(+\middle| w,c\right)=\sigma\left(c\cdot w\right)=\frac{1}{e^{-c\cdot w}}
$$
$$
P\left(-\middle| c,w\right)=1-\sigma\left(c\cdot w\right)
$$
The trained weights therefore provide a linear regression-style way to produce these probabilities.

#### *[This question was from Word Embeddings]*
<hr>

### Question 120
How do we extend the probability function to a set of context words?

#### Answer 120:
$$P\left(+\middle| w,c_{1:L}\right)=\prod_{i=1}^{L}\sigma\left(-c_i\cdot w\right)$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 121
What is the loss function for the continuous skip-gram model?

#### Answer 121:
The goal of the model is to update the randomly initialised embeddings so that similarity in each $\left(w,c_{pos}\right)$ embedding is maximised and in $\left(w,c_{neg}\right)$ is minimised, using stochastic gradient descent.

The loss function $L_{CE}$ is used:
$$
L_{CE}=-\log{\left[P\left(+\middle| w,c_{pos}\right)+\prod_{i=1}^{k}{P\left(-\middle| w,c_{neg_i}\right)}\right]}
$$
$$
=\left[\sigma\left(c_{pos}\cdot w\right)+\sum_{i=1}^{k}log\left(1-P\left(+\middle| w,c_{neg_i}\right)\right)\right]
$$
$$
=\left[\sigma\left(c_{pos}\cdot w\right)+\sum_{i=1}^{k}log\left(\log{\sigma}\left(-c_{neg_i}\cdot w\right)\right)\right]
$$

#### *[This question was from Word Embeddings]*
<hr>

### Question 122
What are three advantages of dense word embeddings over sparse word embeddings?

#### Answer 122:
* Shorter vectors are easier to work with and learn weights for
* Smaller parameter space helps improve generalisation
* Dense vectors are better at capturing synonymy

#### *[This question was from Word Embeddings]*
<hr>

### Question 123
What is one advantage of sparse word embeddings over dense word embeddings?

#### Answer 123:
Sparse word embeddings are better at capturing polysemy.

#### *[This question was from Word Embeddings]*
<hr>

### Question 124
What is the paraphrasing task?

#### Answer 124:
The paraphrasing task tests whether one word/phrase can replace another word/phrase in a given context.

#### *[This question was from Word Embeddings]*
<hr>

### Question 125
What is the word analogy task?

#### Answer 125:
The analogy task solves the question of $a$ is to $b$ what $a^\ast$ is to what?
$$
b\ast={argmax}_xdistance\left(x,a^\ast-a+b\right)
$$

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 126
What are Recurrent Neural Networks (RNNs)?

#### Answer 126:
In Recurrent Neural Networks (RNNs) the input to a hidden layer h_t at time t is expanded with the value of the hidden layer from the preceding time step, h_{t-1}. 

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 127
How do the parameters in a Recurrent Neural Network (RNN) compare to those in a feedforward neural network?

#### Answer 127:
RNNs must learn an extra parameter, the matrix of weights for the previous hidden layer.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 128
When does the exploding gradient problem occur in RNNs?

#### Answer 128:
The exploding gradient problem occurs when the model focuses too much on the immediate context.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 129
When does the vanishing gradient problem occur in RNNs?

#### Answer 129:
The vanishing gradient problem occurs when the model ignores the immediate context.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 130
What are LSTMs?

#### Answer 130:
Long Short Term Memory (LSTM) networks are a type of RNN that use a memory cell to store information from previous time steps.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 131
What are Named Entities?

#### Answer 131:
Named entities are groups of words that can be referred to with a proper noun.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 132
What is Named Entity Recognition (NER)?

#### Answer 132:
Named Entity Recognition (NER) refers to labelling a sequence with its named entities.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 133
What are two schemes for NER, and what do they mark?

#### Answer 133:
* The BIO scheme marks the beginning (B), inside (I) and outside (O) tokens.
* The BIOES scheme also marks the end (E) tokens and single-token entities (S).

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 134
How can RNNs be used for NER and PoS?

#### Answer 134:
RNNs can be used to output a PoS or NER tag for each element in the input sequence.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 135
What can be used to learn a function to map global features of an input to a label?

#### Answer 135:
Linear Chain Conditional Random Fields (CRFs) learns a function $f$ that maps $K$ global features of an input $x$ to the output label $y$.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 136
Derive the equation for the output sequence $Y$ given the input sequence $X$ and the $K$ global features for a CRF.

Start with $Y=argmax_{Y\in\mathcal{Y}}P\left(Y\middle| X\right)$

#### Answer 136:
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

### Question 137
How can an RNN be used for classification?

#### Answer 137:
In an RNN, the final hidden state accumulates history from the whole sequence. Often, a further FNN with a SoftMax is applied to output a probability distribution over the class labels.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 138
What is machine translation?

#### Answer 138:
Machine Translation (MT) consists of translating a sentence $x$ from a source language to a sentence $y$ in a target language.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 139
What is neural machine translation?

#### Answer 139:
Neural Machine Translation (NMT) is MT using neural networks, which are end-to-end differentiable.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 140
What is the format of the input to an RNN?

#### Answer 140:
The input sentence is divided into pieces, with a preceding \<bos> and ending \<eos> tag.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 141
What is an encoding and how is it used in an RNN as input?

#### Answer 141:
An encoding is a representation of the input sentence as a sequence of vectors, that is a representation of an idea or thought that will contribute to generated output.

The encoding is used as the initial hidden state of the RNN.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 142
What is the encoder-decoder architecture?

#### Answer 142:
The encoder-decoder architecture is a neural network that consists of an encoder and a decoder.

The encoder reads the input sentence and produces an encoding.

The decoder reads the encoding and generates the output sentence.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 143
What do conditional language models maximise?

#### Answer 143:
Conditional language models maximise the probability of the output sentence given the source $x$.

$$
P\left(y\middle| x\right)=\prod_{i=1}^{n}P\left(y_i\middle| y_{<i},x\right)
$$

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 144
What does the decoder output vector at a point in time represent? How do we use this to generate the output?

#### Answer 144:
The decoder output at a point is the representation of the input sentence (which is input as chunks) up to that point, as well as the source context. It is then fed through a linear layer and SoftMax to produce a probability distribution over the vocabulary to sample the output from.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 145
Which type of loss function is used for training a Seq2Seq model?

#### Answer 145:
The cross-entropy loss function is used for training a Seq2Seq model. It is given by $-\log{P\left(correct\right)}$, where $p(correct)$ is the predicted probability of the correct output (that is, from the SoftMax output of the decoder).

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 146
At each step of the decoder, we need to take the `argmax` of the output distribution to get the next word. How do we do this efficiently, step-by-step?

#### Answer 146:
To take the `argmax` efficiently at each step of the decoder, we use a **beam search**:
* $k$ is the beam size (typically 5-10), which represents the ‘width’ of the search
* At each step, keep track of the $k$ most probable partial translations (hypotheses)
* Keep track of each hypothesis score, tracking the top $k$ scoring hypotheses
		$$score\left(y_1,\cdots,y_t\right)=log{P_{LM}}\left(y_1,\cdots,y_t\middle| x\right)=\sum_{i=1}^{t}{log{P_{LM}}\left(y_i\middle| y_{<i},x\right)}$$
* A hypothesis is complete when it produces <eos>.
* A beam search is complete when it reaches a predefined timestep $T$ or has a predefined $n$ completed hypotheses


#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 147
What is attention and what is it used for?

#### Answer 147:
Since it is hard to compress a sentence into an encoding, and different information may be relevant at different steps in the decoder, attention allows the decoder to focus on different parts of the input sentence at different times.

#### *[This question was from Recurrent Neural Networks]*
<hr>

### Question 148
How are attention scores calculated and applied?

#### Answer 148:
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

### Question 149
What two things does a transformer do that an RNN does not?

#### Answer 149:
* Parallel processing of sentence (faster pre-training, leading to better downstream performance)
* Lower computational complexity per layer 

#### *[This question was from Transformers]*
<hr>

### Question 150
What type of attention is used in the transformer and what is its equation?

#### Answer 150:
Self attention (scaled dot-product) is used 
$$
\text{Attention}\left(Q,K,V\right)=\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

#### *[This question was from Transformers]*
<hr>

### Question 151
What is masked self-attention and how is it used in the transformer?

#### Answer 151:
In the encoder, each token gathers context from other tokens to update its representation.
In the decoder, we mask future tokens in the inference stage (but not during training).

#### *[This question was from Transformers]*
<hr>

### Question 152
What is multi-head attention and how is it used in the transformer?

#### Answer 152:
Multiple (independent) heads concatenate their attention scores and a linear layer is applied to calculate the attention.

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 153
State and describe briefly two common evaluation metrics for machine translation models.

#### Answer 153:
* BLEU (based on n-gram precision)
* BERTScore (based on cosine similarity with contextual embeddings from a pre-trained BERT model)

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 154
When are automatic and manual evaluation methods used, and what are some common methods?

#### Answer 154:
Automatic metrics are used at development time, and manual evaluation is commonly used at test time. Automatic metrics include BLEU and BERTScore. Manual metrics include Likert scales, direct assessment and relative ranking.

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 155
What are two common problems with language models?

#### Answer 155:
* Bias due to only the most frequent data being stored.
* Hallucination by generating data that is not present in the training data.

#### *[This question was from Evaluation of Language Models]*
<hr>

### Question 156
What is perplexity and how is it calculated?

#### Answer 156:
Perplexity is a measure of how well a language model predicts a sequence of words. It is calculated as the inverse of the probability of the test sequence.
$$
PP\left(W\right)=\sqrt[N]{\frac{1}{P\left(w_1,w_2,\cdots,w_N\right)}}
$$

#### *[This question was from Variants of LLMs]*
<hr>

### Question 157
What are encoder-only models used for?

#### Answer 157:
Encoder-only architectures are used for classification (e.g. Bidirectional Encoder Representations from Transformers – BERT, RoBERTa).

#### *[This question was from Variants of LLMs]*
<hr>

### Question 158
What are decoder-only models used for?

#### Answer 158:
Decoder-only architectures are used for generation (e.g. Generative Pre-Trained Transformer – GPT).

#### *[This question was from Variants of LLMs]*
<hr>

### Question 159
What is emergence and when does it occur?

#### Answer 159:
Emergence is when quantitative changes in a system result in qualitative changes in behaviour.
As the size of a model and training data size increase, the performance of the model increases at a phase transition. At about 10bn parameters, it becomes able to solve problems it could not solve before, e.g. modular arithmetic.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 160
What is Retrieval Augmented Generation (RAG)?

#### Answer 160:
Retrieval Augmented Generation (RAG) is a method of generating text by retrieving relevant information from a knowledge base, splitting them into chunks, encoding as vectors, retrieving the top k chunks based on semantic similarity and using this additional context to generate the output.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 161
What is in-context learning?

#### Answer 161:
In-context learning is a method of learning from a small number of examples by providing the model with a set of examples and then asking it to predict the output for a new example.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 162
What is chain of thought prompting?

#### Answer 162:
Chain of thought prompting encourages models to generate a rationale, increasing the likelihood of a correct answer (this is in-context learning).

#### *[This question was from Variants of LLMs]*
<hr>

### Question 163
What is self-consistency?

#### Answer 163:
Self-consistency involves sampling a diverse range of reasoning paths and taking the most probable path to aggregate the final answer.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 164
What is least-to-most prompting?

#### Answer 164:
Least-to-most prompting (problem decomposition) involves decomposing a question into sub-questions, solving the sub-questions (with access to the previous answer as context) and producing a final answer.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 165
What is problem decomposition?

#### Answer 165:
The same as least-to-most prompting.
Least-to-most prompting (problem decomposition) involves decomposing a question into sub-questions, solving the sub-questions (with access to the previous answer as context) and producing a final answer.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 166
What is program of thought prompting?

#### Answer 166:
Program of thought prompting involves generating a computer program to compute the answer to a complex problem.

#### *[This question was from Variants of LLMs]*
<hr>

### Question 167
What are four things that make up a good prompt?

#### Answer 167:
* Premise (context)
* Hypothesis (question)
* Reasoning example (how to solve the problem)
* Answer options (the possible solutions)

#### *[This question was from Variants of LLMs]*
<hr>

### Question 168
What are five common methods of improving LLM behaviour?

#### Answer 168:
* Retrieval Augmented Generation (RAG)
* Chain of thought prompting
* Self-consistency
* Least-to-most prompting
* Program of thought prompting

#### *[This question was from Variants of LLMs]*
<hr>

