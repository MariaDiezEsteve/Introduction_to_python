#1.1 Overview of Number Types in Python

product_id = 123 #integer data type
sale_price = 14.99 #  floating-point type of data type (decimal)
tip_percentage = 1/5 # it's a fraction
new_product = 150 #integer data type

print(sale_price + new_product)

#1.2 Mathematical Operators in Python
# Addition, subtraction, division, floor division, multiplication, modulus, and exponents.

print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

print('Modulus')
print(100 % 42)

print('Exponents')
print(100 ** 42)

#1.3 Order of Operations in Python
"""
Please -> Parans ()
Excuse -> Exponents **
My -> Multiplication *
Dear -> Division /
Aunt -> Addition +
Sally -> Subtraction -

8 + 2 * 5 - (9 + 2) ** 2
8 + 2 * 5 - 11 ** 2
8 + 2 * 5 - 121
8 + 10 - 121
-103
"""

calculation = 8 + 2 * 5 - (9 + 2) ** 2

print(calculation)

#1.4 Use Assignment Operators in Python
total = 100

total = total + 10
total += 10
total -= 10
total *= 2
total /= 10
total //= 10
total **= 2
total %= 2

product_two = 120
product_three = 10

total += product_two
total += product_three

print(total)

#1.4.1 Decimal vs Float in Python
#Decimal Librery: https://docs.python.org/es/3/library/decimal.html
#Decimal numbers can be represented exactly
from decimal import Decimal
#Without Decimal Librery
product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

#With Decimal Librery
product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451

#1.4.2 Convert Between the Integer, Float, Decimal and Complex Numeric Data Types in Python

from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost)) #integer
print(float(qty)) # float
print(Decimal(product_cost)) #decimal
print(complex(commission_rate)) #complex

#1.4.3 Popular Math Functions in Python
import math

loss = -20.25
product_cost = 89.99

print(abs(loss)) #it's going to take the absolute value of loss (pure value) (25)
print(math.floor(product_cost)) #returned an integer, and it picked the floor of this product cost float. (89)
print(math.ceil(product_cost)) #returned an integer, ceiling is going to give us the rounded up value. (90)
print(abs(math.floor(loss))) #(21)
print(round(product_cost)) #round to the nearest whole number so I can say round here (90)
print(math.sqrt(product_cost)) #https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/sqrt: quare root in the function.  (9.486305919587455)
print(math.pow(5, 2)) #https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math/pow: takes two arguments. And so if I do five comma two and print this out it's 25 because it's going to be five squared.(25.0)
print(5 ** 2) #(25)

#1.4.4 Build a Manual Exponent Function in Python0
from functools import reduce

#  def manual_exponent(num, exp):
#      computed_list = [num] * exp
#      return (reduce(lambda total, element: total * element, computed_list))
#
#
#  print(manual_exponent(2, 3))
#  print(manual_exponent(10, 2))
#  print(manual_exponent(3, 3))
#  print(manual_exponent(10, 5))

# def manual_exponent(num, exp):
#     counter = exp - 1
#     total = num

#     while counter > 0:
#         total *= num
#         counter -= 1

#     return total

# print(manual_exponent(2, 3))
# print(manual_exponent(10, 2))
# print(manual_exponent(3, 3))
# print(manual_exponent(10, 5))

def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
print(manual_exponent(3, 3))
print(manual_exponent(10, 5))