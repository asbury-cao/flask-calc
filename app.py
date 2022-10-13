# Put your app in here.

import re
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def calc_add():
    '''
    takes two numbers as query parameters and returns the sum
    '''

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a,b)
    return str(result)

@app.get('/sub')
def calc_sub():
    '''
    takes two numbers as query parameters and returns the difference
    '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a.b)
    return str(result)

@app.get('/mult')
def calc_mult():
    '''
    takes two numbers as query parameters and returns the product
    '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.get('/div')
def calc_div():
    '''
    takes two numbers as query parameters and returns the quotient
    '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)