# Lute Lemma NLTK

A simple python 3.11 script to generate child-parent lemma mappings for import into [Lute](https://github.com/jzohrab/lute), using NLTK.

> _This may only work for English, I'm not sure ... this is a work-in-progress to explore lemmatization for Lute._


## Requirements

* python3.11 (perhaps will work with earlier versions, untested)

## Installation

Use pip3.11:

```
$ python3.11 -m venv .env
$ source .env/bin/activate
$ pip3.11 install -r requirements.txt
$ deactivate
```

Then, get the necessary data files, following notes at https://www.nltk.org/data.html#interactive-installer.  Eg, for English:


```
$ python3.11

>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> nltk.download('popular')
```

# Usage

Put the full text you wish to lemmatize in a file, and then call main.  e.g., using the demo file:

```
$ source .env/bin/activate
$ python3.11 main.py demo/en_input.txt en_output.txt
$ deactivate
```

This will generate the file of parent-child mappings for the words in the demo text:

```
go	gone
take	took
thing	things
write	wrote
friend	friends
report	reports
```

Note again that this program uses a _full text_ for lemmatization, because it uses tagging to determine the function of each word as it lemmatizes.

# Refs

- https://www.nltk.org/data.html