#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:31:52 2018

@author: cholhyunpark
"""

from flask import request


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello, name please'

@app.route('/find')
def api_find():
    
    numOfuser = request.args.length
    
    if 'name' in request.args:
        for i in range(0, numOfuser):
            return request.arg[i]
    else :
        return "I can't find user"

@app.route('/call/target')
def api_target():
    