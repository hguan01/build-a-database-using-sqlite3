import sqlite3

#### Step 1: Create Database ####
con = sqlite3.connect("employee.db")

#### Step 2: Create Tables ####
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS department")
cur.execute('''CREATE TABLE department (dep_ID INTEGER NOT NULL PRIMARY KEY, 
               dep_Name TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS employee (
               emp_ID INTEGER NOT NULL PRIMARY KEY,
               emp_name TEXT,
               emp_address TEXT,
               dep_ID INTEGER, FOREIGN KEY(dep_ID) REFERENCES department(dep_ID))''')

#### Step 3: Insert Records Into Table ####
dep_data = [("123", "Dev"),
            ("234", "QA"),
            ("567", "Sys Admin"),
            ("890", "Customer Support")]

emp_data = [("999", "John", "TX", "123"),
            ("888", "Sid", "NY", "567"),
            ("777", "Kim", "CA", "123"),
            ("666", "Katy", "CA", "234"),
            ("555", "Tom", "TX", "567")]

cur.executemany("INSERT INTO department VALUES (?, ?)", dep_data)
cur.executemany("INSERT INTO employee VALUES(?, ?, ?, ?)", emp_data)

con.commit()
# con.close()

#### Step 4: Select Records From Table ####
## Example 1
records = cur.execute("SELECT * FROM department ORDER BY dep_ID ASC")

for row in records:
    print(row)

con.commit()

## Example 2
cur.execute("SELECT * FROM employee WHERE emp_ID = ?", (666,))
print(cur.fetchone())
con.commit()









