"""
  @author Victor I. Afolabi
  
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 31 December, 2017 @ 7:36 PM.
  Copyright © 2017. Victor. All rights reserved.
"""
import os

from helpers import consts as cfg


def get_data_titles():
    return [get_single_title(f) for f in get_files()]


def get_single_title(file):
    return os.path.basename(file).split('.')[0]


def get_files():
    files = [os.path.join(cfg.DATASET_DIR, f)
             for f in os.listdir(cfg.DATASET_DIR)
             if f[0] != '.']
    return files


def get_stories(count=None):
    """
    Retrieves dataset stories.

    :param count: int
        Number of stories to get.

    :return: stories, dict
         A dictionary containing story titles (key)
         and story body (value)
    """
    stories = {}

    # Limit the number of files to retrieve.
    files = get_files()[:count] if count else get_files()

    for file in files:
        story = get_story_from_file(file)
        title = story['title']
        body = story['body']
        stories[title] = body
    return stories


def get_story_from_file(file):
    """
    Retrieve a single story.

    :param file: str
        Story file location
    :return: story, dict
        Returns a dictionary => {title: body}
    """
    story = {'title': get_single_title(file)}
    with open(file, mode='r', encoding='utf-8') as f:
        body = f.readlines()
        body = [line.strip() for line in body if len(line.strip()) > 1]
        story['body'] = body
    return story


def get_story_file(title):
    """
    Retrieves the file for a story title

    :param title: str
        Story title.
    :return: str
        Story filename.
    """
    files = get_files()
    for file in files:
        if get_single_title(file).lower() == title.lower():
            return file
    return None


def get_story_from_title(title):
    file = get_story_file(title)
    return get_story_from_file(file)
