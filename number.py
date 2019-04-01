import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/minMax', methods=["POST", "GET"])
def random_number_generate():
	if request.method=="POST":
		a = int(request.form['lowerLimit'])
		b = int(request.form['upperLimit'])
		number = random.randint(a, b)
		return redirect(url_for('/NumberResult.html',
								number=number))
	return render_template("/NumberGenerator.html")

@app.route("/NumberGenerator.html", methods = ["GET"])
def randomNumber():
		name = request.args.get('number')
		return render_template("/NumberResult.html",
								number=number)

if __name__ =="__main__":
    app.run(debug=True, port=8080)

random_numbers()
