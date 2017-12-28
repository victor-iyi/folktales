r"""Test file.
"""
import os.path
import re
import nltk
from nltk.tokenize import PunktSentenceTokenizer


def load_corpus(file, path='./datasets'):
    """
    Load corpus from the datasets directory
    :param file: Name of the file to be loaded
    :param path: Directory the file is located. It's `datasets/` by default
    :return: list of tokenized sentences
    """
    filename = os.path.join(path, file)
    corpus = nltk.load(filename)
    tokenizer = PunktSentenceTokenizer()
    sent_tokens = tokenizer.tokenize(corpus)
    return sent_tokens


def tag(sent):
    """
    Part of speech tagging for a given sentence
    :param sent: the sentence you wanna tag.
    :return: part of speech tags
    """
    words = nltk.word_tokenize(sent)
    return nltk.pos_tag(words)


def start():
    """
    Start program execution
    """
    actors = set()
    tokens = load_corpus('Olailo.txt')
    for sent in tokens[:6]:
        tagged = tag(sent)
        ne_bin = nltk.ne_chunk(tagged, binary=True)
        # ne = nltk.ne_chunk(tagged, binary=False)
        acts = re.findall(r'\(NE\s(.*?)/NNP', str(ne_bin))
        nos = len(acts)
        if nos > 0:
            for act in acts:
                actors.add(act)
    print(actors)


if __name__ == '__main__':
    start()
