"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 December, 2017 @ 12:24 AM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from flask import Flask, render_template, redirect, url_for, request, abort

from helpers.consts import APP_NAME
from model import pre_processing

app = Flask(APP_NAME)


@app.route('/')
def index():
    stories = pre_processing.get_stories(count=5)
    return render_template('index.html', stories=stories)


@app.route('/analysis/<title>')
def analysis(title=None):
    story = pre_processing.get_story_from_title(title)
    return render_template('analysis.html', story=story)


@app.route('/stories/')
def stories():
    stories = pre_processing.get_stories()
    return render_template('stories.html', stories=stories)


@app.route('/newsletter/', methods=['POST'])
def newsletter():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return abort(405)


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('contact.html')
