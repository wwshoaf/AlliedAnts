# modules/reports.py — SELECT-heavy report queries
# Revenue by period · classes per teacher · attendance lookup
from db import fetch_all, fetch_one

# total transaction count and revenue within a time period
def revenue_by_date(start, end):
    return fetch_one("""
    SELECT COUNT(*), SUM(price)
    FROM Sale
    WHERE sale_date >= %s AND sale_date <= %s
    """, (start,end))

# detailed record of all transaction within a time period
def all_trans(start, end):
    return fetch_all("""
    SELECT transaction_id, name, phone, sale_date, sale_time, price, payment_method, type
    FROM Sale
    WHERE sale_date >= %s AND sale_date <= %s
    ORDER BY sale_date, sale_time
    """, (start,end))

# teacher KPI rank
def classes_per_teacher():
    return fetch_all("""
    SELECT *
    FROM Teacher
    ORDER BY number_of_classes_taught DESC
    """)

# attendance rank across all classes
def attendance_report():
    return fetch_all("""
    SELECT *
    FROM Class
    ORDER BY attendance DESC
    """)

# look up anyone's class schedule
def schedule_lookup(name, phone):
    return fetch_all("""
    SELECT class_date, class_time, class_type, duration
    FROM teacherschedule
    WHERE teacher_name = %s AND phone = %s
    ORDER BY class_date ASC, class_time ASC
    """, (name, phone))

# see the list of persons enrolled in a class
def class_enrollment(date, time):
    return fetch_all("""
    SELECT name, role, phone, email
    FROM activeenrollments
    WHERE pc_date = %s AND pc_time = %s
    ORDER BY name ASC
    """, (date, time))

# look up a person's shopping history
def trans_history(name, phone):
    return fetch_all("""
    SELECT transaction_id, sale_date, sale_time, sale_type, price, payment_method
    FROM customerpurchasehistory
    WHERE buyer_name = %s AND buyer_phone = %s
    ORDER BY transaction_id
    """, (name, phone))