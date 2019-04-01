import random, os
from flask import Flask, render_template, request
from intro_to_flask import app
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/cointoss")
def toss():
		return render_template("CoinToss.html")

@app.route("/cointoss_ht")
def tossht():
		t = random.random()
		return render_template("tossresults.html", t=t)


@app.route("/diceroll")
def dice():
	return render_template("DiceRoll.html")

@app.route("/diceroll_num")
def roll():
	r = random.randint(1, 6)
	return render_template("rollresults.html", r=r)

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
	port = int (os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
