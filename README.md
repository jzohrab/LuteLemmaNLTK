# Lute Lemma NLTK

A simple python 3.11 script to generate child-parent lemma mappings for import into [Lute](https://github.com/jzohrab/lute), using NLTK.


## Requirements

* python3.11 (perhaps will work with earlier versions, untested)

## Installation

Use pip3.11:

```
$ python3.11 -m venv .env
$ source .env/bin/activate
$ pip3.11 install -r requirements.txt
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


# Refs

- https://www.nltk.org/data.html