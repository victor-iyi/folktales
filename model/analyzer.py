import re

import nltk


def characters(tagged):
    """Retrieve all the main characters in the story."""
    entities = nltk.ne_chunk(tagged, binary=True)
    matches = re.findall(r'\(NE\s(\w*)/NNP', str(entities))
    return list(sorted(set(matches)))


def songs(story: str):
    """Get the songs in this story."""
    stories = story.split('\n')
    _songs = []
    prev_empty = True
    for st in stories:
        song = re.findall(r'(\w*?:)\s(.*?)', str(st))
        if len(song) > 0:
            if prev_empty:
                _songs.append([st])
            else:
                _songs[-1].append(st)  # += '\n{}'.format(st)

            prev_empty = False
        else:
            prev_empty = True

        # _songs.append(' '.join(song))
    return _songs


def lessons(story: str):
    """Get all moral lessons in the story."""
    return []


def locations(tagged):
    """Get locations in the story."""
    entities = nltk.ne_chunk(tagged, binary=False)
    matches = re.findall(r'\(GPE\s(\w*?)\/NN.+\)', str(entities))
    return list(sorted(set(matches)))


def proverbs(tagged):
    return []


def analyze(story: str):
    """Analyze a given story.

    Args:
        story (str): Story to be analyzed.

    Returns:
        dict - Containing analysis of characters, locations,
            songs, provers and moral lessons.
    """

    token = nltk.word_tokenize(story)
    tagged = nltk.pos_tag(token)

    # Analysis results.
    results = {
        'characters': characters(tagged),
        'locations': locations(tagged), 'songs': songs(story),
        'proverbs': proverbs(tagged), 'lessons': lessons(story),
    }

    return results
