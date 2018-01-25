"""
  @author Victor I. Afolabi
  A.I. Engineer & Software developer
  javafolabi@gmail.com
  Created on 25 January, 2018 @ 8:25 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import Flask

from helpers.consts import APP_NAME

app = Flask(APP_NAME)

from views.controllers import *
from views.forms import *
