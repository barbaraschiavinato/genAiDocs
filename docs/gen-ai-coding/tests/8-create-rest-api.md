# 8. Create a REST API

## Prompt

Generate a simple REST API in Python using Flask that has CRUD operations for managing books. Each book should have an ID, title, author, and publication year.

## Results


### Amazon Q

```python

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory book database
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publication_year": 1960},
    {"id": 2, "title": "1984", "author": "George Orwell", "publication_year": 1949},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publication_year": 1925}
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    new_book['id'] = max([book['id'] for book in books]) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        updated_book = request.get_json()
        book.update(updated_book)
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted'}), 204
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)


```
This API provides the following endpoints:

- `GET /books`: Retrieves a list of all books.

- `GET /books/<int:book_id>`: Retrieves a single book by its ID.

- `POST /books`: Creates a new book.

- `PUT /books/<int:book_id>`: Updates an existing book by its ID.

- `DELETE /books/<int:book_id>`: Deletes a book by its ID.

The book data is stored in an in-memory list, but in a real-world application, you would likely use a database or a more persistent storage solution.

To run the API, save the code in a file (e.g., `app.py`) and run the following command in your terminal:

```
python app.py
```

The API will start running on `http://localhost:5000/`.

### GitHub Copilot


```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list to store books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2000},
    {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2001},
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book.update(request.get_json())
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

To run this API, save the code in a file (e.g., `app.py`) and run the following command in your terminal:

```bash
python app.py
```

The API will start running on `http://localhost:5000/`.

### Axet Gaia


```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Create a list to store the books
books = []

# Create a route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Create a route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'message': 'Book not found'})

# Create a route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': request.json['id'],
        'title': request.json['title'],
        'author': request.json['author'],
        'publication_year': request.json['publication_year']
    }
    books.append(new_book)
    return jsonify({'message': 'Book added successfully'})

# Create a route to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.json['title']
            book['author'] = request.json['author']
            book['publication_year'] = request.json['publication_year']
            return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'})

# Create a route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'})

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we use the Flask framework to create a REST API with CRUD operations for managing books. The `/books` route is used to get all books and add a new book. The `/books/<int:book_id>` route is used to get a specific book, update an existing book, and delete a book. The books are stored in a list, and the data is sent and received in JSON format.

To run this code, you need to have Flask installed. You can install it using `pip install flask`. Then, you can run the code using `python filename.py`, where `filename.py` is the name of the Python file containing the code.


### ChatGpt 4


```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], publication_year=data['publication_year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

# Get a single book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)
    book.title = data['title']
    book.author = data['author']
    book.publication_year = data['publication_year']
    db.session.commit()
    return jsonify(book.to_dict()), 200

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

**How to Use This API**

1. **Create a Book**: Send a `POST` request to `/books` with JSON body containing `title`, `author`, and `publication_year`.
2. **Read All Books**: Send a `GET` request to `/books`.
3. **Read One Book**: Send a `GET` request to `/books/{book_id}` where `book_id` is the ID of the book you want to fetch.
4. **Update a Book**: Send a `PUT` request to `/books/{book_id}` with a JSON body containing updated `title`, `author`, and `publication_year`.
5. **Delete a Book**: Send a `DELETE` request to `/books/{book_id}`.

This code provides a fully functional REST API for a simple book management system. You can further enhance it by adding more features such as sorting, filtering, or user authentication based on your requirements.

### Meta.ai

Here is a simple implementation of a REST API using Flask for managing books:
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for books (replace with a database in a real application)
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2020},
    {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2021},
    {"id": 3, "title": "Book 3", "author": "Author 3", "year": 2022},
]

# GET all books
@app.route("/api/books", methods=["GET"])
def get_all_books():
    return jsonify(books)

# GET a book by ID
@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

# POST a new book
@app.route("/api/books", methods=["POST"])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "year": request.json["year"],
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT (update) a book
@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    book["title"] = request.json.get("title", book["title"])
    book["author"] = request.json.get("author", book["author"])
    book["year"] = request.json.get("year", book["year"])
    return jsonify(book)

# DELETE a book
@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    books.remove(book)
    return jsonify({"message": "Book deleted"})

if __name__ == "__main__":
    app.run(debug=True)
```
This API has the following endpoints:

- `GET` `/api/books`: Returns a list of all books.
- `GET` `/api/books/<book_id>`: Returns a book by its ID.
- `POST` `/api/books`: Creates a new book.
- `PUT` `/api/books/<book_id>`: Updates a book by its ID.
- `DELETE` `/api/books/<book_id>`: Deletes a book by its ID.
- 
You can run the API by saving this code to a file (e.g., (`link unavailable`)) and running it with Python:
```bash
$ python (link unavailable)
```
Then, you can use a tool like curl or a REST client to interact with the API:
```bash
$ curl http://localhost:5000/api/books
```
This is a very basic implementation and you should consider using a database instead of an in-memory list for storing books. Also, error handling and input validation are minimal, so you should improve those aspects in a real application.

### Gemini


```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (replace with a database for persistence)
books = []
next_id = 1


def generate_id():
    global next_id
    next_id += 1
    return next_id


def find_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None


# Create a book (POST)
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('author') or not data.get('publication_year'):
        return jsonify({'error': 'Missing required fields'}), 400

    new_book = {
        'id': generate_id(),
        'title': data['title'],
        'author': data['author'],
        'publication_year': data['publication_year'],
    }
    books.append(new_book)
    return jsonify(new_book), 201  # Created


# Read all books (GET)
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)


# Read a book by ID (GET)
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404  # Not Found
    return jsonify(book)


# Update a book by ID (PUT)
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Missing data'}), 400

    book = find_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    # Update book fields with provided data (or keep existing values)
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['publication_year'] = data.get('publication_year', book['publication_year'])

    return jsonify(book)


# Delete a book by ID (DELETE)
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404

    books.remove(book)
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation of the Completed Code:**

1. **CRUD Operations:**
   - **Create (POST) and Update (PUT):** These functionalities are already implemented as described previously.
   - **Read All (GET):** Retrieves and returns a JSON list of all books in the `books` list.
   - **Read by ID (GET):** Finds a book by its ID and returns the book object if found, otherwise a 404 Not Found error.
   - **Delete by ID (DELETE):** Finds a book by its ID, removes it from the `books` list, and returns a success message.

2. **Error Handling:**
   - Each route checks for potential errors like missing data or non-existent books. It returns appropriate error messages with corresponding HTTP status codes for better client handling.

3. **In-memory Storage (Note):**
   - This example uses an in-memory list for simplicity. In a real application, you would replace it with a database (e.g., SQLAlchemy) for persistent storage and proper data management.

4. **Running the API:**
   - Save the code as a Python file (e.g., book_api.py).
   - Run the script: `python book_api.py`.
   - With the API running (debug mode enabled), you can use tools like Postman or curl to interact with the API endpoints.

This is a basic but functional REST API demonstrating CRUD operations for managing books. Remember to handle authentication and authorization for real-world deployments.

## Analysis

### Amazon Q
   - **Pros**: Provides a complete Flask app with CRUD operations, effectively handling different HTTP methods and responding appropriately.
   - **Cons**: Uses a simple in-memory list for storage which isn't practical for production but suffices for demonstration.
   - **Code Example**: Offers a clear structure, initializing, updating, and deleting entries correctly.
     ```python
     # Amazon's approach is straightforward and correctly implements Flask routing and request handling.
     ```

### GitHub Copilot
   - **Pros**: Includes all CRUD operations, similar to Amazon Q, and manages the state of books well.
   - **Cons**: Lacks explicit ID handling in the POST method, assuming that the client sends a complete book object including a unique ID.
   - **Code Example**:
     ```python
     # Copilot's solution assumes client-side responsibility for some data management tasks.
     ```

### Axet Gaia
   - **Pros**: Introduces explicit ID handling in the POST method which is a good practice for APIs.
   - **Cons**: Somewhat repetitive and verbose in the PUT and DELETE methods; could be optimized or simplified.
   - **Code Example**:
     ```python
     # Gaia's code manually handles each field update in PUT requests, which might not be efficient for larger data structures.
     ```

### ChatGPT 4
   - **Pros**: Uses SQLAlchemy to manage a SQLite database, providing a more realistic and scalable solution.
   - **Cons**: More complex setup due to database integration, might be overkill for very simple or educational purposes.
   - **Code Example**:
     ```python
     # This approach with a database integration is robust and suitable for real-world applications.
     ```

### Meta.ai
   - **Pros**: Simple and direct Flask API similar to other solutions but includes basic error handling in the form of 404 responses.
   - **Cons**: Like others, uses an in-memory list; also, the update method doesn't handle non-existing fields gracefully.
   - **Code Example**:
     ```python
     # Meta's implementation is adequate for educational purposes but needs refinement for production use.
     ```

Certainly! Here's the analysis including Gemini's approach:

### Gemini
   - **Pros**: Introduces a structured and well-organized API setup that handles CRUD operations with clarity. The use of helper functions like `generate_id` and `find_book` improves code organization and reusability.
   - **Cons**: Still relies on an in-memory list, which limits its practicality for real-world applications where data persistence is key.
   - **Code Example**:
     ```python
     # Gemini's approach is thoughtful, introducing utility functions that make the code cleaner and potentially easier to maintain.
     ```

## Conclusion

**Best Implementation**: **ChatGPT 4**'s use of SQLAlchemy for database integration still stands out for its scalability and robustness, making it suitable for real-world applications.

**Worst Implementation**: While all the solutions have their merits, **GitHub Copilot**'s approach is less ideal for production due to its assumption about client-side ID management, which can lead to data inconsistency and other issues.

**Notable Mention**: **Gemini** deserves a special mention for its clean code structure and thoughtful function decomposition, which enhances code readability and maintenance. Although it still uses in-memory storage, the setup provides a solid foundation for further development and integration with database systems for persistence.