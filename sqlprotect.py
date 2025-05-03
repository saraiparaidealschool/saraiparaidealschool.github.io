import sqlite3

# SQLite database connection
def connect_db():
    conn = sqlite3.connect('school.db')
    return conn

# Function to create table (if not exists)
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

# Function to insert data securely using parameterized queries
def insert_student(name, age, grade):
    conn = connect_db()
    cursor = conn.cursor()
    # Using parameterized queries to avoid SQL injection
    cursor.execute('''
    INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
    ''', (name, age, grade))
    conn.commit()
    conn.close()

# Function to fetch student data securely using parameterized queries
def get_student_by_name(student_name):
    conn = connect_db()
    cursor = conn.cursor()
    # Using parameterized queries to avoid SQL injection
    cursor.execute('''
    SELECT * FROM students WHERE name = ?
    ''', (student_name,))
    student = cursor.fetchone()
    conn.close()
    return student

# Function to display all students
def display_all_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

# Main logic
if __name__ == '__main__':
    create_table()

    # Insert new student data (SQL Injection safe)
    insert_student('John Doe', 15, '10th Grade')
    insert_student('Jane Smith', 14, '9th Grade')

    # Fetch student data safely (SQL Injection safe)
    student = get_student_by_name('John Doe')
    if student:
        print(f"Student Found: ID={student[0]}, Name={student[1]}, Age={student[2]}, Grade={student[3]}")
    else:
        print("Student not found!")

    # Display all students
    students = display_all_students()
    print("All Students in the Database:")
    for student in students:
        print(f"ID={student[0]}, Name={student[1]}, Age={student[2]}, Grade={student[3]}")
