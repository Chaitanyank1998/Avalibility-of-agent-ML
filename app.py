# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 13:42:43 2020

@author: Chaitanya Kholapure
"""
from flask import Flask, jsonify, request, render_template, Markup, json, session, redirect, url_for
import pandas as pd 
import numpy as np 
from sklearn.externals import joblib

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/',methods=["GET","POST"])
def predict():
    Encode_role = {'spanish speaker': 1,'sales': 0,'support': 2}
    clf = joblib.load("model.pkl")
    if request.method == "POST":
        role = request.form['role']
        value = Encode_role[role]
        agent = clf.predict([[1,value]])[0]
    return render_template('results.html', c = agent)


if __name__ == '__main__':
	app.run()

		