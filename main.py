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

tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

def generate_import(text):
    tokenization = nltk.word_tokenize(text)
    lmtzr = WordNetLemmatizer()
    lemma_tokens = [
        [ lmtzr.lemmatize(token, tag_map[tag[0]]), token ]
        for token, tag
        in nltk.pos_tag(tokenization)
    ]
    for lemma, token in lemma_tokens:
        print(lemma, "=>", token)


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
generate_import(text)


sys.exit(0)

with open(outfile, 'w') as writer:
    generate_import(lines, writer)

print(f"\nFile generated: {outfile}")
print("\nPlease remove any mappings you don't want from this file before importing it.")

