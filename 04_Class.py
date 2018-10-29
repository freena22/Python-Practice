
###### Objects and Classes ###


import random

class Dog:

	nature = 'cute' # class-level variable

	def __init__(self,name,age):
		# dunder init method
		self.name = name
		self.age = age
		self.woofs = 0

	def eat(self, food):
		if food == 'food':
			print('Yummy food!')
		else:
			print("That's not food!")

	def speak(self):
		print('woof!')

	def hear(self, words):
		if self.name in words:
			self.speak()

	def count(self):
		self.woofs += 1
		for bark in range(self.woofs):
			self.speak()
	def get_age(self):
		if self.age >= 1 and self.age <= 8:
			return "Adult"
		elif self.age < 1:
			return "Puppe"
		else:
			return "Senior"
class Cat:
	def speak(self):
		print(random.choice(['Meow!', 'Purr...']))

lulu = Dog('Lulu Bao', 0.5 )
print(lulu.name)  # lulu
print(lulu.age)   # 0.5
print(lulu.get_age()) # Puppe


luka = Dog('luka', 4)
luka.hear('Can luka hear me?') # Woof!

luka.count() # Woof!
luka.count() # Woof! Woof!

lumi = Cat()
lumi.speak() # Meow! Or Purr...




###### Using super function 

import turtle

class BigOrangeTurtle(turtle.Turtle):

	def __init__(self):
		super().__init__()
		# call the parent class'initializer as the first thing that
		# the child class does in its initializer
		self.color('orange')
		self.width(10)

	def draw_square(self):
		for side in range(4):
			self.forward(100)
			self.right(90)

	def draw_flower(self):
		for petal in range(6):
			self.draw_square()
			self.right(60)
		self.hideturtle()

apple = BigOrangeTurtle()

apple.draw_flower()

