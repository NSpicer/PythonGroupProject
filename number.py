import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/templates/NumberGenerator.html", methods=["POST", "GET"])
def random_numbers():
	if request.method=="POST":
		a = int(request.form['lowerLimit'])
		b = int(request.form['upperLimit'])
		number = random.randint(a, b)
		return redirect(url_for('randomNumber',
								number=number))
	return render_template("/NumberGenerator.html")

@app.route("randomNumber", methods = ["GET"])
def randomNumber():
		name = request.args.get('number')
		return render_template("/NumberGenerator.html",
								number=number)

if __name__ =="__main__":
    app.run(debug=True, port=8080)

random_numbers()
