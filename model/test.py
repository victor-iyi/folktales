import os.path
import re
import spacy


def main():
    """Start program execution."""
    nlp = spacy.load('en_coref_md')
    doc = nlp(u'My sister has a friend called John. She loves him')
    print(doc._.coref_clusters)


if __name__ == '__main__':
    main()
