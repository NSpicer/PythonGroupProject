import random

from flask import Flask, render_template, request

app = Flask("Numbers")

@app.route("/randomnumber", methods=["POST", "GET"])
def random_numbers():
	a = request.form['lowerLimit']
	b = request.form['upperLimit']
	a = int(a)
	b = int(b)
	number = random.randint(a, b)
	return render_template("NumberGenerator.html", name = number)


random_numbers()
