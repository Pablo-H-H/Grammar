import nltk
from nltk import CFG
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# Definir la gramática simplificada
grammar = CFG.fromstring("""
    S -> NP VP

    NP -> Det N | Det Adj N | Det N PP | Det Adj N PP

    VP -> V NP | V NP | V Adv | V Adv PP | Adv V NP | Adv V

    PP -> P NP

    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'mouse' | 'table' | 'house'
    V -> 'chases' | 'sees' | 'finds'
    Adj -> 'happy' | 'small' | 'red' | 'big'
    Adv -> 'quickly' | 'silently'
    P -> 'on' | 'in' | 'under' | 'beside' | 'above'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)


# Input sentences to be parsed
simple_sentences = [
    "the happy dog chases the cat under the table",
    "the cat chases the mouse",
    "a dog sees the table",
    "the big dog quickly finds the cat",
    "the mouse under the table silently sees the dog",
    "the cat on the table chases the mouse"
]

# Parse the sentence and print the trees
for sentence in simple_sentences:
    print(f"\nParsing: '{sentence}'")
    
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    parsed_trees = list(parser.parse(tokens))
    
    if not parsed_trees:
        print("No valid parse trees found.")
    else:
        for tree in parsed_trees:
            tree.pretty_print()
