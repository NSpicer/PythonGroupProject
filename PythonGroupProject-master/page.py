import random
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/cointoss")
def toss():
		return render_template("CoinToss.html")


@app.route("/diceroll")
def dice():
	return render_template("DiceRoll.html")

@app.route("/rnumber")
def number():
	return render_template("NumberGenerator.html")

@app.route("/rnumber_result", methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		a = request.form["max"]
		b = request.form["min"]
		c = random.randint(int(a), int(b))
		return render_template("numberresults.html", c=c)

		

if __name__ == '__main__':
	app.run(debug=True)