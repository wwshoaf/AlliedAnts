from flask import Flask, render_template, request, redirect, url_for, flash
from modules import persons, classes, sales, reports


app = Flask(__name__)
app.secret_key = "yogastudio440"

# home page

@app.route("/")
def index():
    return render_template("index.html")

# customers
@app.route("/customers")
def customers():
    rows = persons.list_customers()
    return render_template("customers.html", customers=rows)

@app.route("/customers/add", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        payment = request.form["payment"]
        success, msg = persons.add_customer(name, phone, email, payment)
        flash(msg, "success" if success else "error")
        return redirect(url_for("customers"))
    return render_template("add_customer.html")

@app.route("/customers/delete/<name>/<phone>")
def delete_customer(name, phone):
    _, msg = persons.delete_person(name, phone)
    flash(msg, "success")
    return redirect(url_for("customers"))

@app.route("/customers/update/<name>/<phone>", methods = ["GET", "POST"])
def update_customer(name, phone):
    if request.method == "POST":
        new_payment = request.form["payment"]
        _, msg = persons.update_payment_method(name, phone, new_payment)
        flash(msg, "success")
        return redirect(url_for("customers"))
    customer = persons.get_person(name, phone)
    return render_template("update_customer.html", customer = customer)

# teachers
@app.route("/teachers")
def teachers():
    rows = persons.list_teachers()
    return render_template("teachers.html", teachers=rows)

@app.route("/teachers/add", methods=["GET", "POST"])
def add_teacher():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        success, msg = persons.add_teacher(name, phone, email)
        flash(msg, "success" if success else "error")
        return redirect(url_for("teachers"))
    return render_template("add_teacher.html")

# classes
@app.route("/classes")
def class_list():
    rows = classes.list_classes()
    return render_template("classes.html", classes=rows)

# sales
@app.route("/sales")
def sales_list():
    rows = sales.list_sales()
    return render_template("sales.html", sales=rows)

# reports
@app.route("/reports")
def reports_page():
    return render_template("reports.html")

@app.route("/reports/revenue")
def reports_page_rev():
    start = request.args.get('st')
    end = request.args.get('ed')
    return render_template("reports.html", rev = reports.revenue_by_date(start, end))

@app.route("/reports/trans")
def reports_page_trans():
    start = request.args.get('st')
    end = request.args.get('ed')
    return render_template("reports.html", trans = reports.all_trans(start, end))

@app.route("/reports/teacher_KPI")
def reports_page_teacher():
    return render_template("reports.html", teacher = reports.classes_per_teacher())

@app.route("/reports/attn")
def reports_page_attn():
    return render_template("reports.html", attn=reports.attendance_report())

# run
if __name__ == "__main__":
    app.run(debug=True)