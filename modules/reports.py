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
    SELECT * 
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