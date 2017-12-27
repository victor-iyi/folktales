"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  
  Created on 27 December, 2017 @ 12:24 AM.
  
  Copyright © 2017. Victor. All rights reserved.
"""
from flask import Flask, render_template

from helpers.config import *

app = Flask(APP_NAME)

@app.route('/')
def index():
    return render_template('index.html')
