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
    return render_template("customers.html", customers=[], show_add_form=True)

@app.route("/customers/delete/<name>/<phone>")
def delete_customer(name, phone):
    success, msg = persons.delete_person(name, phone)
    flash(msg, "success" if success else "error")
    return redirect(url_for("customers"))

@app.route("/customers/update/<name>/<phone>", methods = ["GET", "POST"])
def update_customer(name, phone):
    if request.method == "POST":
        new_payment = request.form["payment"]
        success, msg = persons.update_payment_method(name, phone, new_payment)
        flash(msg, "success" if success else "error")
        return redirect(url_for("customers"))
    customer = persons.get_person(name, phone)
    return render_template("customers.html", customers = persons.list_customers(), show_update_form=True, customer=customer)

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
    return render_template("teachers.html", teachers=persons.list_teachers(), show_add_form=True)

# classes
@app.route("/classes")
def class_list():
    rows = classes.list_classes_by_date()
    return render_template("classes.html", classes=rows)

@app.route("/classes/add", methods=["GET", "POST"])
def add_class():
    if request.method == "POST":
        success, msg = classes.create_class(
            class_date=request.form["class_date"],
            class_time=request.form["class_time"],
            class_type=request.form["class_type"],
            duration=request.form["duration"]
        )
        flash(msg, "success" if success else "error")
        return redirect(url_for("class_list"))
    return render_template("classes.html", classes=[], show_add_form=True)

@app.route("/classes/<class_date>/<class_time>/enroll", methods=["GET", "POST"])
def enroll_student(class_date, class_time):
    if request.method == "POST":
        success, msg = classes.enroll_customer(
            name=request.form["name"],
            phone=request.form["phone"],
            class_date=class_date,
            class_time=class_time
        )
        flash(msg, "success" if success else "error")
        return redirect(url_for("class_list"))
    return render_template("classes.html", classes=[], show_enroll_form=True, enroll_date=class_date, enroll_time=class_time)

@app.route("/classes/<class_date>/<class_time>/drop", methods=["GET", "POST"])
def drop_student(class_date, class_time):
    if request.method == "POST":
        success, msg = classes.drop_customer(
            name=request.form["name"],
            phone=request.form["phone"],
            class_date=class_date,
            class_time=class_time
        )
        flash(msg, "success" if success else "error")
        return redirect(url_for("class_list"))
    return render_template("classes.html", classes=[], show_drop_form=True, drop_date=class_date, drop_time=class_time)

@app.route("/classes/<class_date>/<class_time>/delete")
def delete_class(class_date, class_time):
    success, msg = classes.delete_class(class_date, class_time)
    flash(msg, "success" if success else "error")
    return redirect(url_for("class_list"))

# sales
@app.route("/sales")
def sales_list():
    rows = sales.list_sales()
    return render_template("sales.html", sales=rows)

@app.route("/sales/add", methods=["GET", "POST"])
def add_sale():
    if request.method == "POST":
        success, msg = sales.record_sale(
            name=request.form["customer_name"],
            phone=request.form["customer_phone"],
            sale_date=request.form["sale_date"],
            sale_time=request.form.get("sale_time", "00:00"),
            price=request.form["amount"],
            payment_method=request.form.get("payment_method"),
            buyer=request.form.get("buyer"),
            sale_type=request.form.get("sale_type"),
        )
        flash(msg, "success" if success else "error")
        return redirect(url_for("sales_list"))
    return render_template("sales.html", sales=[], show_add_form=True)

@app.route("/sales/<int:transaction_id>/edit", methods=["GET", "POST"])
def edit_sale(transaction_id):
    sale = sales.get_sale(transaction_id)
    if not sale:
        flash("Sale not found", "error")
        return redirect(url_for("sales_list"))

    if request.method == "POST":
        success, msg = sales.update_sale_price(
            transaction_id=transaction_id,
            new_price=request.form["amount"]
        )
        flash(msg, "success" if success else "error")
        return redirect(url_for("sales_list"))

    return render_template("sales.html", sales=[], show_edit_form=True,
                          edit_sale=sale, edit_id=transaction_id)

@app.route("/sales/<int:transaction_id>/delete", methods=["GET", "POST"])
def delete_sale(transaction_id):
    success, msg = sales.delete_sale(transaction_id)
    flash(msg, "success" if success else "error")
    return redirect(url_for("sales_list"))

# reports
@app.route("/reports")
def reports_page():
    return render_template("reports.html")
# activated to update page when user hitting buttons
@app.route("/reports/revenue")
def reports_page_rev():
    # .args.get() only works for GET, use .form[''] for POST
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

@app.route("/schedule/<name>/<phone>")
def personclass(name, phone):
    return render_template("details.html", person = name, p=phone, schedule = reports.schedule_lookup(name, phone))

# run
if __name__ == "__main__":
    app.run(debug=True)