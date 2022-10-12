# Put your app in here.

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

