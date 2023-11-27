from flask import Flask, json, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route('/isbns', methods=['GET'])
def isbn_list():
    with open('books.json') as json_data:
        result = []
        data = json.load(json_data)
        for book in data['books']:
            result.append(book['isbn'])
        return result


@app.route('/isbns/<isbn>', methods=['GET'])
def isbn_details(isbn):
    with open('books.json') as json_data:
        result = []
        data = json.load(json_data)
        for book in data['books']:
            if book['isbn'] == isbn:
                result.append(book)
    if result:
        return result
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/authors/<expression>', methods=['GET'])
def author_list(expression):
    with open('books.json') as json_data:
        result = []
        data = json.load(json_data)
        for book in data['books']:
            if expression in book['title']:
                result.append(book['author'])
        return result

