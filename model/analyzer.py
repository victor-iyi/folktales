import os.path
import re

import nltk

from model.utils import *


def main():
    """Start program execution."""
    pass


def characters(entities):
    matches = re.findall(r'\(PERSON\s(.*?)\/NNP\)', str(entities))
    return set(matches)


def songs(story: str):
    return []


def lessons(story: str):
    return []


def locations(entities):
    matches = re.findall(r'\(GPE\s(.*?)\/NNP\)', str(entities))
    return set(matches)


def proverbs(tagged):
    return []


def analyze(story):
    token = nltk.word_tokenize(story)
    tagged = nltk.pos_tag(token)

    entities = nltk.ne_chunk(tagged, binary=False)
    print(type(entities))

    # Analysis results.
    results = {
        'characters': characters(entities),
        'locations': locations(entities), 'songs': songs(story),
        'proverbs': proverbs(tagged), 'lessons': lessons(story),
    }

    return results


if __name__ == '__main__':
    main()
