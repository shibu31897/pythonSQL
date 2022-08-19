from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
all_books = []
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

@app.route('/')
def home():
    return render_template("index.html",books = all_books)


@app.route("/add",methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book={
            "title" : request.form['title'],
            "author" : request.form['author'],
            "rating" : request.form['rating']
        }
        # cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
        # db.commit()
        all_books.append(new_book)
        return redirect(url_for('home'))
    print(all_books)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)