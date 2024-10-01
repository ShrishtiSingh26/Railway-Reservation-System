# Railway Reservation System

This project is a **Railway Reservation System** developed in Python, using MySQL as the backend database. It allows users and employees to interact with the railway system, perform actions like booking tickets, viewing train schedules, and managing trains, with separate functionalities for users and employees.

## Features

### User Functionality:
- **Signup/Login**: Users can sign up with a username, password (securely hashed), and email, or log in if they have an account.
- **View Train Schedule**: Users can view the train schedule for all available trains.
- **Book Tickets**: Users can book a train ticket by selecting a train and providing a booking date.
- **View Booked Tickets**: Users can view the list of tickets they have booked.
- **Cancel Tickets**: Users can cancel a booked ticket.

### Employee Functionality:
- **Signup/Login**: Employees can sign up or log in to the system.
- **Update Train Schedule**: Employees can modify the schedule of a particular train.
- **Add New Train**: Employees can add a new train to the system.
- **Delete Train**: Employees can remove an existing train from the system.

## Technologies Used
- **Python 3.x**: Core programming language used for the system logic.
- **MySQL**: Database management system used to store user, train, and booking data.
- **MySQL Connector**: A Python library used to connect to and interact with the MySQL database.
- **Hashlib**: A Python library used for hashing passwords for secure storage.
- **Logging**: Python logging module to log important actions and errors.

## Prerequisites
- Python 3.x installed on your system.
- MySQL server installed and running.
- MySQL Connector Python library. You can install it using:
  ```bash
  pip install mysql-connector-python
  ```

## Setup Instructions

1. **Clone the Repository** (or download the files):
   ```bash
   git clone https://github.com/your-repo/railway-reservation-system.git
   cd railway-reservation-system
   ```

2. **Database Setup**:
   - Create a new database in MySQL:
     ```sql
     CREATE DATABASE railway_reservation;
     ```
   - Update the connection parameters (username, password, host) in the script:
     ```python
     username = 'your_username'
     password = getpass('Enter password: ')
     host = 'your_host'
     ```

3. **Run the Program**:
   Simply run the Python script:
   ```bash
   python railway_reservation.py
   ```

4. **Creating Tables**:
   The script will automatically create the required tables (`users`, `employees`, `trains`, `bookings`) when it first runs.

## How to Use

### User Actions
1. **Signup**: Select option `2` to create a new user account.
2. **Login**: After signing up, log in with option `1`.
3. **View Train Schedule**: Use option `5` to view the current train schedules.
4. **Book Ticket**: Use option `7` to book a train ticket by providing a train ID and booking date.
5. **View Booked Tickets**: Use option `8` to view all the tickets you've booked.
6. **Cancel Ticket**: Use option `9` to cancel a booked ticket by providing the booking ID.

### Employee Actions
1. **Signup/Login**: Employees can sign up (option `4`) and log in (option `3`).
2. **Update Train Schedule**: Use option `10` to update the schedule of a particular train.
3. **Add a New Train**: Use option `11` to add a new train to the database.
4. **Delete Train**: Use option `12` to delete an existing train from the system.

### Exit the Program:
- Select option `13` to exit the system.

## Security Measures
- **Password Hashing**: User and employee passwords are stored securely using SHA-256 hashing.
- **SQL Injection Prevention**: All SQL queries are parameterized to prevent SQL injection attacks.
- **Logging**: The system logs important actions and errors for debugging and auditing purposes.

## Error Handling
The system includes error handling for common issues such as:
- Database connection errors.
- SQL query execution failures.
- Invalid user input (such as incorrect email formats or invalid booking dates).

## Future Enhancements
Some potential future improvements:
- Implementing more user-friendly error messages.
- Adding train seat selection and availability.
- Enhancing security with features like account lockout on multiple failed login attempts.
- Implementing a GUI for better user interaction.
