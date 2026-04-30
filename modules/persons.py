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


def add_teacher(name, phone, number_of_classes_taught=0):
    if get_person(name, phone):
        return False, "Teacher already exists"
    # Insert with empty email since email is required in schema
    execute_query(
        "INSERT INTO person (name, phone, email) VALUES (%s, %s, '')",
        (name, phone)
    )
    execute_query(
        "INSERT INTO teacher (name, phone, number_of_classes_taught) VALUES (%s, %s, %s)",
        (name, phone, number_of_classes_taught)
    )
    return True, f"Teacher {name} added successfully"

# update teacher
def update_teacher(old_name, old_phone, new_name, new_phone, number_of_classes_taught):
    # If the key is changing, do a manual migration
    if (old_name, old_phone) != (new_name, new_phone):
        # Get current email
        person = fetch_one("SELECT email FROM person WHERE name = %s AND phone = %s", (old_name, old_phone))
        email = person[0] if person else ''
        # Insert new person row
        execute_query(
            "INSERT INTO person (name, phone, email) VALUES (%s, %s, %s)",
            (new_name, new_phone, email)
        )
        # Update teacher to new key and classes taught
        execute_query(
            "UPDATE teacher SET name = %s, phone = %s, number_of_classes_taught = %s WHERE name = %s AND phone = %s",
            (new_name, new_phone, number_of_classes_taught, old_name, old_phone)
        )
        # Delete old person row
        execute_query(
            "DELETE FROM person WHERE name = %s AND phone = %s",
            (old_name, old_phone)
        )
    else:
        # Only update classes taught
        execute_query(
            "UPDATE teacher SET number_of_classes_taught = %s WHERE name = %s AND phone = %s",
            (number_of_classes_taught, old_name, old_phone)
        )
    return True, f"Teacher {old_name} updated successfully"

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
    # deletes teacher (if present) and then person to avoid FK constraint
    if not get_person(name, phone):
        return False, "No person with that name and phone number"
    # Try to delete from teacher first (safe even if not a teacher)
    execute_query(
        "DELETE FROM teacher WHERE name = %s AND phone = %s",
        (name, phone)
    )
    execute_query(
        "DELETE FROM person WHERE name = %s AND phone = %s",
        (name, phone)
    )
    return True, f"{name} deleted successfully"