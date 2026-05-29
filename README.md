# API Data Fetcher with Search Filter

## Project Overview
This project is a Python-based API Data Fetcher that retrieves user data from a public API using the `requests` module. The program parses JSON data and allows users to search/filter results dynamically.

---

## Features
- Fetch API data using Requests module
- Parse JSON response
- Search and filter user data
- Exception handling for API errors
- User-friendly terminal output

---

## Technologies Used
- Python
- Requests Module
- JSON Parsing

---

## Project Structure

API-Data-Fetcher/
│
├── api_fetcher.py
├── README.md
└── screenshots/

---

## API Used
JSONPlaceholder API:
https://jsonplaceholder.typicode.com/users

---

## How to Run the Project

### Step 1: Install Python
Download Python from:
https://www.python.org/downloads/

---

### Step 2: Install Requests Module

Open terminal and run:

```bash
pip install requests
```

---

### Step 3: Run the Program

```bash
python api_fetcher.py
```

---

## Sample Input

```text
Enter name to search:
Leanne
```

---

## Sample Output

```text
===== API Data Fetcher =====

Total Users Fetched: 10

User Found
------------------------------
Name : Leanne Graham
Email: Sincere@april.biz
City : Gwenborough
```

---

## Concepts Used
- API Integration
- Requests Module
- JSON Handling
- Search Filtering
- Exception Handling

---

## Future Enhancements
- GUI Interface
- Multiple API support
- Export results to CSV/Excel
- Real-time API filtering

---

## Author
Developed as a Python API Integration and Automation Project.