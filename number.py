import random

def random_numbers():
	print("What is the min and max of your random number?")
	a = int(input("min"))
	b = int(input("max"))

	number = random.randint(a, b)
	print number

random_numbers()