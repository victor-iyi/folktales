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


def get_stories(count=5):
    stories = {}
    for file in get_files()[:count]:
        story = get_story(file)
        title = story['title']
        body = story['body']
        stories[title] = body
    return stories


def get_story(file):
    story = {
        'title': get_single_title(file)
    }
    with open(file, mode='r', encoding='utf-8') as f:
        body = f.readlines()
        body = [line.strip() for line in body if len(line.strip()) > 1]
        story['body'] = body
    return story
