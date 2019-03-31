from flask import Flask, render_template, request 
app = Flask("Generator")

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/cointoss/")
def coin():
	return render_template("CoinTossPage.html")

@app.route("/diceroll/")
def dice():
	return render_template("DiceRoll.html")

@app.route("/cointoss/")
def number():
	return render_template("NumberGenerator.html")


app.run(debug=True)