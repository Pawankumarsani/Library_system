# Book Class
 
class Book:
    def __init__(self,isbn,title,Author):
        self.isbn=isbn
        self.title=title
        self.Author=Author
    # __str__ human-readable    
    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.Author}"
    # Dev-readable
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, Author:{self.Author})'
    
#Member Class

class Member:
    def __init__(self,name,member_id,email):
        self.name=name
        self.member_id=member_id
        self.email=email
        
    def __str__(self):
        return f"Name: {self.name}, Member: {self.member_id},Email: {self.email}"
    def __repr__(self):
        return f'Member(name={self.name}, Member={self.member_id}, Email= {self.email})'
 
 #Borrowrecord Class   
    
class BorrowRecord:
    def __init__(self,Member,Book):
        self.member=Member
        self.book=Book
        self.returned=False
        
    def __str__(self):
        status= "Returned" if self.returned else "Borrowed"
        return f"member: {self.member.name}, book:{self.book.title} ({status})"
    
# Library Class

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowedrecord = []
        
    # -----------book management-----------
       
    def add_book(self,Book):
        self.books.append(Book)
    def remove_book(self,isbn):
        self.books = [b for b in self.books if b.isbn != isbn]
    def search_book(self,title):
        return [b for b in self.books if b.title.lower() == title.lower()]
    def list_books(self):
        return self.books
    
    #---------Member management-------------
    
    def add_member(self,member):
        self.members.append(member)
    def remove_member(self,member_id):
        self.members = [m for m in self.members if m.member_id != member_id ]
    def list_members(self):
        return (self.members)
    
    # ----------------Borrow and Return System----------------
    
    def borrow_book(self, member_id, isbn):
        # Find member and book
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if member and book:
            record = BorrowRecord(member, book)
            self.borrowedrecord.append(record)
            return f"{member.name} borrowed {book.title}"
        return "Member or Book not found."

    def return_book(self, member_id, isbn):
        # Find active borrow record
        for record in self.borrowedrecord:
            if record.member.member_id== member_id and record.book.isbn == isbn and not record.returned:
                record.returned = True
                return f"{record.member.name} returned {record.book.title}"
        return "No active borrow record found."

    def list_borrow_records(self):
        return self.borrowedrecord
    
if __name__ == "__main__":
    # Create library
    lib = Library()

    # Add books
    lib.add_book(Book(20232, "Maths", "Dr. Ramanujan"))
    lib.add_book(Book(20233, "Physics", "Einstein"))

    # Add members
    lib.add_member(Member("joe",1, "joe334@gmail.com"))
    lib.add_member(Member("max",2, "max5523@gmail.com"))

    # Borrow and return
    print(lib.borrow_book(1, 20232))   
    print(lib.borrow_book(2, 20233))   
    print(lib.return_book(1, 20232))   

    # Show borrow records
    for record in lib.list_borrow_records():
        print(record)

    # Show books and members
    print("Books:", lib.list_books())
    print("Members:", lib.list_members())