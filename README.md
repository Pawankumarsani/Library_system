#  Library Management System (Python)

A simple **Library Management System** built using Python and Object-Oriented Programming concepts.  
This project demonstrates how to manage books, members, and borrow/return records.

---

##  Features
- Add, remove, search, and list books
- Add, remove, and list members
- Borrow and return books with status tracking
- Human-readable outputs using `__str__`

---

##  Classes
- **Book** → stores `isbn`, `title`, `author`
- **Member** → stores `member_id`, `name`, `email`
- **BorrowRecord** → links a member and book, tracks `returned` status
- **Library** → manages collections and operations

---

##  Example Usage
```python
lib = Library()
lib.add_book(Book(20232, "Maths", "Dr. Ramanujan"))
lib.add_member(Member("Joe", 1, "joe334@gmail.com"))
print(lib.borrow_book(1, 20232))
print(lib.return_book(1, 20232))
