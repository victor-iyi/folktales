import os.path
import re

import nltk

from model.utils import *


def main():
    """Start program execution."""
    pass


def characters(tagged):
    entities = nltk.ne_chunk(tagged, binary=True)
    matches = re.findall(r'\(NE\s(\w*)/NNP', str(entities))
    return set(matches)


def songs(story: str):
    return []


def lessons(story: str):
    return []


def locations(tagged):
    entities = nltk.ne_chunk(tagged, binary=False)
    matches = re.findall(r'\(GPE\s(\w*?)\/NNP\)', str(entities))
    return set(matches)


def proverbs(tagged):
    return []


def analyze(story):
    token = nltk.word_tokenize(story)
    tagged = nltk.pos_tag(token)

    # Analysis results.
    results = {
        'characters': characters(tagged),
        'locations': locations(tagged), 'songs': songs(story),
        'proverbs': proverbs(tagged), 'lessons': lessons(story),
    }

    return results


if __name__ == '__main__':
    main()
