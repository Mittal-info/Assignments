
"""

Database creation



[x] Students table creation



[x] Add 6 students



[x] View all students



[x] Search by class



[x] Update monthly fee



[x] Delete student



[x] Parameterized SQL queries



[x] Commit and rowcount


"""


import pymysql


# STEP 1: Connect to MySQL server
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD"
)

cursor = connection.cursor()

# STEP 2: Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS tuition_fee_db")

cursor.close()
connection.close()


# STEP 3: Connect with database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="tuition_fee_db"
)

cursor = conn.cursor()


# STEP 4: Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    class_name VARCHAR(50),
    monthly_fee DECIMAL(10,2)
)
""")

conn.commit()

print("Table ready")


# STEP 5: Add Student
def add_student(name, class_name, monthly_fee):

    query = """
    INSERT INTO students (name, class_name, monthly_fee)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, class_name, monthly_fee))

    conn.commit()

    print("Student added successfully!")


# STEP 6: View All Students
def view_students():

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    if not records:
        print("No students found")
        return

    print("\n" + "-" * 65)
    print(f"{'ID':<8}{'NAME':<20}{'CLASS':<15}{'MONTHLY FEE':>15}")
    print("-" * 65)

    for row in records:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<15}{row[3]:>15}")

    print("-" * 65)


# STEP 7: Search Students by Class
def search_by_class(class_name):

    query = "SELECT * FROM students WHERE class_name = %s"

    cursor.execute(query, (class_name,))

    records = cursor.fetchall()

    if not records:
        print("No students found")
        return

    print("\nStudents in", class_name)

    print("-" * 65)
    print(f"{'ID':<8}{'NAME':<20}{'CLASS':<15}{'MONTHLY FEE':>15}")
    print("-" * 65)

    for row in records:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<15}{row[3]:>15}")

    print("-" * 65)


# STEP 8: Update Student Fee
def update_fee(student_id, new_fee):

    query = "UPDATE students SET monthly_fee = %s WHERE id = %s"

    cursor.execute(query, (new_fee, student_id))

    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Fee updated successfully!")


# STEP 9: Delete Student
def delete_student(student_id):

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Student deleted successfully!")


# STEP 10: Menu Driven Program
while True:

    print("\n===== TUITION FEE TRACKER =====")

    print("1. Add student")
    print("2. View all students")
    print("3. Search by class")
    print("4. Update fee")
    print("5. Delete student")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        class_name = input("Enter class: ")
        monthly_fee = float(input("Enter monthly fee: "))

        add_student(name, class_name, monthly_fee)

    elif choice == "2":

        view_students()

    elif choice == "3":

        class_name = input("Enter class name: ")

        search_by_class(class_name)

    elif choice == "4":

        student_id = int(input("Enter student ID: "))
        new_fee = float(input("Enter new monthly fee: "))

        update_fee(student_id, new_fee)

    elif choice == "5":

        student_id = int(input("Enter student ID: "))

        delete_student(student_id)

    elif choice == "0":

        print("Thank you for using Tuition Fee Tracker!")

        break

    else:

        print("Invalid choice! Please try again.")


# STEP 11: Close connection
cursor.close()
conn.close()
