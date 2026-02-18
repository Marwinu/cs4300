
# List of Hunger Games books (title, author)
favorite_books = [
    ("The Hunger Games", "Suzanne Collins"),
    ("Catching Fire", "Suzanne Collins"),
    ("Mockingjay", "Suzanne Collins")
]

# Function to get the first books
def get_first_books(book_list, n=3):

    return book_list[:n]  # list slicing for n items

# Dictionary with student names and IDs
student_database = {
    "Julian Romero": 1301,
    "Alexander Topete": 3102,
    "Charlie Sanders": 4303,
    "David Dobrik": 2104
}

# Function to get student ID by name
def get_student_id(name):
# returns ID from the database
    return student_database.get(name)

if __name__ == "__main__":
    # Print the first three books
    first_books = get_first_books(favorite_books)
    print("First three books:")
    for title, author in first_books:
        print(f"{title} by {author}")

    # Get ID for David Dobrik
    student_name = "David Dobrik"
    student_id = get_student_id(student_name)
    if student_id:
        print(f"\nStudent ID for {student_name}: {student_id}")
    else:
        print(f"\nStudent was not found")