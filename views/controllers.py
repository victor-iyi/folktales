"""
  @author Victor I. Afolabi

  A.I. Engineer & Software developer
  javafolabi@gmail.com

  Created on 25 January, 2018 @ 8:26 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from model import utils, analyzer
from views import app


@app.route('/')
def index():
    stories = utils.get_stories(count=5)
    return render_template('index.html', stories=stories)


@app.route('/analysis/<title>')
def analysis(title=None):
    story = utils.get_story_from_title(title)
    story_str = '\n'.join(story['body'])
    results = analyzer.analyze(story_str)
    print(results)

    return render_template('analysis.html', story=story, results=results)


@app.route('/stories/')
def stories():
    stories = utils.get_stories()
    return render_template('stories.html', stories=stories)


@app.route('/contact-us/')
def contact():
    return render_template('contact.html')
