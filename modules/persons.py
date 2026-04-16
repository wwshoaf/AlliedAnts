# modules/persons.py — Person, Teacher, Customer CRUD
# Add/list/update/delete · %s prepared statements throughout

from db import fetch_all, fetch_one, execute_query


# read operations
def list_customers():
    # return all customers as tuple list
    return fetch_all("""
        SELECT p.Name, p.Phone, p.Email, c.PaymentMethod
        FROM Person p
        JOIN Customer c ON p.NAME AND p.Phone = c.Phone
        ORDER BY p.Name
                     """)

def list_teachers():
    # all teachers as tuple list
    return fetch_all("""
        SELECT p.Name, p.Phone, p.Email
        FROM Person p
        JOIN Teacher t ON p.NAME AND p.Phone = t.Phone
        ORDER BY p.Name
                     """)

def get_person(name, phone):
    return fetch_one("""
                     SELECT Name, Phone, Email
                     FROM Person
                     WHERE Name = %s AND Phone = %s
                     """, (name, phone))

# create operations
def add_customer(name, phone, email, payment):
    if get_person(name, phone):
        return False, "Customer already exists"
    execute_query("" \
        "INSERT INTO Person (Name, Phone, Email) " \
        "VALUES (%s, %s, %s)", 
        (name, phone, email))
    execute_query("" \
        "INSERT INTO Customer (Name, Phone, PaymentMethod) " \
        "VALUES (%s, %s, %s)", 
        (name, phone, payment))
    
    return True, f"Customer {name} added successfully"


def add_teacher(name, phone, email):
    if get_person(name, phone):
        return False, "Teacher already exists"
    execute_query("" \
        "INSERT INTO Person (Name, Phone, Email) " \
        "VALUES (%s, %s, %s)", 
        (name, phone, email))
    execute_query("" \
        "INSERT INTO Teacher (Name, Phone, NumberOfClassesTaught) " \
        "VALUES (%s, %s, 0)", 
        (name, phone))    
    
    return True, f"Teacher {name} added successfully"

# update ops
def update_payment_method(name, phone, new_payment):
    existing = fetch_one(
        "SELECT Name FROM Customer WHERE Name = %s AND Phone = %s",
        (name, phone)
    )
    if not existing:
        return False, "No customer with that name and phone number"
    
    execute_query(
        "UPDATE Customer SET PaymentMethod = %s WHERE Name = %s AND Phone = %s",
        (new_payment, name, phone)
    )
    return True, f"Payment method updated to {new_payment}"


# delete ops
def delete_person(name, phone):
    # deletes person and should cascade to customer/teacher
    if not get_person(name, phone):
        return False, "No person with that name and phone number"
    execute_query(
        "DELETE FROM Person WHERE Name = %s AND Phone = %s",
        (name, phone)
    )

    return True, f"{name} deleted successfully"