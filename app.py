from flask import Flask, request, render_template
app= Flask(__name__)

# def addition (num1, num2):
#     addition = num1 + num2

# def subtarction (num1, num2):
#     subtarction= num1 - num2

# def multiplication (num1, num2):
#     multiplication = num1 * num2

# def division (num1, num2):
#     division = num1 / num2    


@app.route ('/')
def home():
    return render_template('home.html')

@app.route ('/calculate', methods=["POST"])
def calculate():
    n1 = float(request.form["num1"])
    n2= float(request.form['num2'])
    n3 = request.form['operation']
    print(n1,n2,n3)
    print(type(n3))
    res= 0
    if n3 == 'add':
        res= n1 + n2
    elif n3 == 'sub':
        res= n1- n2
    elif n3 == 'mul':
        res = n1* n2 
    elif n3 == 'div':
        res = n1 / n2
    print(res)

    return render_template("home.html", res=res)

# @app.route('/plus')
# def addition():
#     return render_template(home.html)

# @app.route('/minus')
# def subtraction():
#     return render_template(home.html)

# @app.route('/multiply')
# def multiplication():
#     return render_template(home.html)

# @app.route('/divide')
# def division():
#     return render_template(home.html)
if __name__=='__main__ ':
    app.run(debug = True)