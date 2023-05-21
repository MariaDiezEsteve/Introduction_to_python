"""
SITE WEB INFORMATION:
http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
"""

# A First Function Definition
'''Function definition and invocation.'''

def happyBirthdayEmily(): 
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")

happyBirthdayEmily() 

# Multiple Function Definitions

'''Function definitions and invocation.'''

def happyBirthdayEmily():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")

def happyBirthdayAndre():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Andre.")
    print("Happy Birthday to you!")

def main():
    happyBirthdayEmily()
    happyBirthdayAndre()

main()

#F VS G
def f():
    print('In function f')
print('When does this print?')
f()

def g():
    print('In function f')
    print('When does this print?')
g()

# Function Parameters

'''Function with parameter.'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

happyBirthday('Emily')
happyBirthday('Andre')

'''Function with parameter called in main'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    happyBirthday('Emily')
    happyBirthday('Andre')

main()

'''User input supplies function parameter'''

def happyBirthday(person):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    print("Happy Birthday to you!")

def main():
    userName = input("Enter the Birthday person's name: ")
    happyBirthday(userName)

main()

#Multiple Function Parameters
'''Display any number of sum problems with a function.
Handle keyboard input separately.
'''

def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

main() 

#Returned Function Values
'''A simple function returning a value, used in an expression'''

def f(x):
    return x*x

print(f(3))
print(f(3) + f(4)) 

'''A function returning a string and using a local variable'''

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))
