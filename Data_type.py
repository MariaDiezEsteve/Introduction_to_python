"""
List of Data Types
Booleans
Numbers
Strings
Bytes and byte arrays
None
Lists
Tuples
Sets
Dictionaries

"""

meal_completed = True
sub_total = 100
tip = sub_total * 1/5
total = sub_total + tip
receipt = "Your total is " + str(total) #total as string
print(receipt)


"""
1. Change variables values
"""

first = 'Springer'
second = 'Bregman'
third = 'Altuve'

print(first)

first = third

print(first)


#1. Python String Basics

sentence = "The quick brown fox jumped over the lazy dog"

sentence_two = "That is my dog\'s Bob"
#\ : that is gonna say that the nex character is gonna be string
print(sentence)


#1.1 Python String Case Functions
#upper - THE QUICK BROWN FOX JUMPED
#1.1.1 Part 1

sentence_three = "The quick brown fox jumped".upper()
print(sentence_three)
#1.1.2 Part 2
print(sentence_three.upper())

#1.1.3 Part 3
sentence_start = "The quick brown fox jumped"
sentece_four = sentence_start.upper()
print(sentence_start)
print(sentece_four)

#1.2 How to Access Portions of Strings in Python

#"The quick brown fox jumped"
#T: 0
#c: 6

starter_sentence = "The quick brown fox jumped"
print([starter_sentence[10]])
print([starter_sentence[3:6]])
#Out: ['b']
#Out: [' qu']

second_sentence = "The" + starter_sentence[9:]
print(second_sentence)
#Out: The brown fox jumped

# Heredoc

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()

#string.strip(characters)
"""
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt") --- Delete this characters
print(x) 
out: banana
"""

print(content)

"""
The repr() function returns a printable representation of the given object.
numbers = [1, 2, 3, 4, 5]

# create a printable representation of the list
printable_numbers = repr(numbers)
print(printable_numbers)

# Output: [1, 2, 3, 4, 5]
"""
print(repr(content))