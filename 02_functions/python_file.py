import mysql.connector 

# Database connection 
def connect(): 
    try: 
        return mysql.connector.connect( 
            host="localhost", 
            user="root", 
            password="K@#est4002", 
            database="Pratham_college" 
        ) 
    except mysql.connector.Error as err: 
        print(f"Error connecting to database: {err}") 
        return None 

# Function to create the 'students' table 
def create_table(conn): 
    cursor = conn.cursor() 
    query = """ 
        CREATE TABLE IF NOT EXISTS students ( 
            Student_ID INT AUTO_INCREMENT, 
            Student_Name VARCHAR(255) NOT NULL, 
            Course VARCHAR(255) NOT NULL, 
            Age INT NOT NULL, 
            PRIMARY KEY (Student_ID) 
        ) 
    """ 
    cursor.execute(query) 
    conn.commit() 
    print("Table created successfully!") 
    cursor.close() 

# Function to add a new student record 
def add_student(conn): 
    name = input("Enter Student Name: ") 
    course = input("Enter Course: ") 
    age = int(input("Enter Age: ")) 

    cursor = conn.cursor() 
    query = "INSERT INTO students (Student_Name, Course, Age) VALUES (%s, %s, %s)" 
    values = (name, course, age) 
    cursor.execute(query, values) 
    conn.commit() 
    print("Student added successfully!") 
    cursor.close() 

# Function to delete a student record by ID 
def delete_student(conn): 
    student_id = int(input("Enter Student ID to delete: ")) 

    cursor = conn.cursor() 
    query = "DELETE FROM students WHERE Student_ID = %s" 
    cursor.execute(query, (student_id,)) 
    conn.commit() 
    print("Student deleted successfully!") 
    cursor.close() 

# Function to update a student record by ID 
def update_student(conn): 
    student_id = int(input("Enter Student ID to update: ")) 
    name = input("Enter new Student Name: ") 
    course = input("Enter new Course: ") 
    age = int(input("Enter new Age: ")) 

    cursor = conn.cursor() 
    query = "UPDATE students SET Student_Name = %s, Course = %s, Age = %s WHERE Student_ID = %s" 
    values = (name, course, age, student_id) 
    cursor.execute(query, values) 
    conn.commit() 
    print("Student updated successfully!") 
    cursor.close() 

# Function to view all student records 
def view_students(conn): 
    cursor = conn.cursor() 
    query = "SELECT * FROM students" 
    cursor.execute(query) 
    results = cursor.fetchall() 

    print("\n--- Students List ---") 
    for row in results: 
        print(f"ID: {row[0]}, Name: {row[1]}, Course: {row[2]}, Age: {row[3]}") 
    cursor.close() 

# Main menu 
def menu(): 
    conn = connect() 
    if conn is None:
        return  # Exit if connection fails

    create_table(conn)  # Create the 'students' table if it does not exist 

    while True: 
        print("\n--- Student Database Navigation ---") 
        print("1. Add Student") 
        print("2. Delete Student") 
        print("3. Update Student") 
        print("4. View Students") 
        print("5. Exit") 
         
        choice = input("Enter your choice: ") 
         
        if choice == '1': 
            add_student(conn) 
        elif choice == '2': 
            delete_student(conn) 
        elif choice == '3': 
            update_student(conn) 
        elif choice == '4': 
            view_students(conn) 
        elif choice == '5': 
            print("Exiting...") 
            break 
        else: 
            print("Invalid choice. Please try again.") 

    conn.close()  # Close the connection when done

# Run the menu 
if __name__ == "__main__": 
    menu()