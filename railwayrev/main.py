import mysql.connector
from getpass import getpass
import hashlib
import re
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# MySQL connection parameters
username = 'your_username'
password = getpass('Enter password: ')
host = 'your_host'
database = 'railway_reservation'

try:
    # Establish a connection to the MySQL database
    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    # Create a cursor object to execute SQL queries
    cursor = cnx.cursor()
    logging.info("Connected to the database successfully.")

except mysql.connector.Error as err:
    logging.error(f"Error connecting to the database: {err}")
    exit(1)


# Function to hash passwords using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to validate email using regular expressions
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


# Function to validate date input
def validate_date(date_str):
    try:
        return bool(re.match(r'\d{4}-\d{2}-\d{2}', date_str))
    except ValueError:
        return False


# Function to create tables in the database
def create_tables():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE,
                password VARCHAR(100),
                email VARCHAR(100),
                PRIMARY KEY (id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE,
                password VARCHAR(100),
                email VARCHAR(100),
                PRIMARY KEY (id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS trains (
                id INT AUTO_INCREMENT,
                train_number INT UNIQUE,
                train_name VARCHAR(100),
                source_station VARCHAR(50),
                destination_station VARCHAR(50),
                schedule TIME,
                PRIMARY KEY (id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INT AUTO_INCREMENT,
                user_id INT,
                train_id INT,
                booking_date DATE,
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (train_id) REFERENCES trains(id)
            );
        """)
        cnx.commit()
        logging.info("Tables created successfully.")
    except mysql.connector.Error as err:
        logging.error(f"Error creating tables: {err}")
        cnx.rollback()


# Function to login for users
def login_user(username, password):
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hash_password(password)))
        user = cursor.fetchone()
        return user
    except mysql.connector.Error as err:
        logging.error(f"Error during user login: {err}")
        return None


# Function to signup for users
def signup_user(username, password, email):
    if not validate_email(email):
        print("Invalid email format.")
        return
    try:
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, hash_password(password), email))
        cnx.commit()
        logging.info("User signup successful.")
    except mysql.connector.Error as err:
        logging.error(f"Error during user signup: {err}")
        cnx.rollback()


# Function to login for employees
def login_employee(username, password):
    try:
        cursor.execute("SELECT * FROM employees WHERE username = %s AND password = %s", (username, hash_password(password)))
        employee = cursor.fetchone()
        return employee
    except mysql.connector.Error as err:
        logging.error(f"Error during employee login: {err}")
        return None


# Function to signup for employees
def signup_employee(username, password, email):
    if not validate_email(email):
        print("Invalid email format.")
        return
    try:
        cursor.execute("INSERT INTO employees (username, password, email) VALUES (%s, %s, %s)", (username, hash_password(password), email))
        cnx.commit()
        logging.info("Employee signup successful.")
    except mysql.connector.Error as err:
        logging.error(f"Error during employee signup: {err}")
        cnx.rollback()


# Function to view train schedule
def view_train_schedule():
    try:
        cursor.execute("SELECT * FROM trains")
        trains = cursor.fetchall()
        for train in trains:
            print(f"Train Number: {train[1]}, Train Name: {train[2]}, Source: {train[3]}, Destination: {train[4]}, Schedule: {train[5]}")
    except mysql.connector.Error as err:
        logging.error(f"Error viewing train schedule: {err}")


# Function to book a ticket
def book_ticket(user_id, train_id, booking_date):
    if not validate_date(booking_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    try:
        cursor.execute("INSERT INTO bookings (user_id, train_id, booking_date) VALUES (%s, %s, %s)", (user_id, train_id, booking_date))
        cnx.commit()
        logging.info("Ticket booked successfully.")
    except mysql.connector.Error as err:
        logging.error(f"Error booking ticket: {err}")
        cnx.rollback()


# Function to cancel a ticket
def cancel_ticket(booking_id):
    try:
        cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        cnx.commit()
        logging.info("Ticket cancelled successfully.")
    except mysql.connector.Error as err:
        logging.error(f"Error cancelling ticket: {err}")
        cnx.rollback()


# Main function to interact with the railway reservation system
def main():
    create_tables()

    while True:
        print("1. User Login")
        print("2. User Signup")
        print("3. Employee Login")
        print("4. Employee Signup")
        print("5. View Train Schedule")
        print("6. Book a Ticket")
        print("7. Cancel a Ticket")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            user = login_user(username, password)
            if user:
                print("Login successful!")
            else:
                print("Invalid username or password.")
        elif choice == "2":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            email = input("Enter email: ")
            signup_user(username, password, email)
        elif choice == "3":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            employee = login_employee(username, password)
            if employee:
                print("Login successful!")
            else:
                print("Invalid username or password.")
        elif choice == "4":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            email = input("Enter email: ")
            signup_employee(username, password, email)
        elif choice == "5":
            view_train_schedule()
        elif choice == "6":
            user_id = int(input("Enter user ID: "))
            train_id = int(input("Enter train ID: "))
            booking_date = input("Enter booking date (YYYY-MM-DD): ")
            book_ticket(user_id, train_id, booking_date)
        elif choice == "7":
            booking_id = int(input("Enter booking ID: "))
            cancel_ticket(booking_id)
        elif choice == "8":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
