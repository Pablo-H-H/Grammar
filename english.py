import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""
    S -> UNP UVP
                         
    UNP -> Det N | Det N PP
    UVP -> V NP | VP PP
    NP -> Det N | Det N PP

    PP -> P NP
    
    
    Det -> 'the' | 'a' | 'an'

    N -> 'man' | 'student' | 'teacher' | 'homework' | 'dog' | 'school'
    P -> 'in' | 'with' | 'past' | 'above'
    V -> 'saw' | 'ate' | 'walked' | 'figthed' | 'scored'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = "the teacher scored the homework in the school"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()