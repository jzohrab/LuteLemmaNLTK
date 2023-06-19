import sys
import os
import nltk

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize, pos_tag
from collections import defaultdict


def generate_import(text):
    # POS tagger returns strings like "VBN" that need to be mapped to
    # things that the lemmatizer understands.
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV

    tokenization = nltk.word_tokenize(text)
    lmtzr = WordNetLemmatizer()
    lemma_tokens = [
        [ lmtzr.lemmatize(token, tag_map[tag[0]]), token ]
        for token, tag
        in nltk.pos_tag(tokenization)
    ]
    lemma_tokens = [ t for t in lemma_tokens if t[0] != t[1] ]

    def len_then_string(p):
        s = p[0]
        n = len(s)
        key = f'{n:03}_' + s
        return key

    sortedbylenthenstring = sorted(
        lemma_tokens,
        key = lambda x: len_then_string(x)
    )
    
    return sortedbylenthenstring


ARGS=sys.argv
if (len(ARGS) != 3):
    print("Need infile, outfile")
    sys.exit(1)

infile = ARGS[1]
outfile = ARGS[2]

if (not os.path.exists(infile)):
    print(f"Missing input file {infile}")
    sys.exit(1)

text = ""
with open(infile, 'r') as reader:
    text = reader.read()

pairs = generate_import(text)

with open(outfile, 'w') as writer:
    for lemma, child in pairs:
        writer.write(f"{lemma}\t{child}\n")
    writer.flush()


print(f"\nFile generated: {outfile}")
print("\nPlease remove any mappings you don't want from this file before importing it.")

