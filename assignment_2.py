import sqlite3

def create_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (product_id INTEGER PRIMARY KEY, name TEXT, price REAL, quantity INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers
                      (supplier_id INTEGER PRIMARY KEY, name TEXT, location TEXT)''')

    # Insert sample data
    cursor.execute("INSERT INTO products VALUES (1, 'Laptop', 999.99, 100)")
    cursor.execute("INSERT INTO products VALUES (2, 'Smartphone', 599.99, 200)")
    cursor.execute("INSERT INTO products VALUES (3, 'Headphones', 49.99, 150)")

    cursor.execute("INSERT INTO suppliers VALUES (1, 'TechCorp', 'New York')")
    cursor.execute("INSERT INTO suppliers VALUES (2, 'ElectroMart', 'Los Angeles')")

    conn.commit()
    print("Database initialized successfully.")
    conn.close()

def execute_query(query, params=()):
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()

def run_queries():
    print("Checking database state...")
    tables = execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('products', 'suppliers')")
    
    if tables is None or len(tables) != 2:
        print("Database tables don't exist. Creating new database...")
        create_database()
        print("New database created. Running queries again.")
        run_queries()
        return

    print("\nRunning queries:")
    print("Basic queries:")
    print("All products:", execute_query("SELECT * FROM products"))
    print("Products over $500:", execute_query("SELECT * FROM products WHERE price > ?", (500,)))

    print("\nJoin queries:")
    print("Inner join:", execute_query("SELECT p.product_id, p.name, s.name AS supplier_name "
                                        "FROM products p INNER JOIN suppliers s ON p.supplier_id = s.supplier_id"))
    print("Left join:", execute_query("SELECT p.product_id, p.name, s.name AS supplier_name "
                                       "FROM products p LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id"))

    print("\nAggregate queries:")
    print("Average price per product:", execute_query("SELECT AVG(price) FROM products"))
    print("Total quantity sold:", execute_query("SELECT SUM(quantity) FROM products"))

    print("\nGrouping:")
    print("Products grouped by category:", execute_query("SELECT name, price, quantity "
                                                        "FROM products GROUP BY price < ?, price >= ?",
                                                        ((500, 1000),)))

    print("\nOrder by:")
    print("Products ordered by price:", execute_query("SELECT * FROM products ORDER BY price DESC"))

    print("\nLimit:")
    print("First 2 products:", execute_query("SELECT * FROM products LIMIT 2"))

if __name__ == "__main__":
    run_queries()
