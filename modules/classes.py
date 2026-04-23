
# modules/classes.py — Class & enrollment CRUD
# Schedule class · enroll/drop student · list by date or teacher


from db import fetch_all, fetch_one, execute_query

def create_class(class_date, class_time, class_type, duration=None, attendance=0):
    execute_query("""
        INSERT INTO Class (class_date, class_time, class_type, duration, attendance)
        VALUES (%s, %s, %s, %s, %s)
    """, (class_date, class_time, class_type, duration, attendance))
    return True, f"Class created successfully"

def list_classes_by_date():
    return fetch_all("""
        SELECT c.class_date, c.class_time, c.class_type
        FROM Class c
        ORDER BY c.class_date, c.class_time
    """)

def enroll_customer(name, phone, class_date, class_time):
    customer = fetch_one("""
        SELECT Name, Phone
        FROM Customer
        Where Name = %s and Phone = %s
    """, (name, phone))

    if not customer:
        return False, "Customer not found"

    class_exists = fetch_one("""
        SELECT Class_Date, Class_Time
        FROM Class
        WHERE Class_Date = %s AND Class_Time = %s
    """, (class_date, class_time))

    if not class_exists:
        return False, "Class not found"

    execute_query("""
        INSERT INTO PersonClass (name, phone, class_date, class_time)
        VALUES (%s, %s, %s, %s)
    """, (name, phone, class_date, class_time))
    return True, "Customer enrolled successfully"

def drop_customer(name, phone, class_date, class_time):
    enrollment = fetch_one("""
        SELECT Name, Phone, Class_Date, Class_Time
        FROM PersonClass
        WHERE Name = %s AND Phone = %s AND Class_Date = %s AND Class_Time = %s
    """, (name, phone, class_date, class_time))

    if not enrollment:
        return False, "Enrollment not found"

    execute_query("""
        DELETE FROM PersonClass
        WHERE Name = %s AND Phone = %s AND Class_Date = %s AND Class_Time = %s
    """, (name, phone, class_date, class_time))
    return True, "Customer dropped from class successfully"

