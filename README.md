# 📦 Inventory Restock Management System

A Python-based inventory management application that reads inventory data from a CSV file, identifies items that require restocking, assigns priority levels, calculates reorder quantities, generates a restock report, simulates an email alert, and exports the results to a new CSV file.

---

## 📌 Project Overview

This project automates the process of checking inventory levels by comparing the current stock quantity with the predefined reorder threshold. It helps warehouse managers quickly identify products that need replenishment.

---

## ✨ Features

- Read inventory data from a CSV file
- Store each record using Python dictionaries
- Compare current quantity with reorder threshold
- Identify items that need restocking
- Assign priority levels (Low / Critical)
- Calculate reorder quantity
- Generate a formatted restock report
- Simulate an inventory email alert
- Export the report to a new CSV file
- Handle invalid or missing data using exception handling

---

## 🛠️ Technologies Used

- Python 3
- CSV Module
- File Handling
- Exception Handling
- Dictionaries
- Lists
- Conditional Statements
- Loops

---

## 📂 Project Structure

```
Inventory-Restock-Management/
│
├── main.py
├── stock.csv
├── restock_report.csv
└── README.md
```

---

## 📄 Input File (stock.csv)

Example:

```csv
item_name,current_quantity,reorder_threshold
Rice,25,30
Sugar,15,20
Salt,15,20
Salt,50,25
Oil,5,15
Tea Powder,40,40
Soap,2,20
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/python-inventory-assessment.git
```

2. Navigate to the project folder

```bash
cd python-inventory-assessment
```

3. Run the program

```bash
python main.py
```

or

```bash
py main.py
```

---

## 📋 Sample Output

```
==================================================
RESTOCK REPORT
==================================================

Item Name      : Rice
Current Stock  : 25
Threshold      : 30
Priority       : Low
Reorder Qty    : 5

Item Name      : Sugar
Current Stock  : 15
Threshold      : 20
Priority       : Low
Reorder Qty    : 5

Item Name      : Oil
Current Stock  : 5
Threshold      : 15
Priority       : Low
Reorder Qty    : 10

Item Name      : Soap
Current Stock  : 2
Threshold      : 20
Priority       : Critical
Reorder Qty    : 18
```

---

## 📤 Output Files

The application generates:

- `restock_report.csv`

It contains all items that require restocking along with:

- Item Name
- Current Quantity
- Reorder Threshold
- Priority
- Reorder Quantity

---

## 🔮 Future Improvements

- Send real email notifications using SMTP
- Connect to a database (MySQL or SQLite)
- Build a graphical user interface (GUI)
- Add supplier information
- Schedule automatic inventory checks
- Generate charts and analytics

---

## 👨‍💻 Author

**Anandakannan S**

B.Sc. Computer Science (2026)

Aspiring Front-End & Python Developer

GitHub: https://github.com/your-username

---

## 📜 License

This project is created for educational and assessment purposes.
