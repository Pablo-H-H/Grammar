# Grammar English
## Description
in this evidence i have to create a grammar that represents the lenguage English, make a model of that grammar, do the implementation, test it and realize the complexity analysis

Old English or Anglo-Saxon, was a deeply Germanic language brought by the tribes who began to migrate to the British Isles from Germany in the 5th century AD. Old English still retains some short words that we recognize today (him; he – and their derivatives), but the construction of more complex phrases and vocabulary requires greater attention.

## Model
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
Each article should be followed by a noun and every verb should be followed by an article or a preposition.
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
To do the implementation of my grammar and to be sure that what i do is correct i use the library of python "nltk" to create a tree of how is constructed each sentence. I also put a .txt file with a lot of correct sentences. 
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

This type of grammar falls within the third tier of the Extended Chomsky Hierarchy. This tier 
encompasses regular grammars, which are capable of generating regular languages such as 
Esperanto. Due to its recursive nature, this grammar cannot fit into any lower tier, as it 
does not meet the criteria for a context-free grammar, which is the second tier.

