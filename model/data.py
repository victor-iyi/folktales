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
    files = (os.path.join(cfg.DATASET_DIR, f)
             for f in os.listdir(cfg.DATASET_DIR)
             if f[0] != '.')
    return files


def get_stories():
    stories = {}
    for file in get_files():
        title = get_single_title(file)
        with open(file, mode='rb') as f:
            story = f.readlines()
            stories[title] = story
    return stories
