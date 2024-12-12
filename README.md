# Car Rental System

## Overview

The **Car Rental System** is a Django-based application designed to manage car rentals efficiently. It provides a comprehensive solution for managing employees, customers, cars, and rental transactions. This system includes the following functionalities:

- Employee and customer management
- Car catalog management
- Rental booking and tracking

## Features

- **Employee Management:** Employees can be added with details such as name, email, position, and password.
- **Customer Management:** Customers are registered with details like name, email, phone number, address, and password.
- **Car Management:** Cars are categorized based on type and availability status.
- **Rental Transactions:** Rentals can be created and tracked, including the status of each rental.

## Installation

Follow these steps to set up the project on your local system:

### Prerequisites

- Python 3.8+
- Django 3.2+

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/carrentalsystem.git
   cd carrentalsystem
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at:

   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Models

### 1. Employee

| Field         | Type            | Description                          |
|---------------|-----------------|--------------------------------------|
| `user`        | ForeignKey(User)| Links to Django User (optional).     |
| `name`        | CharField       | Name of the employee.                |
| `email`       | EmailField      | Email of the employee.               |
| `position`    | CharField       | Job position (optional).             |
| `password`    | CharField       | Password for the employee.           |
| `created_date`| DateTimeField   | Date of record creation.             |

### 2. Customer

| Field         | Type            | Description                          |
|---------------|-----------------|--------------------------------------|
| `user`        | ForeignKey(User)| Links to Django User (optional).     |
| `name`        | CharField       | Name of the customer.                |
| `email`       | EmailField      | Email of the customer.               |
| `phone`       | CharField       | Contact number (optional).           |
| `address`     | CharField       | Address of the customer (optional).  |
| `password`    | CharField       | Password for the customer.           |
| `created_date`| DateTimeField   | Date of record creation.             |

### 3. Car

| Field         | Type            | Description                          |
|---------------|-----------------|--------------------------------------|
| `name`        | CharField       | Name of the car.                     |
| `model`       | CharField       | Model of the car.                    |
| `year`        | IntegerField    | Manufacturing year.                  |
| `type`        | CharField       | Type of car (e.g., SUV, Sedan, etc.).|
| `status`      | CharField       | Availability status.                 |
| `created_date`| DateTimeField   | Date of record creation.             |

### 4. Rental

| Field         | Type            | Description                          |
|---------------|-----------------|--------------------------------------|
| `start_date`  | DateField       | Start date of rental.                |
| `end_date`    | DateField       | End date of rental.                  |
| `customer`    | ForeignKey(Customer)| Customer renting the car.          |
| `employee`    | ForeignKey(Employee)| Employee managing the rental.      |
| `car`         | ForeignKey(Car) | Car being rented.                    |
| `status`      | CharField       | Status of the rental (Pending, etc.).|
| `created_date`| DateTimeField   | Date of record creation.             |

## Usage

1. **Admin Dashboard:**
   - Manage employees, customers, cars, and rentals.
   - Track the status of each rental transaction.

2. **Customer Operations:**
   - Customers can view available cars and request rentals.

3. **Employee Operations:**
   - Employees can manage rental requests and update statuses.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
