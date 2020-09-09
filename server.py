from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    print(request.form)
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    print(request.form)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id= request.form['student_id']
    strawberry=int(request.form['strawberry'])
    raspberry=int(request.form['raspberry'])
    blackberry=int(request.form['blackberry'])
    apple=int(request.form['apple'])
    return render_template("checkout.html", first_name=first_name, last_name=last_name, student_id=student_id, strawberry=strawberry, raspberry=raspberry, blackberry=blackberry, apple=apple)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
