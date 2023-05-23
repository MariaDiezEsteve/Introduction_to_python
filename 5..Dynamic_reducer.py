"""
DINAMIC REDUCER
dynamic_reduce([1,2,3], "+" ) # 6
dynamic_reduce([1,2,3], "-" ) # 0
dynamic_reduce([1,2,3], "*" ) # 6
dynamic_reduce([1,2,3], "/" ) # 0 
"""
import operator
from functools import reduce

def dynamic_reduce(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }   
    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reduce([1,2,3], "+" )) # 6
print(dynamic_reduce([1,2,3], "-" )) # -4
print(dynamic_reduce([1,2,3], "*" )) # 6
print(dynamic_reduce([1,2,3], "/" )) # 0.16666666666666666

