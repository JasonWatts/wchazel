#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:58:05 2018

@author: cholhyunpark
"""

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'root directory'

@app.route('/hello')
def api_hello():
    return url_for('api_hello')

@app.route('/hello/name')
def api_hello(name):
    return name

@app.route('/find')
def api_find():
    return url_for('api_find')

@app.route('/call')
def api_call():
    return url_for('api_call')

@app.route('/call/target')
def api_call(target):
    return target

@app.route('/drop')
def api_drop():
    return url_for('drop')

@app.route('/goodbye')
def api_goodbye():
    return url_for('goodbye')

if __name__ == '__main__':
    app.run()
    
    
