"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 December, 2017 @ 12:24 AM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from flask import Flask, render_template

from helpers import config as cfg
from model import data
app = Flask(cfg.APP_NAME)


@app.route('/')
def index():
    story_title = data.get_title()
    return render_template('index.html', story_title=story_title)


@app.route('/left-sidebar/')
def left_sidebar():
    return render_template('left-sidebar.html')


@app.route('/right-sidebar/')
def right_sidebar():
    return render_template('right-sidebar.html')


@app.route('/no-sidebar/')
def no_sidebar():
    return render_template('no-sidebar.html')


@app.route('/elements/')
def elements():
    return render_template('elements.html')
