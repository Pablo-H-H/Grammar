# Grammar English
## Description
in this evidence i have to create a grammar that represents the lenguage English, make a model of that grammar, do the implementation, test it and realize the complexity analysis

Old English or Anglo-Saxon, was a deeply Germanic language brought by the tribes who began to migrate to the British Isles from Germany in the 5th century AD. Old English still retains some short words that we recognize today (him; he – and their derivatives), but the construction of more complex phrases and vocabulary requires greater attention.

## Model
Some rules of the English grammar are represented in this grammar, at the followings points i'm going to explain that rules in the parts of my grammar. 
```
   S -> UNP UVP
                         
    UNP -> Det N | Det N PP
    UVP -> V NP | V PP

    NP -> Det N | Det N PP

    PP -> P NP
    
    
    Det -> 'the' | 'a' | 'an'

    N -> 'man' | 'student' | 'teacher' | 'homework' | 'dog' | 'school'
    P -> 'in' | 'with' | 'past' | 'above'
    V -> 'saw' | 'ate' | 'walked' | 'figthed' | 'scored'
```
All starts with S, that represents any sentences. In English we have two posibilities to write an article and a verb.
``` 
    S -> UNP UVP
                         
    UNP -> Det N | Det N PP
    UVP -> V NP | V PP
```
Each article should be followed by a noun and every verb should be followed by an article or a preposition.
```
    UNP -> Det N | Det N PP
    UVP -> V NP | V PP

    NP -> Det N | Det N PP

    PP -> P NP
```
Finally to represent each word into the grammar we have to construct them in each rule. 
```
    Det -> 'the' | 'a' | 'an'

    N -> 'man' | 'student' | 'teacher' | 'homework' | 'dog' | 'school'
    P -> 'in' | 'with' | 'past' | 'above'
    V -> 'saw' | 'ate' | 'walked' | 'figthed' | 'scored'
```
## Implementation
To do the implementation of my grammar and to be sure that what i do is correct i use the library of python "nltk" to create a tree of how is constructed each sentence. I also put a .txt file with a lot of correct sentences. 
## Test
Here are some test that i tried with my python program
"the teacher scored the homework"
```
                        S                             
      __________________|_____                         
     |                       UVP                      
     |             ___________|______                  
     |            |                  NP               
     |            |      ____________|___              
     |            |     |     |          PP           
     |            |     |     |       ___|___          
    UNP           |     |     |      |       NP       
  ___|_____       |     |     |      |    ___|____     
Det        N      V    Det    N      P  Det       N   
 |         |      |     |     |      |   |        |    
the     teacher scored the homework  in the     school
```
"the dog ate the homework"
```
             S                  
      _______|___                
     |          UVP             
     |        ___|___            
    UNP      |       NP         
  ___|___    |    ___|_____      
Det      N   V  Det        N    
 |       |   |   |         |     
the     dog ate the     homework
```

"the teache saw the dog in the school"

```
                     S                        
      _______________|___                      
     |                  UVP                   
     |            _______|___                  
     |           |           NP               
     |           |    _______|___              
     |           |   |   |       PP           
     |           |   |   |    ___|___          
    UNP          |   |   |   |       NP       
  ___|_____      |   |   |   |    ___|____     
Det        N     V  Det  N   P  Det       N   
 |         |     |   |   |   |   |        |    
the     teacher saw the dog  in the     school
```

Examples of incorrect sentences:
- the dog the saw school
- the school saw saw the dog
- the the dog saw the homework

## Analysis

This type of grammar falls within the third tier of the Extended Chomsky Hierarchy. This tier encompasses regular grammars, which are capable of generating regular languages such as Esperanto. Due to its recursive nature, this grammar cannot fit into any lower tier, as it does not meet the criteria for a context-free grammar, which is the second tier.
