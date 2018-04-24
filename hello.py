#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:41:52 2018

@author: cholhyunpark, Dempsey Salazar
"""

# hello.py
import json
from flask import Flask
app = Flask(__name__)
users = list()


@app.route("/hello/<name>")
def hello(name):
    users.append(name)
    
    data = {}
    data['connected'] = True
    data['users'] = users
    json_data = json.dumps(data)
    
    return json_data



app.run(host='10.124.2.119', port=5000, debug=False) 
