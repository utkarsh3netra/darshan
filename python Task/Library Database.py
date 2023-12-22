library = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "year": 1960},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "year": 1925},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "year": 1932}
]
print(library)

# 1 Task
book_genre = {}

for book in library:
    genre = book['genre']
    if genre in book_genre:
        book_genre[genre].append(book["title"])
    else:
        book_genre[genre] = [book["title"]]

for genre, book in book_genre.items():
    print(f"\n{genre}:{book}")

# 2 Task

old_book = {}
for book in library:
    genre = book['genre']
    if genre not in old_book or book["year"] < old_book[genre]["year"]:
        old_book[genre] = book
print("\nOld Book : ", old_book)

# 3 Task

author_book = {}
for book in library:
    author = book["author"]
    if author in author_book:
        author_book[author] += 1
    else:
        author_book[author] = 1

for author, count in author_book.items():
    print(f"\nauthor : \n{author}:{count}")
