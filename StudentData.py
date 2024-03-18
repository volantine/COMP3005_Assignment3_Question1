import psycopg2
from psycopg2 import Error

# Database connection parameters
# These parameters are to be changed by TA/user
DB_NAME = "Student"
DB_USER = "postgres"
DB_PASSWORD = "student"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect():
    """Connect to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def disconnect(connection):
    """Disconnect from the PostgreSQL database."""
    if connection:
        connection.close()

def getAllStudents():
    """Retrieves and displays all records from the students table."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            for student in students:
                print(student)
            cursor.close()
    finally:
        disconnect(connection)

def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the students table."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                           (first_name, last_name, email, enrollment_date))
            connection.commit()
            print("Student added successfully")
            cursor.close()
    finally:
        disconnect(connection)

def updateStudentEmail(student_id, new_email):
    """Updates the email address for a student with the specified student_id."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                           (new_email, student_id))
            connection.commit()
            print("Email updated successfully")
            cursor.close()
    finally:
        disconnect(connection)

def deleteStudent(student_id):
    """Deletes the record of the student with the specified student_id."""
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE student_id = %s",
                           (student_id,))
            connection.commit()
            print("Student deleted successfully")
            cursor.close()
    finally:
        disconnect(connection)


if __name__ == "__main__":
    getAllStudents()

    # Test addStudent function
    addStudent("Abraham", "Cole", "abraham@example.com", "2024-03-18")

    # Check database after adding a student
    getAllStudents()

    # Test updateStudentEmail function
    updateStudentEmail(2, "alina@example.com")

    # Check database after updating email
    getAllStudents()

    # Test deleteStudent function
    deleteStudent(1)

    # Check database after deleting a student
    getAllStudents()
