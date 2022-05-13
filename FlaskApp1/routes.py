from FlaskApp1 import app, db
from flask import render_template, request, redirect, flash, json, Response, url_for
from FlaskApp1.models import User, Course, Enrolment, Calculator
from FlaskApp1.forms import LoginForm, RegisterForm, CalculatorForm


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    # return "<h1>Hello Everyone!!</h1>"
    return render_template("index.html", login=False, index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password) == user.password:
            flash(f"{user.first_name}, you are successfully logged in!")
            return redirect("/index")
        else:
            flash("Sorry, Something went wrong.")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term=None):
    courseData = [
        {"courseID": "1111", "title": "PHP 101", "description": "Intro to PHP", "credits": 3, "term": "Fall, Spring"},
        {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": 4,
         "term": "Spring"},
        {"courseID": "3333", "title": "Adv PHP 201", "description": "Advanced PHP Programming", "credits": 3,
         "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": 3,
                           "term": "Fall, Spring"},
        {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": 4,
         "term": "Fall"}]
    if term is None:
        term = term
    classes = Course.objects.order_by("+courseID")
    return render_template("courses.html", courseData=courseData, courses=True, term=term)


@app.route("/enrolment", methods=['GET', 'POST'])
def enrolment():
    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = 1
    if courseID:
        if Enrolment.objects(user_id=user_id, courseID=courseID):
            flash(f"OOps! You are already registered in this course {courseTitle}!")
            return redirect(url_for("courses"))
        else:
            Enrolment(user_id=user_id, courseID=courseID)
            flash(f"You are enrolled in {courseTitle}!")
    classes = None
    # term = request.form.get('term')
    return render_template("enrolment.html", enrolment=True, title="Enrolment", classes=classes)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(user_id=User, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)


@app.route("/user")
def user():
    # User(user_id=1, first_name="Ryan", last_name="Hawcroft", email="ryan@sps.com.au", password="abc1234").save()
    # User(user_id=2, first_name="Connor", last_name="Lowe", email="connor@sps.com.au", password="password123").save()
    # Users = User.object.all()
    return render_template("user.html")


@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    num1 = form.num1.data
    num2 = form.num2.data
    num1AddNum2 = str(num1 + num2)
    num1TakeNum2 = str(num1 - num2)
    num1DivNum2 = str(num1 / num2)
    num1TimesNum2 = str(num1 * num2)
    if form.validate_on_submit():
        return render_template("calculator.html", num1AddNum2=num1AddNum2, num1TakeNum2=num1TakeNum2,
                               num1DivNum2=num1DivNum2, num1TimesNum2=num1TimesNum2, form=form, title=Calculator)
    return render_template("calculator.html", form=form, title="Calculator")


@app.route("/calcDF", methods=['GET'])
def calcDF():
    """" Simply Displays the calc page accessible at '/calcDF """
    return render_template('calcDF.html')


@app.route("/operation_result/", methods=['POST'])
def operation_result():
    """ Route where we send"""
    error = None
    result = None
    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        if operation == "+":
            result = input1+input2

        elif operation == "-":
            result = input1-input2

        elif operation == "/":
            result = input1/input2

        elif operation == "*":
            result = input1*input2

        elif operation == "%":
            result = input1%input2



