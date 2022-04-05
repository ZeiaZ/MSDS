#Notes for basic python syntax

#IMPORTS
from math import *

#python 3 print syntax
print("Hello world")

#printing with variables
name = "Bob"
age = 52
print (name + "'s age is " + str(age) + ".")

#BOOLEANS
boolean1 = True
boolean2 = False

#STRINGS
mrString = "I am a string"
#newlines in strings
multilineString = "I\nam\na string"
print(multilineString)
#escape chars
escapeString = "I am a \"string\""
print(escapeString)
#concatonation
concat = "I am " + "concatonated. " + mrString
print(concat)
#upper and lower case
print(concat.upper())
print(concat.lower())
print(concat.isupper())
print(concat.upper().isupper())
print(concat.islower())
print(concat.lower().islower())
#length
print(len(concat))
#indexing. They start at 0
print(concat[0])
print(concat[-1])
print(concat[len(concat)-1]) #this would out of bounds error without -1
#searching for index
print(concat.index("c"))#returns index where the first "c" is.
#replace
print(concat.replace("string","dog"))

#NUBMERS
#ints
add = 1 + 2
sub = 2 - 1
div = 4 / 2
multi = 6 * 2
mod = 10 % 3
#absolute value
neg = -5
print(abs(neg))
#powers/exponents
fourSquared = pow(4,2)
print(fourSquared)
#max/min
threeSquared = pow(3,2)
print(max(threeSquared,fourSquared)) #these both return the value of the min or max arg
print(min(threeSquared,fourSquared))
#rounding
mrDecimal = 5.241412
print(round(mrDecimal))
#floor/ceil REQUIRES MATH IMPORT
print(floor(mrDecimal))
print(ceil(mrDecimal))
#sqrt
print(sqrt(mrDecimal))

#USER INPUTS
#basic
name = input("Enter your name: ")#will prompt for name and save it is name var
print("Hello " + name + "!")

#TYPECASTING
print(str(1251512))
print(float("5.623623"))
print(int("534"))

#LISTS
l = []