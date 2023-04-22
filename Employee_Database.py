import sqlite3

# Open a connection to the database
conn = sqlite3.connect('mydatabase.db')

# Create employee table
conn.execute('''
    CREATE TABLE employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name varchar(255) NOT NULL,
        email TEXT CHECK(email LIKE '%@%'),
        password varchar(255) NOT NULL,
        role TEXT,
        dob Date,
        gender TEXT,
        status TEXT
    );
''')

# Create employee_address table
conn.execute('''
    CREATE TABLE employee_address (
        employee_id INTEGER REFERENCES employee(id),
        address Varchar(255) NOT NULL,
        PRIMARY KEY (employee_id, address)
    );
''')

# Create employee_salary table
conn.execute('''
    CREATE TABLE employee_salary (
        employee_id INTEGER REFERENCES employee(id),
        salary INTEGER,
        PRIMARY KEY (employee_id, salary)
    );
''')

# Create supplier table
conn.execute('''
    CREATE TABLE supplier (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT CHECK(name GLOB '*[a-zA-Z]*'),
        email TEXT CHECK(email LIKE '%@%'),
        status TEXT
    );
''')

# Create supplier_contact table
conn.execute('''
    CREATE TABLE supplier_contact (
        supplier_id INTEGER REFERENCES supplier(id),
        contact TEXT CHECK(phone GLOB '[0-9]*'),
        PRIMARY KEY (supplier_id, contact)
    );
''')

# Create supplier_address table
conn.execute('''
    CREATE TABLE supplier_address (
        supplier_id INTEGER REFERENCES supplier(id),
        address varchar(255) NOT NULL,
        PRIMARY KEY (supplier_id, address)
    );
''')

# Create category table
conn.execute('''
    CREATE TABLE category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    );
''')

# Create product table
conn.execute('''
    CREATE TABLE product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER REFERENCES category(id),
        name TEXT CHECK(name GLOB '*[a-zA-Z]*'),
        price TEXT,
        quantity INTEGER,
        status TEXT
    );
''')

# Create product_supplier table
conn.execute('''
    CREATE TABLE product_supplier (
        product_id INTEGER REFERENCES product(id),
        supplier_id INTEGER REFERENCES supplier(id),
        PRIMARY KEY (product_id, supplier_id)
    );
''')

# Commit changes and close the connection
conn.commit()
conn.close()
