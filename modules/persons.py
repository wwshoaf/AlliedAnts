# modules/persons.py — Person, Teacher, Customer CRUD
# Add/list/update/delete · %s prepared statements throughout

from db import fetch_all, fetch_one, execute_query


# read operations
def list_customers():
    # return all customers as tuple list
    return fetch_all("""
        SELECT p.name, p.phone, p.email, c.payment_method
        FROM person p
        JOIN customer c ON p.name = c.name AND p.phone = c.phone
        ORDER BY p.name
                     """)

def list_teachers():
    # all teachers as tuple list
    return fetch_all("""
        SELECT p.name, p.phone, p.email, t.number_of_classes_taught
        FROM person p
        JOIN teacher t ON p.name = t.name AND p.phone = t.phone
        ORDER BY p.name
                     """)

def get_person(name, phone):
    return fetch_one("""
                     SELECT name, phone, email
                     FROM person
                     WHERE name = %s AND phone = %s
                     """, (name, phone))

# create operations
def add_customer(name, phone, email, payment):
    if get_person(name, phone):
        return False, "customer already exists"
    
    ## NEED TO ADD TRANSACTION HERE
    execute_query("" \
        "INSERT INTO person (name, phone, email) " \
        "VALUES (%s, %s, %s)", 
        (name, phone, email))
    execute_query("" \
        "INSERT INTO customer (name, phone, payment_method) " \
        "VALUES (%s, %s, %s)", 
        (name, phone, payment))
    
    return True, f"customer {name} added successfully"


def add_teacher(name, phone, email):
    if get_person(name, phone):
        return False, "Teacher already exists"
    
    ## NEED TO ADD TRANSACTION HERE
    execute_query("" \
        "INSERT INTO person (name, phone, email) " \
        "VALUES (%s, %s, %s)", 
        (name, phone, email))
    execute_query("" \
        "INSERT INTO teacher (name, phone, number_of_classes_taught) " \
        "VALUES (%s, %s, 0)", 
        (name, phone))    
    
    return True, f"Teacher {name} added successfully"

# update ops
def update_payment_method(name, phone, new_payment):
    existing = fetch_one(
        "SELECT name FROM customer WHERE name = %s AND phone = %s",
        (name, phone)
    )
    if not existing:
        return False, "No customer with that name and phone number"
    
    execute_query(
        "UPDATE customer SET payment_method = %s WHERE name = %s AND phone = %s",
        (new_payment, name, phone)
    )
    return True, f"Payment method updated to {new_payment}"


# delete ops
def delete_person(name, phone):
    # deletes person and should cascade to customer/teacher
    if not get_person(name, phone):
        return False, "No person with that name and phone number"
    execute_query(
        "DELETE FROM person WHERE name = %s AND phone = %s",
        (name, phone)
    )

    return True, f"{name} deleted successfully"