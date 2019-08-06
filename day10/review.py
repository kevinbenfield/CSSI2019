""" remove theese qoutes@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#how to define a function.
'''You start by typing the 
keyword def followed by the 
name of the function and then
parentheses with a list of
parameters separated by commas.
last you add a colon after the
close parenthesis and indent the next
line for the body of the function'''

def f(x):
    return 2 * x + 3
    print "the end of the function"

'''The above function is named f.
It takes one parameter which should 
be a number. The function returns
twice the parameter plus 3'''

'''Once a function is defined, you can use 
it by calling it. To call a function, you must 
use the function's name followed by parentheses 
with arguments of the function enclosed in them.
arguments are literals, objects, expressions 
or return-value function calls that take the
place the parameters in the function definition.
the arguments are associated with the parameter
in the same position as them in. Hence, the first 
argument is associated with the first parameter,
and so on. Last, the number of arguments must match
number of parameters whenever default valuse are
not provided.'''

#function call with a literal
print f(2)

#function call with an expression
print f(3 + 4 * 6) #return 57

#function call with a function call
print f(f(6)) #return 33

v = 89
#function call with a variable
print f(v) #return 181

'''Task 1: Define a function that takes two
parameters. It returns the greater of the
two parameters. Assume that the parameters
are numbers'''

def Greater(x,y):
    if x >= y:
        return x
    else:
        return y

x = float(raw_input("Enter first number: "))
y = float(raw_input("Enter second number: "))

print Greater(x,y)

'''Task 2: Define a function that takes no parameters. It
prompts the user to enter a string. Afterwards, it return
the string concatenated with itself'''

def Echo():
    msg = raw_input("Enter a string")
    return msg + msg

print Echo()

'''Task 3: Define a function that takes 
three parameters. It displays the value of 
three more than the product of the 
parameters. Assume that the parameters are 
numbers'''

def Three(w,r,t):
    v = (w * r * t) + 3
    print v

Three(2,3,4)

#list
'''What is a list?'''
'''A list is an ordered collection of objects'''
'''You access the elements of a list with an 
index which is an interger between -n to n-1
where n is the length of the list'''

#list methods 
print "The original list"
print "l =", l
print "k =", k
print "j =", j

l.append ('a')
k.append('t')
j.append(k) #is now an empty list

print "the list after clear is calledn j"
print "l =", l
print "k =", k
print "j =", j

l.insert(0,'h')
k.insert(0,'a')
j.insert(5,12)

l.pop()
k.pop()
j.pop()

print "\nThe list after an pop"
print "l =", l
print "k =", k 
print "j =", j
""" #remove these qoutes @@@@@@@@@@@@@@@@
#loops
#while loop

#counting to 10 from 1
"""i = 1
while i <= 10:
        print i
    i += 1

#count to 20 starting from 1
i = 1 
while i <= 20:
        print i
    i += 1

#counting to 20 starting from 1 but only even numbers
i = 1
while i <= 20:
    if 1 % 2 == 0:
        print i
    i += 1

#counting to 20 with odd numbers 
i = 1
while i <= 20:
    if 1 % 2 == 1:
        print i
    i += 1

v = ""
while v != "hello":
    v = raw_input("Enter a string: ")"""

"""
#for loop
#it is used for traversing,sequences
for i in range (1,11):
        print i

for i in range (1,21):
        print i

for i in range (2,21,2):
        print i 

for i in range (1,21):
    if i % 2 == 0:
        print i

for i in range (1,21):
    if i % 2 == 1:
        print i

for i in "This is a string":
        print i

h = []

for i in range (20):
    h.append(0)

print h, len(h)

h[1] = 1

for i in range (2,20):
    h[1] = h[i-1] + h[i-2]

print h 

"""
#dictionary
'''What is a dictionary?'''
'''An unordered collection of key-value pairs'''
'''How to create a dictionary'''
"""
d = {}
b = dict()
a = {1:2,2:1,3:3,4:5,5:4} #a dictionary of permutation
c= {12:"John Smite",69:"Jane Doe"}

print a[1]

print c[69]

#adding elements to a dictionary

c[72] = "Joe Brown"

print c 

#dictionary
"""

'''What is an object'''
'''an instance of a class'''

class Person:
    def __init__(self,name):
        self.name = name 
        self.age = 0 

    def birthday(self):
        self.age += 1

#Create objects

t = Person("Jane Doe") #created a person object

print t.name, t.age

s = Person("Roger Sam")

print s.name, s.age

t.birthday()

print t.name, t.age
