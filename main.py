import sys
import os
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()



def generate_import(lines, writer):
    text = " ".join(lines)
    tokenization = nltk.word_tokenize(text)
    for w in tokenization:
        print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w))) 


ARGS=sys.argv
if (len(ARGS) != 3):
    print("Need infile, outfile")
    sys.exit(1)

infile = ARGS[1]
outfile = ARGS[2]

if (not os.path.exists(infile)):
    print(f"Missing input file {infile}")
    sys.exit(1)

lines = []
with open(infile, 'r') as reader:
    lines = reader.readlines()

with open(outfile, 'w') as writer:
    generate_import(lines, writer)

print(f"\nFile generated: {outfile}")
print("\nPlease remove any mappings you don't want from this file before importing it.")

