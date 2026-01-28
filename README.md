IN-MEMORY LIBRARY MANAGEMENT API (FLASK)
======================================

A simple REST API built using Flask to manage a library’s book inventory using strictly in-memory storage.


1️. PROJECT TITLE & GOAL
--------------------------------------------------
The goal of this project is to build a simple REST API using Flask that manages a library’s book inventory using strictly in-memory storage, allowing users to add, retrieve, search, and delete books.


2️. SETUP INSTRUCTIONS
--------------------------------------------------
**Prerequisites**

* Python 3.12.8

* pip (Python package manager)

**Steps to Run the Project Locally**

1. Install dependencies
pip install -r requirements.txt

2. Run the application
python app.py

**Once started, the application runs at:**

http://127.0.0.1:5000

3️. THE LOGIC (HOW I THOUGHT)
--------------------------------------------------

**Why I chose this approach**

I chose Flask because it is lightweight, easy to understand, and well-suited for building small REST APIs. Since the task explicitly required strictly in-memory storage, I avoided using any database or file system and stored all book data in a Python list during runtime.



**Data Structure**

Each book is represented as a dictionary containing:

* id

* title

* author

* year

**How the API works**

* **POST /books:** Adds a new book.

* **GET /books:** Retrieves all books.

* **GET /books/{id}:** Retrieves a specific book by its ID.

* **GET /books/search?year=YYYY:** Filters books by publication year.

* **DELETE /books/{id}:** Removes a book from the inventory.


4️. OUTPUT SCREENSHOTS
--------------------------------------------------
The screenshots below demonstrate that the API is working correctly.

* Required Proof: GET /books
<img width="1360" height="717" alt="Screenshot 2026-01-28 110049" src="https://github.com/user-attachments/assets/b283f17d-6a31-44b7-92cf-e50309dabc64" />


--------------------------------------------------

* POST /books
<img width="1360" height="717" alt="Screenshot 2026-01-28 110049" src="https://github.com/user-attachments/assets/acb65db6-8cac-4a92-9810-50e1b6ab0275" />



--------------------------------------------------
* GET /books/{id}
<img width="1354" height="715" alt="Screenshot 2026-01-28 105453" src="https://github.com/user-attachments/assets/6b8e0262-98dc-42d1-bc47-5d66416a0d00" />



--------------------------------------------------
* GET /books/search?year=2024
<img width="1361" height="718" alt="Screenshot 2026-01-28 110114" src="https://github.com/user-attachments/assets/a659d4c4-3cc6-449d-9e5f-7b5cd336ace4" />



--------------------------------------------------
* DELETE /books/{id}
<img width="1352" height="711" alt="Screenshot 2026-01-28 110158" src="https://github.com/user-attachments/assets/aadfedf8-6a84-4abf-bc64-97d635c6b1f2" />

--------------------------------------------------
5️. FUTURE IMPROVEMENTS
--------------------------------------------------


- Persist data using a lightweight database such as SQLite so that book records are retained across server restarts.
- Add proper request validation to ensure all incoming data follows a strict schema and prevents invalid inputs.
- Write unit tests for each API endpoint to verify correctness and handle edge cases.
- Improve error handling and return more descriptive HTTP status codes.
- Add basic request logging to help with debugging and monitoring API usage.

ADDITIONAL NOTES
--------------------------------------------------
This project was intentionally kept simple and focused to clearly demonstrate backend fundamentals such as API design, in-memory data handling, and clean request-response flow.

Submission Checklist
--------------------------------------------------
[x] Runs locally without external APIs

[x] Uses strictly in-memory storage

[x] All required endpoints implemented

[x] Screenshots embedded (not linked)

[*] Clean and readable code

[x] Public GitHub repository
