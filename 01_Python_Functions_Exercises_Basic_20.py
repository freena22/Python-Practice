
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
print(multiply_all(list))

# 4. Write a function to reverse a string

# Sample string: "1234abcd"
# Expected Output: "dcba4321"



