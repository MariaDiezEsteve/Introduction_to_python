#1.1 Guide to Python's Partition Function
#https://www.w3schools.com/python/ref_string_partition.asp
"""
Search for the word "bananas", and return a tuple with three elements:
1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
Out: ('I could eat ', 'bananas', ' all day')

"""

heading = "Python: An Introduction, and Python: Advanced"

header, _ , subheader = heading.partition(': ')

print(header)
print(subheader)

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)

#1.2 Guide to the Python split Function
#https://www.w3schools.com/python/ref_string_split.asp

tags = 'python,coding,programming,development'

#1.2.1 Create a list
list_of_tags = tags.split(',') #create a list with all words separeted by ","
list_of_tags = tags.split()

print(list_of_tags)

#1.2.2 Take out after the coma
heading = "Python: An Introduction"
heading, subheading = heading.split(': ')

print(heading)
print(subheading)

#1.3 Check if Strings Represent Numbers or Alphanumeric Characters in Python
api_data = '5'
greeting = 'Hi there'

print("alpha numero", api_data.isalpha())
print("alpha string", greeting.isalpha())

print("numeric numero",api_data.isnumeric())
print("numeric string",greeting.isnumeric())