# Grammar English
## Description
Old English or Anglo-Saxon, was a deeply Germanic language brought by the tribes who began to migrate to the British Isles from Germany in the 5th century AD. Old 
English still retains some short words that we recognize today (him; he – and their derivatives), but the construction of more complex phrases and vocabulary 
requires greater attention.

## Model

A grammar program is a computational implementation of a formal grammar. Formal grammar provides rules for generating all valid strings of a specific formal 
language. In the context of computing theory, a grammar program is essentially a parser that can take an input string and determine whether that string is valid 
according to the rules of the grammar.

Some rules of the English grammar are represented in this grammar, at the followings points i'm going to explain that rules in the parts of my grammar. 
```
    S -> NP VP

    NP -> Det N | Det Adj N | Det N PP | Det Adj N PP

    VP -> V NP | V Adv | V Adv PP | Adv V NP | Adv V

    PP -> P NP

    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'mouse' | 'table' | 'house'
    V -> 'chases' | 'sees' | 'finds'
    Adj -> 'happy' | 'small' | 'red' | 'big'
    Adv -> 'quickly' | 'silently'
    P -> 'on' | 'in' | 'under' | 'beside' | 'above'
```
All starts with S, that represents any sentences. In English we have two posibilities to write a subject and a verb.
``` 
    S -> NP VP
```
Each subject should start with an article and be followed by a noun that can be or not described by an adjective and can be followed or not with a peoposition, 
every verb can be started or followed with an adverb and they can end with a preposition or a subject. The preposition should be followed with a subject.
```
    NP -> Det N | Det Adj N | Det N PP | Det Adj N PP
    VP -> V NP | V Adv | V Adv PP | Adv V NP | Adv V

    PP -> P NP
```
Finally to represent each word into the grammar we have to construct them in each rule. 
```
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'mouse' | 'table' | 'house'
    V -> 'chases' | 'sees' | 'finds'
    Adj -> 'happy' | 'small' | 'red' | 'big'
    Adv -> 'quickly' | 'silently'
    P -> 'on' | 'in' | 'under' | 'beside' | 'above'
```
## Implementation
To do the implementation of my grammar and to be sure that what i do is correct i use the library of python "nltk" to create a tree of how is constructed each sentence. I also put a .txt file with correct sentences. 
## Test
Here are some test that i tried with my python program

Parsing: 'the happy dog chases the cat under the table'
```

                      S                         
       _______________|___                       
      |                   VP                    
      |          _________|____                  
      |         |              NP               
      |         |      ________|____             
      |         |     |   |         PP          
      |         |     |   |     ____|___         
      NP        |     |   |    |        NP      
  ____|____     |     |   |    |     ___|____    
Det  Adj   N    V    Det  N    P   Det       N  
 |    |    |    |     |   |    |    |        |   
the happy dog chases the cat under the     table
```

Parsing: 'the cat chases the mouse'
```
              S                 
      ________|_____             
     |              VP          
     |         _____|___         
     NP       |         NP      
  ___|___     |      ___|____    
Det      N    V    Det       N  
 |       |    |     |        |   
the     cat chases the     mouse
```

Parsing: 'a dog sees the table'

```
             S                
      _______|____             
     |            VP          
     |        ____|___         
     NP      |        NP      
  ___|___    |     ___|____    
Det      N   V   Det       N  
 |       |   |    |        |   
 a      dog sees the     table
```

Examples of incorrect sentences:
- the dog the finds house
- the table sees sees the dog
- the the dog chases mouse

## Analysis

### Time Complexity
The time complexity of a parser algorithm depends largely on the structure of the grammar and the approach used to perform the parsing.

In the case of the parser we have used, nltk's RecursiveDescentParser, time complexity is generally measured in terms of the length of the input (the length 
of the sentence being parsed) and the complexity of the grammar.

The time complexity of a parse is typically linear in the length of the input, that is, O(n), where n is the length of 
the input string. This is because at each step of the analysis, the parser steps through the input tokens and makes a decision based solely on the current non-
terminal symbol and the current input token.

### Why should you use a grammar over traditional programming
This parser is at the highest level of Chomsky's hierarchy, known as type 0 grammars or recursively enumerable grammars. These grammars can generate any language 
that can be recognized by a Turing machine, meaning they can represent the syntactic structure of extremely complex and expressive languages. For this reason, it 
is better to use this type of programming compared to traditional programming which can be more confusing and time-consuming.

## References

Guide to the parser. (s. f.). Python Developer’s Guide. https://devguide.python.org/internals/parser/index.html

Fitch, W. T. (2014). Toward a computational framework for cognitive biology: Unifying approaches from cognitive neuroscience and comparative cognition. Physics Of 
Life Reviews, 11(3), 329-364. https://doi.org/10.1016/j.plrev.2014.04.005
