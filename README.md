# 🏨 Hotel Reservation System

A console-based Hotel Reservation System built with **Python** using **Object-Oriented Programming (OOP)** principles. The application allows hotel staff to manage rooms, customers, and reservations through an interactive command-line interface.

This project is designed to practice clean code organization, modular programming, and OOP concepts while simulating a real-world hotel reservation workflow.

---

## ✨ Features

### 🏨 Room Management

* View all hotel rooms
* Add new rooms
* Remove existing rooms
* View room availability
* Display room details

### 👤 Customer Management

* Register new customers
* Search customers
* View customer information

### 📅 Reservation Management

* Book a room
* Cancel reservations
* Check out customers
* View all reservations
* Prevent double-booking of occupied rooms

### 📊 Hotel Statistics

* Total number of rooms
* Available rooms
* Occupied rooms
* Total reservations
* Hotel occupancy summary

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Modules
* Classes & Objects
* Constructors
* Static Methods
* Class Methods
* Inheritance
* Polymorphism
* Properties (`@property`)
* Decorators

---

## 📂 Project Structure

```text
hotel-reservation-system/
│
├── main.py
├── menu.py
├── database.py
├── utils.py
│
├── models/
│   ├── room.py
│   ├── customer.py
│   ├── reservation.py
│   └── hotel.py
│
├── README.md
└── .gitignore
```

---

## 📌 Classes

### 🏨 Hotel

Responsible for managing the hotel and coordinating room reservations.

### 🚪 Room

Represents an individual hotel room including:

* Room Number
* Room Type
* Price
* Availability

### 👤 Customer

Represents a hotel customer including:

* Customer ID
* Name
* Phone Number
* Email Address

### 📅 Reservation

Represents a reservation made by a customer including:

* Reservation ID
* Customer
* Room
* Check-in Date
* Check-out Date
* Reservation Status

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/kidus-yo/Hotel Reservation System.git
```

2. Navigate to the project directory.

```bash
cd hotel-reservation-system
```

3. Run the application.

```bash
python main.py
```

---

## 📚 Concepts Practiced

* Object-Oriented Programming
* Modular Programming
* Data Modeling
* Lists of Objects
* Class Design
* Function Decomposition
* Code Reusability
* Separation of Concerns

---

## 🚀 Future Improvements

* Save reservations to files
* Load hotel data automatically
* User authentication
* Employee management
* Payment processing
* Room categories
* Discount system
* Receipt generation
* Search and filtering
* Reservation history
* Date validation
* GUI version with PyQt5
* Database integration (SQLite/MySQL)

---

## 🎯 Learning Objectives

This project was created to strengthen practical skills in:

* Python Programming
* Software Design
* Object-Oriented Programming
* Building modular applications
* Real-world project organization

---

## 👨‍💻 Author

**Kidus Yonas**

Computer Science | Python Developer | Aspiring AI Engineer

If you found this project helpful or interesting, feel free to ⭐ the repository.
