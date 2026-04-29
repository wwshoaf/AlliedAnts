
# modules/classes.py — Class & enrollment CRUD
# Schedule class · enroll/drop student · list by date or teacher


from db import fetch_all, fetch_one, execute_query, get_connection

def create_class(class_date, class_time, class_type, duration=None, attendance=0):
    result = execute_query("""
        INSERT INTO Class (class_date, class_time, class_type, duration, attendance)
        VALUES (%s, %s, %s, %s, %s)
    """, (class_date, class_time, class_type, duration, attendance))
    if not result:
        return False, "Failed to create class"
    
    return True, f"Class created successfully"

def list_classes_by_date():
    return fetch_all("""
        SELECT class_date, class_time, class_type, duration, attendance
        FROM Class
        ORDER BY class_date, class_time
    """)

def enroll_customer(name, phone, class_date, class_time):
    # verify class exists
    class_exists = fetch_one("""
        SELECT class_date, class_time
        FROM Class
        WHERE class_date = %s AND class_time = %s
    """, (class_date, class_time))

    if not class_exists:
        return False, "Class not found"
    
    # Call stored procedure to enroll student
    conn = get_connection()
    if not conn:
        return False, "Database connection error"
    try:
        cursor = conn.cursor()
        cursor.callproc('EnrollStudent', (name, phone, class_date, class_time))
        conn.commit()
        return True, "Student enrolled successfully"

    except Exception as e:
        conn.rollback()
        return False, f"Error enrolling student: {str(e)}"
    finally:
        conn.close()

## CHANGE TO INCLUDE TRANSACTION
def drop_customer(name, phone, class_date, class_time):
    # verify enrollment exists
    enrollment = fetch_one("""
        SELECT name
        FROM PersonClass
        WHERE name = %s AND phone = %s AND pc_date = %s AND pc_time = %s
    """, (name, phone, class_date, class_time))

    if not enrollment:
        return False, "Enrollment not found"

    execute_query("""
        DELETE FROM PersonClass
        WHERE name = %s AND phone = %s AND pc_date = %s AND pc_time = %s
    """, (name, phone, class_date, class_time))

    #if they are a teacher, then decrement their number of classes taught
    is_teacher = fetch_one("""
        SELECT name
        FROM Teacher
        WHERE name = %s AND phone = %s
    """, (name, phone))
    if is_teacher:
        execute_query("""
            UPDATE Teacher
            SET number_of_classes_taught = number_of_classes_taught - 1
            WHERE name = %s AND phone = %s
        """, (name, phone))

    # decrement attendance for the class
    execute_query("""
        UPDATE Class
        SET attendance = attendance - 1
        WHERE class_date = %s AND class_time = %s
    """, (class_date, class_time))

    return True, "Customer dropped from class successfully"

def delete_class(class_date, class_time):
    # verify class exists
    class_exists = fetch_one("""
        SELECT class_date
        FROM Class
        WHERE class_date = %s AND class_time = %s
        """, (class_date, class_time))
    if not class_exists:
        return False, "Class not found"

    execute_query("""
        DELETE FROM Class
        WHERE class_date = %s AND class_time = %s
    """, (class_date, class_time))
    return True, "Class deleted successfully"

def list_enrollments(class_date, class_time):
    return fetch_all("""
        SELECT name, phone
        FROM PersonClass
        WHERE pc_date = %s AND pc_time = %s
        ORDER BY name
    """, (class_date, class_time))
