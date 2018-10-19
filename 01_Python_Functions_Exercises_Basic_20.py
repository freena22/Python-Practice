
########## Python Functions Exercises ########

# 1. Write a function to find the Max of three numbers

# Solution 1:
def max_of_two(a,b):
	if a > b:
		return a
	else:
		return b
def max_of_three(a,b,c):
	if c > max_of_two(a,b):
		return c 
	else:
		return max_of_two(a,b)

# print(max_of_three(7,9,6))

# Solution 2:
def biggest(a,b,c):
	max = a
	if b > max:
		max = b
		if c > max:
			max = c
	return max

# print(biggest(9,6,8))


# 2. Write a function to sum all the numbers in a list

# Sample List: (8,2,3,0,7)
# Expected Output: 20

def sum_all(list):
	sum = 0
	for i in list:
		sum += i 
	return sum

list = [8,2,3,0,7]
#print(sum_all(list))

# 3. Write a function to multiply all the numbers in a list

# Sample list: (8,2,3,-1,7)
# Expected Output: -336

def multiply_all(list):
	num = 1
	for i in list:
		num  *=  i
	return num

list = [8,2,3,-1,7]
#print(multiply_all(list))

# 4. Write a function to reverse a string

# Sample string: "1234abcd"
# Expected Output: "dcba4321"

def string_reverse(str):
	rstr = ''
	index = len(str)
	while index > 0:
		rstr += str[index - 1]
		index -= 1
	return rstr

#print(string_reverse('1234abcd'))


# 5.Write a function to calculate the factorial of a number (non-negative integer)
# Sample number : 5
# Out: 5*4*3*2*1 = 120

def get_factorial(num):
	factorial = 1
	if num == 0:
		return 1
	else:
		for i in range(1, num + 1):
			factorial = factorial * i
		return factorial

print(get_factorial(5))

# 6. Write a function to check whether a number is in a given range.


#7. write a function that accepts a string and calculate the number of upper case letters and lower case letters
# Sample String: 'The quick Brow Fox'
# Expected Output: No. of Upper : 3 No. of lower: 12




