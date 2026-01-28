from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
books = []

# Helper function
def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


# 1. POST /books - Add a book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    required_fields = ["id", "title", "author", "year"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({
            "status": "error",
            "message": "Missing required fields"
        }), 400

    if find_book(data["id"]):
        return jsonify({
            "status": "error",
            "message": "Book with this ID already exists"
        }), 400

    books.append(data)

    return jsonify({
        "status": "success",
        "message": "Book added successfully",
        "data": data
    }), 201


# 2. GET /books/<id> - Get book by ID
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = find_book(book_id)

    if not book:
        return jsonify({
            "status": "error",
            "message": "Book not found"
        }), 404

    return jsonify({
        "status": "success",
        "data": book
    })


# EXTRA (useful): GET /books - Get all books
@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify({
        "status": "success",
        "data": books
    })


# 3. GET /books/search?year=2024
@app.route("/books/search", methods=["GET"])
def search_books():
    year = request.args.get("year")

    if not year:
        return jsonify({
            "status": "error",
            "message": "Year query parameter is required"
        }), 400

    filtered_books = [book for book in books if str(book["year"]) == year]

    return jsonify({
        "status": "success",
        "data": filtered_books
    })


# 4. DELETE /books/<id>
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = find_book(book_id)

    if not book:
        return jsonify({
            "status": "error",
            "message": "Book not found"
        }), 404

    books.remove(book)

    return jsonify({
        "status": "success",
        "message": "Book deleted successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)
