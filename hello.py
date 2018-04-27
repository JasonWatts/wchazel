#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:41:52 2018

@author: cholhyunpark, Dempsey Salazar
"""
#check client code for requests library for ring function
# hello.py
import json
from flask import Flask
app = Flask(__name__)
users = list()
temp_ip = ""
temp_port = ""

@app.route("/hello/<name>")
def hello(name):
   
    data = {}
    
    if name == "kclu":
        data['connected'] = False
        data['users'] = "Sorry kclu is a reserved name"
        json_data = json.dumps(data)
        return json_data
    
    
    data['connected'] = True
    data['users'] = users
    
    
    users.append(name)
    json_data = json.dumps(data)
    return json_data


@app.route("/find")
def find():
    data = {}
    data['users'] = users
    json_data = json.dumps(data)
    return json_data

@app.route("/call/kclu")
def callKCLU():
    ##return the kclu IP
    return 0
    


@app.route("/call/<name>/<IP>/<port>")
def call(name):
    data = {}
    if name in users:
        
        
        data['request_recieved'] = True
        json_data = json.dumps(data)
        ring(name)
        temp_ip == IP
        temp_port == port
        return json_data
    else:
        data['request_recieved'] = False
        json_data = json.dumps(data)
        return json_data
def ring(person):
    ##send them a ring with the user 
    return 0


@app.route("/accept/<name>")
def accept(name):
    data = {}
    data['IP'] = temp_ip
    data['PORT'] = temp_port
    json_data = json.dumps(data)
    
    return json_data
    

@app.route("/drop/<name>")
def drop(name):
    data = {}
    data['drop'] = "api doesnt specify what to return"
    json_data = json.dumps(data)
    #send the user drop message (this was not spceified in api)
    return json_data

@app.route("/goodbye/<name>")
def goodbye(name):
    data = {}
    users.remove(name)
    data['connected'] = False
    data['users'] = users
    json_data = json.dumps(data)
    
    
    return json_data

        
        
        
        


app.run(host='10.124.2.119', port=5000, debug=False) 
