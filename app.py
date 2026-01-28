from flask import Flask, request, jsonify

app = Flask(__name__)

# in-memory
books = []


@app.route("/")
def home():
    return "Library API is running"


@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data provided"}), 400

    if "id" not in data or "title" not in data or "author" not in data or "year" not in data:
        return jsonify({"message": "Required fields missing"}), 400

    #duplicate
    for book in books:
        if book["id"] == data["id"]:
            return jsonify({"message": "Book with this id already exists"}), 400

    books.append(data)
    return jsonify({"message": "Book added", "book": data}), 201


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/books/search", methods=["GET"])
def search_books():
    year = request.args.get("year")

    if not year:
        return jsonify({"message": "Year parameter required"}), 400

    result = []
    for book in books:
        if str(book["year"]) == year:
            result.append(book)

    return jsonify(result)


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})

    return jsonify({"message": "Book not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
