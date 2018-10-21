#### Play with the Strings ####

print("a\n very short \n poem")
# \n newline character

print("Give us\n\nsome\n\n\n\nspcae") # multiple

print("It\'s long")
# escape character

word = "happy"
for num in range(len(word)):
    print(num, word[num])

# f to print {}
animal = "kitten"
f"Who's a cute {animal}?" # f-function

import math
pi = 3.1415926
f"pi is about {math.pi:.6}"
# 'pi is about 3.14159'  take the 6 digits

for x in [7, 8, 9]:
    y = x + 1
    print(f"After {x} comes {y}.")


word = ["luka", "lumi"]
word.append("lucy")
word.extend('abc') # appends each element to the end of the list.
#word.extend("loo","cc","bb") # append multiples
word.sort() # alphabetical order


noun = "wolf"
#noun[0] = 'g'
# You can't modify the values inside of a string in Python cause it's inmutable.


######## function 1: word triangle
def word_triangle(word):
  length = len(word)
  for n in range(length):
    print(word[:length - n])
word_triangle("luka")
'''
luka
luk
lu
l
'''


######### function 2: Total of three

def total_of_three(x1,x2,x3):
	one = input("Enter a number: ")
	two = input("Enter another number: ")
	three = input("Enter a third number: ")
	result = int(one) + int(two) + int(three)
	print(f"{one} + {two} + {three} = {result}")


######### function 3: start with string two versions
def starts_with_1(long,short):
	for position in range(len(short)):
		if long[position] != short[position]:
			return False
	return True

def starts_with_2(long, short):
	return long[0:len(short)] == short

######### function 4: find the possible HTML tag
def possible_tag(word):
    if word.startswith("<") and word.endswith(">"):
        print(word, "could maybe be an HTML tag")
    else:
        print(word, "is definitely not an HTML tag (but might contain one)")

########## function 5:  define a good_length function for password
def good_length(input):
	return len(input) >=8


########## function 6: Count any character
def count_ch(string, target):
	count = 0
	for ch in string:
		if ch == target:
			count += 1
	print(count)
count_ch("the goofy doom of the balloon goons", "o") # 9




