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
def count_ch_1(string, target): # for loop
	count = 0
	for ch in string:
		if ch == target:
			count += 1
	print(count)

def count_ch_2(string, target): # while loop
	index = 0
	count = 0
	while index < len(string):
		if string[index] == target:
			count += 1
		index += 1
	return count

count_ch1("the goofy doom of the balloon goons", "o") # 9


########## function 7: until dot function
def until_dot_1(s):
    index = 0
    while index < len(s) and s[index] != '.':
        # No dots yet, keep going.
        index += 1
    # We either found a dot or ran out of string.
    return s[:index]

def until_dot_2(s):
    for index in range(len(s)):
        if s[index] == '.':
            # A dot! Return everything up to here.
            return s[:index-1]
    # We ran out of string without seeing any dots.
    # Return the whole string.
    return s

until_dot("This is a sentence. This is another.")
# 'This is a sentence'

########### function 8: no repeating input 
def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words
'''putput
Tell me a word: luka
Tell me a word: luki
Tell me a word: lumi
Tell me a word: lucy
Tell me a word: luka
You told me that word already!
['luka', 'luki', 'lumi', 'lucy']
'''
