"""
  @author Victor I. Afolabi

  A.I. Engineer & Software developer
  javafolabi@gmail.com

  Created on 25 January, 2018 @ 8:28 PM.
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import request, redirect, url_for

from views import app


@app.route('/_newsletter', methods=['POST'])
def form_newsletter():
    email = request.form['email']
    print(email)
    return redirect(url_for('index'))


@app.route('/_contact', methods=['POST'])
def form_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(name, email, message)
    return redirect(url_for('index'))
