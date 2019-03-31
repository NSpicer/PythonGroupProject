import random

from flask import Flask, render_template, request

app = Flask("Numbers")

@app.route("/randomnumber", methods=["POST"])

def random_numbers():
	form_data = request.form
	print("What is the min and max of your random number?")
	a = int(lowerLimit)
	b = int(upperLimit)

	number = random.randint(a, b)
	print number

random_numbers()
