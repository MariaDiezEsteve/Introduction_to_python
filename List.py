
#1.1Lists in Python
"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)

print([users[2]])

users[4] = 'Brayden'

print(users)

#1.2 Three Ways to Remove Elements from a Python List
user = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(user)

user.remove('Jordan')

print(user)

popped_user = user.pop() #pop doesn't simply delete an item pop actually returns that item so that you can use it.

print(popped_user)
print(user)

del user[0]

print(user)

#1.3 Nested Lists and Best Practices for Storing Multiple Data Types in a Python List

nested_lists = [[123], [234], [345]] #Example: nested list - listas anidadas

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list) #['Kristine', 'Tiffany', 'Jordan', 'Leann'] we keep in user_list the element that we are deleting from mixed_list
print(mixed_list) # [42, 10.3, 'Altuve'] - With pop() changes the list mixed_list 

#1.4 Python List Query Processes: len(), Negative Indexes, and index()

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags) # 4
print(last_item) # code 
print(index_of_last_item)# 3

#1.5 How to Sort Lists in Python - sort: clasificar
tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags) #['code', 'development', 'python', 'tutorials'] in alphabetical order

tags.sort(reverse=True) 

print(tags) #['tutorials', 'python', 'development', 'code'] in alphabetical reverse order

totals = [234, 1, 543, 2345]

totals.sort()

print(totals) #[1, 234, 543, 2345] sort in ascending order

totals.sort(reverse=True) 

print(totals) #[2345, 543, 234, 1] sort in descending order

#1.6 Using the join Function in Python to Build a URL Query String
#replicate this url https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']

formatted_tags = '+'.join(tags)
print(formatted_tags) # python+development+tutorial

query_uri = f'{uri}{formatted_tags}'
print(query_uri) #https://www.google.com/search?q=python+development+tutorial

#1.7 Ranges in Python Lists
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[2:]
print(tag_range) #['tutorials', 'code']

tag_range = tags[0:2]
print(tag_range) # ['python', 'development']

tag_range = tags[:2]
print(tag_range) #['python', 'development']

tag_range = tags[0:-1]
print(tag_range) # ['python', 'development', 'tutorials']

#1.8 Advanced Techniques for Implementing Ranges and Slices in Python Lists
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_ranges = tags[1:-1:2] # ['development', 'code'] - start:1 -> to the end:-1 -> just give 2 elements 
print("tags[1:-1:2]" , tag_ranges)

tag_ranges = tags[::-1] #['computer science', 'programming', 'code', 'tutorials', 'development', 'python'] -> give all the elements starting for the last
print("tags[::-1]", tag_ranges)

tags.sort(reverse=True) #['tutorials', 'python', 'programming', 'development', 'computer science', 'code'] -> give all the elements in desdending alphabetical order
print(tags)

#1.8.1 Difference between [::-1] vs sort
#[::-1] keep the list in a variable
#sort can't keep the list in a variable because it's change the value of the variable.

#1.9 The sorted Function in Python
#How to resolve this problem: "sort can't keep the list in a variable because it's change the value of the variable" with the sorted function
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices, reverse=True) #[400, 220, 100, 100, 83, 40, 10, 3, 1]
print(sorted_list)

#1.10 How to Find the Median of a Python List with an Odd Number of Numbers
#find the median in a Python list
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices) #[1, 3, 10, 40, 83, 100, 100, 220, 400]
num_of_sales = len(sorted_list) #4
half_slice = math.floor(num_of_sales/2) # 4/2 = 2
first_sales_items = sorted_list[:half_slice] # [:2] -> [1, 3, 10, 40]
last_sales_items = sorted_list[-(half_slice):] # [-2:] -> [100, 100, 220, 400]
median = sorted_list[half_slice:(half_slice + 1)] # [2:3] -> [83]

print(sorted_list)
print(num_of_sales)
print(half_slice)
print(first_sales_items)
print(last_sales_items)
print(median)

#1.11 Working with the slice Class in Python to Store Slices
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2]) #['development', 'code']

slice_obj = slice(1, 4, 2)

print(slice_obj.start) # 1
print(slice_obj.stop) #4
print(slice_obj.step)# 2

print(tags[slice_obj]) #['development', 'code']