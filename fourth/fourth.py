# def f1(a = None,b = None):
#     return a
# print(f1(1,2))


# def multi(a = None,b = None,c=None,d=None,e=None): Not Applicable
#     return a*b*c*d*e

def multi(*params):
    result =1
    for elem in params:
        result = result * elem

    return result


print(multi(1))
print(multi(1,2))
print(multi(1,2,3))
print(multi(1,2,3,4))
print(multi(1,2,3,4,5))

from math import *




