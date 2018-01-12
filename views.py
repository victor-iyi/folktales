"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 December, 2017 @ 12:24 AM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from flask import Flask, render_template, redirect, url_for, request, abort

from helpers.consts import APP_NAME
from model import data

app = Flask(APP_NAME)


@app.route('/')
def index():
    stories = data.get_stories()
    titles = data.get_data_titles()
    return render_template('index.html', stories=stories, titles=titles)


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


@app.route('/newsletter/', methods=['POST'])
def newsletter():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return abort(405)
