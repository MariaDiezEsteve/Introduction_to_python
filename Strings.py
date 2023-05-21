#1.1 String interpolation
#String interpolation allows us to process python code inside of strings 

#f-strings: https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals

#We can use it {} into string to show another variable.

name = 'Kristine'
greeting = f"Hi {name}"

product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(greeting)
print(email_content)

#1.2 str.format(*args, **kwargs)
# https://docs.python.org/3/library/stdtypes.html#str.format
name = "María"
age = 50
product = "Python eLearning course"

greeting_maria = " Hi {0}, you are listed as {1} years old and you have purchased: {2} ...".format(name, age, product)

print(greeting_maria)

#1.3 Finding a Substring in Python with: Find, Index, and In

sentence_dog = 'The quick brown fox jumped over the lazy dog.'

#1.3.1 Find
#https://docs.python.org/3/library/stdtypes.html#str.find

query= sentence_dog.find("quick")
print(query) #out 4 index value

query= sentence_dog.find("ops")
print(query) #out -1

#1.3.2 Index
#https://docs.python.org/3/library/stdtypes.html#str.index

query_two = sentence_dog.index("quick")
print(query_two) #out 4 

#query_two = sentence_dog.index("ops")
#print(query_two) #out - error, only if existis in the sentence_dog

#1.3.3 In

query_three = "opps" in sentence_dog
print(query_three) #out - False


#1.4 Using Python's replace Function to Find and Replace String Values
#1.4.1 New value

sentence_fox = 'The quick brown fox jumped over the lazy dog.'
sentence_fox = "New value"

print(sentence_fox)

#1.4.2 Replace

sentence_fox = sentence_fox.replace("New value", "The quick brown fox jumped over the lazy dog.")
#sentence_fox = sentence_fox.replace("quick","slow")
print(sentence_fox)


#1.5 Overview of Python's strip, lstrip, and rstrip Functions
#string.strip(characters): https://www.w3schools.com/python/ref_string_strip.asp

url = 'https://google.com'

print(url.strip('https://'))

url = url.lstrip('https://') #start left to clear
url = url.rstrip('.com') #start rigth to clear

print(url.capitalize())

#1.6 Guide to Python's Partition Function
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

#1.7 Guide to the Python split Function
#https://www.w3schools.com/python/ref_string_split.asp

tags = 'python,coding,programming,development'

#1.7.1 Create a list
list_of_tags = tags.split(',') #create a list with all words separeted by ","
list_of_tags = tags.split()

print(list_of_tags)

#1.7.2 Take out after the coma
heading = "Python: An Introduction"
heading, subheading = heading.split(': ')

print(heading)
print(subheading)

#1.8 How to Check if Strings Represent Numbers or Alphanumeric Characters in Python

