"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 31 December, 2017 @ 7:36 PM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
import os

from helpers import config as cfg


def get_title():
    files = [os.path.basename(f).split('.')[0]
             for f in os.listdir(cfg.DATASET_DIR)
             if f[0] != '.']
    return files
