# PRACTICE DATABASE
import sqlite3

# 1) DATABASE 
conn = sqlite3.connect("db1.db")
print("Database created")

# 2)  TABLES

sql1 = """
CREATE TABLE IF NOT EXISTS emp(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(50),
mob VARCHAR(20),
city VARCHAR(50)
)
"""
conn.execute(sql1)

sql2 = """
CREATE TABLE IF NOT EXISTS dept(
dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
dept_name VARCHAR(50),
location VARCHAR(50)
)
"""
conn.execute(sql2)

print("Tables created")


# 3) INSERT 

conn.execute('INSERT INTO emp(name, mob, city) VALUES ("Amit", "98910", "Jaipur")')
conn.execute('INSERT INTO emp(name, mob, city) VALUES ("Neha", "91230", "Delhi")')
conn.execute('INSERT INTO emp(name, mob, city) VALUES ("Ravi", "99885", "Ajmer")')

conn.execute('INSERT INTO dept(dept_name, location) VALUES ("CSE", "A")')
conn.execute('INSERT INTO dept(dept_name, location) VALUES ("IT", "B")')

conn.commit()
print("Records inserted")


# 4) SELECT 

print("\nAll Employees:")
res = conn.execute("SELECT * FROM emp")
for row in res:
    print(row)

print("\nEmployees from Jaipur:")
res = conn.execute("SELECT * FROM emp WHERE city='Jaipur'")
for row in res:
    print(row)

print("\nDepartments:")
res = conn.execute("SELECT * FROM dept")
for row in res:
    print(row)


# 5) UPDATE 

conn.execute("UPDATE emp SET city='Mumbai' WHERE name='Amit'")
conn.commit()
print("\nData updated ")


# 6) DELETE 

conn.execute("DELETE FROM emp WHERE name='Ravi'")
conn.commit()
print("Data deleted ")


print("\Employee Table:")
res = conn.execute("SELECT * FROM emp")
for row in res:
    print(row)

conn.close()