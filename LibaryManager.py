#Initialize empty lists, set, and dictionary
books_list = []
authors_set = set()
books_dict = {}

#Add books
books_list.append("Python Programing")
authors_set.add("Jhon Smith")
books_dict["Python Prigraming"] = "Jhon Smith"

books_list.append("Data Structure and Alogorithms")
authors_set.add("Jane Doe")
books_dict["Data Structure and Alogorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Jhonson")
books_dict["Machine Learning Basics"] = "Alice Jhonson"

#Search for Books
search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found!")

#Display all books
print("Lists of Books:")
for book in books_list:
    print(Book)
            

