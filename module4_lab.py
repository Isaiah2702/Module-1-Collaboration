from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list of books
books = [
    {
        'id': 1,
        'book_name': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'publisher': 'HarperCollins'
    }
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((b for b in books if b['id'] == id), None)
    return jsonify(book) if book else (jsonify({'message': 'Book not found'}), 404)

# Create a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': books[-1]['id'] + 1 if books else 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update an existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    book['book_name'] = data['book_name']
    book['author'] = data['author']
    book['publisher'] = data['publisher']
    return jsonify(book)

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return jsonify({'message': f'Book with id {id} deleted'})

if __name__ == '__main__':
    app.run(debug=True)
