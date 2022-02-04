from flask import Flask, request
from operations import *
from math import *

app = Flask(__name__)

@app.route("/<op>")
def op_ab(op):
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  if op == "add":
    return str(add(a,b))
  elif op == "sub":
    return str(sub(a,b))
  elif op == "mult":
    return str(mult(a,b))
  elif op == "div":
    return str(int(div(a,b)))