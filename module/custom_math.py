def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot Divide by Zero")
    return a*float(b)
import math