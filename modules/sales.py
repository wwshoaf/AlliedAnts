# modules/sales.py — Sale CRUD + purchase transaction
# Record sale · update payment · delete · wrap INSERT in transaction

from db import fetch_one, fetch_all, execute_query, get_connection

def list_sales():
    return fetch_all("SELECT transaction_id, sale_date, name, price FROM Sale ORDER BY sale_date DESC")

def get_sale(transaction_id):
    return fetch_one(
        "SELECT * FROM Sale WHERE transaction_id = %s",
        (transaction_id,)
    )

# Record sale
def record_sale(name, phone, sale_date, sale_time, price,
                class_date=None, class_time=None):
    customer = fetch_one(
        "SELECT name FROM Customer WHERE name = %s AND phone = %s",
        (name, phone)
    )
    if not customer:
        return False, "No customer with that name and phone number"

    conn = get_connection()
    if not conn:
        return False, "Database connection failed"
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Sale (name, phone, sale_date, sale_time, price) "
            "VALUES (%s, %s, %s, %s, %s)",
            (name, phone, sale_date, sale_time, price)
        )
        # optionally enroll customer in a class in the same transaction
        if class_date and class_time:
            cursor.execute(
                "INSERT INTO PersonClass (name, phone, pc_date, pc_time) "
                "VALUES (%s, %s, %s, %s)",
                (name, phone, class_date, class_time)
            )
        conn.commit()
        return True, f"Sale recorded for {name} — ${price}"
    except Exception as e:
        conn.rollback()
        return False, f"Transaction failed: {e}"
    finally:
        conn.close()


# Update the price on an existing sale
def update_sale_price(transaction_id, new_price):
    if not get_sale(transaction_id):
        return False, "No sale with that transaction ID"
    execute_query(
        "UPDATE Sale SET price = %s WHERE transaction_id = %s",
        (new_price, transaction_id)
    )
    return True, f"Sale {transaction_id} updated to ${new_price}"


# Delete a sale record
def delete_sale(transaction_id):
    if not get_sale(transaction_id):
        return False, "No sale with that transaction ID"
    execute_query(
        "DELETE FROM Sale WHERE transaction_id = %s",
        (transaction_id,)
    )
    return True, f"Sale {transaction_id} deleted"
